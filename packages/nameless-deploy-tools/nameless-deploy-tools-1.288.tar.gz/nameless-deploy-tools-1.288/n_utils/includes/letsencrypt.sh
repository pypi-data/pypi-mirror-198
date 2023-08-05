#!/usr/bin/env bash

# dehydrated by lukas2511
# Source: https://dehydrated.io
#
# This script is licensed under The MIT License (see LICENSE for more information).

set -e
set -u
set -o pipefail
[[ -n "${ZSH_VERSION:-}" ]] && set -o SH_WORD_SPLIT && set +o FUNCTION_ARGZERO && set -o NULL_GLOB && set -o noglob
[[ -z "${ZSH_VERSION:-}" ]] && shopt -s nullglob && set -f

umask 077 # paranoid umask, we're creating private keys

# Close weird external file descriptors
exec 3>&-
exec 4>&-

VERSION="0.7.1"

# Find directory in which this script is stored by traversing all symbolic links
SOURCE="${0}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

BASEDIR="${SCRIPTDIR}"
ORIGARGS=("${@}")

# Generate json.sh path matching string
json_path() {
	if [ ! "${1}" = "-p" ]; then
		printf '"%s"' "${1}"
	else
		printf '%s' "${2}"
	fi
}

# Get string value from json dictionary
get_json_string_value() {
  local filter
  filter="$(printf 's/.*\[%s\][[:space:]]*"\([^"]*\)"/\\1/p' "$(json_path "${1:-}" "${2:-}")")"
  sed -n "${filter}"
}

# Get array values from json dictionary
get_json_array_values() {
  grep -E '^\['"$(json_path "${1:-}" "${2:-}")"',[0-9]*\]' | sed -e 's/\[[^\]*\][[:space:]]*//g' -e 's/^"//' -e 's/"$//'
}

# Get sub-dictionary from json
get_json_dict_value() {
  local filter
	echo "$(json_path "${1:-}" "${2:-}")"
  filter="$(printf 's/.*\[%s\][[:space:]]*\(.*\)/\\1/p' "$(json_path "${1:-}" "${2:-}")")"
  sed -n "${filter}" | jsonsh
}

# Get integer value from json
get_json_int_value() {
  local filter
  filter="$(printf 's/.*\[%s\][[:space:]]*\([^"]*\)/\\1/p' "$(json_path "${1:-}" "${2:-}")")"
  sed -n "${filter}"
}

# Get boolean value from json
get_json_bool_value() {
  local filter
  filter="$(printf 's/.*\[%s\][[:space:]]*\([^"]*\)/\\1/p' "$(json_path "${1:-}" "${2:-}")")"
  sed -n "${filter}"
}

# JSON.sh JSON-parser
# Modified from https://github.com/dominictarr/JSON.sh
# Original Copyright (c) 2011 Dominic Tarr
# Licensed under The MIT License
jsonsh() {

  throw() {
    echo "$*" >&2
    exit 1
  }

  awk_egrep () {
    local pattern_string=$1

    gawk '{
      while ($0) {
        start=match($0, pattern);
        token=substr($0, start, RLENGTH);
        print token;
        $0=substr($0, start+RLENGTH);
      }
    }' pattern="$pattern_string"
  }

  tokenize () {
    local GREP
    local ESCAPE
    local CHAR

    if echo "test string" | egrep -ao --color=never "test" >/dev/null 2>&1
    then
      GREP='egrep -ao --color=never'
    else
      GREP='egrep -ao'
    fi

    if echo "test string" | egrep -o "test" >/dev/null 2>&1
    then
      ESCAPE='(\\[^u[:cntrl:]]|\\u[0-9a-fA-F]{4})'
      CHAR='[^[:cntrl:]"\\]'
    else
      GREP=awk_egrep
      ESCAPE='(\\\\[^u[:cntrl:]]|\\u[0-9a-fA-F]{4})'
      CHAR='[^[:cntrl:]"\\\\]'
    fi

    local STRING="\"$CHAR*($ESCAPE$CHAR*)*\""
    local NUMBER='-?(0|[1-9][0-9]*)([.][0-9]*)?([eE][+-]?[0-9]*)?'
    local KEYWORD='null|false|true'
    local SPACE='[[:space:]]+'

    # Force zsh to expand $A into multiple words
    local is_wordsplit_disabled=$(unsetopt 2>/dev/null | grep -c '^shwordsplit$')
    if [ $is_wordsplit_disabled != 0 ]; then setopt shwordsplit; fi
    $GREP "$STRING|$NUMBER|$KEYWORD|$SPACE|." | egrep -v "^$SPACE$"
    if [ $is_wordsplit_disabled != 0 ]; then unsetopt shwordsplit; fi
  }

  parse_array () {
    local index=0
    local ary=''
    read -r token
    case "$token" in
      ']') ;;
      *)
        while :
        do
          parse_value "$1" "$index"
          index=$((index+1))
          ary="$ary""$value"
          read -r token
          case "$token" in
            ']') break ;;
            ',') ary="$ary," ;;
            *) throw "EXPECTED , or ] GOT ${token:-EOF}" ;;
          esac
          read -r token
        done
        ;;
    esac
    value=$(printf '[%s]' "$ary") || value=
    :
  }

  parse_object () {
    local key
    local obj=''
    read -r token
    case "$token" in
      '}') ;;
      *)
        while :
        do
          case "$token" in
            '"'*'"') key=$token ;;
            *) throw "EXPECTED string GOT ${token:-EOF}" ;;
          esac
          read -r token
          case "$token" in
            ':') ;;
            *) throw "EXPECTED : GOT ${token:-EOF}" ;;
          esac
          read -r token
          parse_value "$1" "$key"
          obj="$obj$key:$value"
          read -r token
          case "$token" in
            '}') break ;;
            ',') obj="$obj," ;;
            *) throw "EXPECTED , or } GOT ${token:-EOF}" ;;
          esac
          read -r token
        done
      ;;
    esac
    value=$(printf '{%s}' "$obj") || value=
    :
  }

  parse_value () {
    local jpath="${1:+$1,}${2:-}" isleaf=0 isempty=0 print=0
    case "$token" in
      '{') parse_object "$jpath" ;;
      '[') parse_array  "$jpath" ;;
      # At this point, the only valid single-character tokens are digits.
      ''|[!0-9]) throw "EXPECTED value GOT ${token:-EOF}" ;;
      *) value=$token
         # replace solidus ("\/") in json strings with normalized value: "/"
         value=$(echo "$value" | sed 's#\\/#/#g')
         isleaf=1
         [ "$value" = '""' ] && isempty=1
         ;;
    esac
    [ "$value" = '' ] && return
    [ -z "$jpath" ] && return # do not print head

    printf "[%s]\t%s\n" "$jpath" "$value"
    :
  }

  parse () {
    read -r token
    parse_value
    read -r token || true
    case "$token" in
      '') ;;
      *) throw "EXPECTED EOF GOT $token" ;;
    esac
  }

  tokenize | parse
}

# Create (identifiable) temporary files
_mktemp() {
  # shellcheck disable=SC2068
  mktemp ${@:-} "${TMPDIR:-/tmp}/dehydrated-XXXXXX"
}

# Check for script dependencies
check_dependencies() {
  # look for required binaries
  for binary in grep mktemp diff sed awk curl cut; do
    bin_path="$(command -v "${binary}" 2>/dev/null)" || _exiterr "This script requires ${binary}."
    [[ -x "${bin_path}" ]] || _exiterr "${binary} found in PATH but it's not executable"
  done

  # just execute some dummy and/or version commands to see if required tools are actually usable
  "${OPENSSL}" version > /dev/null 2>&1 || _exiterr "This script requires an openssl binary."
  _sed "" < /dev/null > /dev/null 2>&1 || _exiterr "This script requires sed with support for extended (modern) regular expressions."

  # curl returns with an error code in some ancient versions so we have to catch that
  set +e
  CURL_VERSION="$(curl -V 2>&1 | head -n1 | awk '{print $2}')"
  set -e
}

store_configvars() {
  __KEY_ALGO="${KEY_ALGO}"
  __OCSP_MUST_STAPLE="${OCSP_MUST_STAPLE}"
  __OCSP_FETCH="${OCSP_FETCH}"
  __OCSP_DAYS="${OCSP_DAYS}"
  __PRIVATE_KEY_RENEW="${PRIVATE_KEY_RENEW}"
  __PRIVATE_KEY_ROLLOVER="${PRIVATE_KEY_ROLLOVER}"
  __KEYSIZE="${KEYSIZE}"
  __CHALLENGETYPE="${CHALLENGETYPE}"
  __HOOK="${HOOK}"
  __PREFERRED_CHAIN="${PREFERRED_CHAIN}"
  __WELLKNOWN="${WELLKNOWN}"
  __HOOK_CHAIN="${HOOK_CHAIN}"
  __OPENSSL_CNF="${OPENSSL_CNF}"
  __RENEW_DAYS="${RENEW_DAYS}"
  __IP_VERSION="${IP_VERSION}"
}

reset_configvars() {
  KEY_ALGO="${__KEY_ALGO}"
  OCSP_MUST_STAPLE="${__OCSP_MUST_STAPLE}"
  OCSP_FETCH="${__OCSP_FETCH}"
  OCSP_DAYS="${__OCSP_DAYS}"
  PRIVATE_KEY_RENEW="${__PRIVATE_KEY_RENEW}"
  PRIVATE_KEY_ROLLOVER="${__PRIVATE_KEY_ROLLOVER}"
  KEYSIZE="${__KEYSIZE}"
  CHALLENGETYPE="${__CHALLENGETYPE}"
  HOOK="${__HOOK}"
  PREFERRED_CHAIN="${__PREFERRED_CHAIN}"
  WELLKNOWN="${__WELLKNOWN}"
  HOOK_CHAIN="${__HOOK_CHAIN}"
  OPENSSL_CNF="${__OPENSSL_CNF}"
  RENEW_DAYS="${__RENEW_DAYS}"
  IP_VERSION="${__IP_VERSION}"
}

hookscript_bricker_hook() {
  # Hook scripts should ignore any hooks they don't know.
  # Calling a random hook to make this clear to the hook script authors...
  if [[ -n "${HOOK}" ]]; then
    "${HOOK}" "this_hookscript_is_broken__dehydrated_is_working_fine__please_ignore_unknown_hooks_in_your_script" || _exiterr "Please check your hook script, it should exit cleanly without doing anything on unknown/new hooks."
  fi
}

# verify configuration values
verify_config() {
  [[ "${CHALLENGETYPE}" == "http-01" || "${CHALLENGETYPE}" == "dns-01" || "${CHALLENGETYPE}" == "tls-alpn-01" ]] || _exiterr "Unknown challenge type ${CHALLENGETYPE}... cannot continue."
  if [[ "${CHALLENGETYPE}" = "dns-01" ]] && [[ -z "${HOOK}" ]]; then
    _exiterr "Challenge type dns-01 needs a hook script for deployment... cannot continue."
  fi
  if [[ "${CHALLENGETYPE}" = "http-01" && ! -d "${WELLKNOWN}" && ! "${COMMAND:-}" = "register" ]]; then
    _exiterr "WELLKNOWN directory doesn't exist, please create ${WELLKNOWN} and set appropriate permissions."
  fi
  [[ "${KEY_ALGO}" == "rsa" || "${KEY_ALGO}" == "prime256v1" || "${KEY_ALGO}" == "secp384r1" ]] || _exiterr "Unknown public key algorithm ${KEY_ALGO}... cannot continue."
  if [[ -n "${IP_VERSION}" ]]; then
    [[ "${IP_VERSION}" = "4" || "${IP_VERSION}" = "6" ]] || _exiterr "Unknown IP version ${IP_VERSION}... cannot continue."
  fi
  [[ "${API}" == "auto" || "${API}" == "1" || "${API}" == "2" ]] || _exiterr "Unsupported API version defined in config: ${API}"
  [[ "${OCSP_DAYS}" =~ ^[0-9]+$ ]] || _exiterr "OCSP_DAYS must be a number"
}

# Setup default config values, search for and load configuration files
load_config() {
  # Check for config in various locations
  if [[ -z "${CONFIG:-}" ]]; then
    for check_config in "/etc/dehydrated" "/usr/local/etc/dehydrated" "${PWD}" "${SCRIPTDIR}"; do
      if [[ -f "${check_config}/config" ]]; then
        BASEDIR="${check_config}"
        CONFIG="${check_config}/config"
        break
      fi
    done
  fi

  # Preset
  CA_ZEROSSL="https://acme.zerossl.com/v2/DV90"
  CA_LETSENCRYPT="https://acme-v02.api.letsencrypt.org/directory"
  CA_LETSENCRYPT_TEST="https://acme-staging-v02.api.letsencrypt.org/directory"
  CA_BUYPASS="https://api.buypass.com/acme/directory"
  CA_BUYPASS_TEST="https://api.test4.buypass.no/acme/directory"

  # Default values
  CA="letsencrypt"
  OLDCA=
  CERTDIR=
  ALPNCERTDIR=
  ACCOUNTDIR=
  CHALLENGETYPE="http-01"
  CONFIG_D=
  CURL_OPTS=
  DOMAINS_D=
  DOMAINS_TXT=
  HOOK=
  PREFERRED_CHAIN=
  HOOK_CHAIN="no"
  RENEW_DAYS="30"
  KEYSIZE="4096"
  WELLKNOWN=
  PRIVATE_KEY_RENEW="yes"
  PRIVATE_KEY_ROLLOVER="no"
  KEY_ALGO=secp384r1
  OPENSSL=openssl
  OPENSSL_CNF=
  CONTACT_EMAIL=
  LOCKFILE=
  OCSP_MUST_STAPLE="no"
  OCSP_FETCH="no"
  OCSP_DAYS=5
  IP_VERSION=
  CHAINCACHE=
  AUTO_CLEANUP="no"
  DEHYDRATED_USER=
  DEHYDRATED_GROUP=
  API="auto"

  if [[ -z "${CONFIG:-}" ]]; then
    echo "#" >&2
    echo "# !! WARNING !! No main config file found, using default config!" >&2
    echo "#" >&2
  elif [[ -f "${CONFIG}" ]]; then
    echo "# INFO: Using main config file ${CONFIG}"
    BASEDIR="$(dirname "${CONFIG}")"
    # shellcheck disable=SC1090
    . "${CONFIG}"
  else
    _exiterr "Specified config file doesn't exist."
  fi

  if [[ -n "${CONFIG_D}" ]]; then
    if [[ ! -d "${CONFIG_D}" ]]; then
      _exiterr "The path ${CONFIG_D} specified for CONFIG_D does not point to a directory."
    fi

    # Allow globbing
    [[ -n "${ZSH_VERSION:-}" ]] && set +o noglob || set +f

    for check_config_d in "${CONFIG_D}"/*.sh; do
      if [[ -f "${check_config_d}" ]] && [[ -r "${check_config_d}" ]]; then
        echo "# INFO: Using additional config file ${check_config_d}"
        # shellcheck disable=SC1090
        . "${check_config_d}"
      else
        _exiterr "Specified additional config ${check_config_d} is not readable or not a file at all."
      fi
    done

    # Disable globbing
    [[ -n "${ZSH_VERSION:-}" ]] && set -o noglob || set -f
  fi

  # Check for missing dependencies
  check_dependencies

  has_sudo() {
    command -v sudo > /dev/null 2>&1 || _exiterr "DEHYDRATED_USER set but sudo not available. Please install sudo."
  }

  # Check if we are running & are allowed to run as root
  if [[ -n "$DEHYDRATED_USER" ]]; then
    command -v getent > /dev/null 2>&1 || _exiterr "DEHYDRATED_USER set but getent not available. Please install getent."

    TARGET_UID="$(getent passwd "${DEHYDRATED_USER}" | cut -d':' -f3)" || _exiterr "DEHYDRATED_USER ${DEHYDRATED_USER} is invalid"
    if [[ -z "${DEHYDRATED_GROUP}" ]]; then
      if [[ "${EUID}" != "${TARGET_UID}" ]]; then
        echo "# INFO: Running $0 as ${DEHYDRATED_USER}"
        has_sudo && exec sudo -u "${DEHYDRATED_USER}" "${0}" "${ORIGARGS[@]}"
      fi
    else
      TARGET_GID="$(getent group "${DEHYDRATED_GROUP}" | cut -d':' -f3)" || _exiterr "DEHYDRATED_GROUP ${DEHYDRATED_GROUP} is invalid"
      if [[ -z "${EGID:-}" ]]; then
        command -v id > /dev/null 2>&1 || _exiterr "DEHYDRATED_GROUP set, don't know current gid and 'id' not available... Please provide 'id' binary."
        EGID="$(id -g)"
      fi
      if [[ "${EUID}" != "${TARGET_UID}" ]] || [[ "${EGID}" != "${TARGET_GID}" ]]; then
        echo "# INFO: Running $0 as ${DEHYDRATED_USER}/${DEHYDRATED_GROUP}"
        has_sudo && exec sudo -u "${DEHYDRATED_USER}" -g "${DEHYDRATED_GROUP}" "${0}" "${ORIGARGS[@]}"
      fi
    fi
  elif [[ -n "${DEHYDRATED_GROUP}" ]]; then
    _exiterr "DEHYDRATED_GROUP can only be used in combination with DEHYDRATED_USER."
  fi

  # Remove slash from end of BASEDIR. Mostly for cleaner outputs, doesn't change functionality.
  [[ "$BASEDIR" != "/" ]] && BASEDIR="${BASEDIR%%/}"

  # Check BASEDIR and set default variables
  [[ -d "${BASEDIR}" ]] || _exiterr "BASEDIR does not exist: ${BASEDIR}"

  # Check for ca cli parameter
  if [ -n "${PARAM_CA:-}" ]; then
    CA="${PARAM_CA}"
  fi

  # Preset CAs
  if [ "${CA}" = "letsencrypt" ]; then
    CA="${CA_LETSENCRYPT}"
  elif [ "${CA}" = "letsencrypt-test" ]; then
    CA="${CA_LETSENCRYPT_TEST}"
  elif [ "${CA}" = "zerossl" ]; then
    CA="${CA_ZEROSSL}"
  elif [ "${CA}" = "buypass" ]; then
    CA="${CA_BUYPASS}"
  elif [ "${CA}" = "buypass-test" ]; then
    CA="${CA_BUYPASS_TEST}"
  fi

  if [[ -z "${OLDCA}" ]] && [[ "${CA}" = "https://acme-v02.api.letsencrypt.org/directory" ]]; then
    OLDCA="https://acme-v01.api.letsencrypt.org/directory"
  fi

  # Create new account directory or symlink to account directory from old CA
  # dev note: keep in mind that because of the use of 'echo' instead of 'printf' or
  # similar there is a newline encoded in the directory name. not going to fix this
  # since it's a non-issue and trying to fix existing installations would be too much
  # trouble
  CAHASH="$(echo "${CA}" | urlbase64)"
  [[ -z "${ACCOUNTDIR}" ]] && ACCOUNTDIR="${BASEDIR}/accounts"
  if [[ ! -e "${ACCOUNTDIR}/${CAHASH}" ]]; then
    OLDCAHASH="$(echo "${OLDCA}" | urlbase64)"
    mkdir -p "${ACCOUNTDIR}"
    if [[ -n "${OLDCA}" ]] && [[ -e "${ACCOUNTDIR}/${OLDCAHASH}" ]]; then
      echo "! Reusing account from ${OLDCA}"
      ln -s "${OLDCAHASH}" "${ACCOUNTDIR}/${CAHASH}"
    else
      mkdir "${ACCOUNTDIR}/${CAHASH}"
    fi
  fi

  [[ -f "${ACCOUNTDIR}/${CAHASH}/config" ]] && . "${ACCOUNTDIR}/${CAHASH}/config"
  ACCOUNT_KEY="${ACCOUNTDIR}/${CAHASH}/account_key.pem"
  ACCOUNT_KEY_JSON="${ACCOUNTDIR}/${CAHASH}/registration_info.json"
  ACCOUNT_ID_JSON="${ACCOUNTDIR}/${CAHASH}/account_id.json"
  ACCOUNT_DEACTIVATED="${ACCOUNTDIR}/${CAHASH}/deactivated"

  if [[ -f "${ACCOUNT_DEACTIVATED}" ]]; then
    _exiterr "Account has been deactivated. Remove account and create a new one using --register."
  fi

  if [[ -f "${BASEDIR}/private_key.pem" ]] && [[ ! -f "${ACCOUNT_KEY}" ]]; then
    echo "! Moving private_key.pem to ${ACCOUNT_KEY}"
    mv "${BASEDIR}/private_key.pem" "${ACCOUNT_KEY}"
  fi
  if [[ -f "${BASEDIR}/private_key.json" ]] && [[ ! -f "${ACCOUNT_KEY_JSON}" ]]; then
    echo "! Moving private_key.json to ${ACCOUNT_KEY_JSON}"
    mv "${BASEDIR}/private_key.json" "${ACCOUNT_KEY_JSON}"
  fi

  [[ -z "${CERTDIR}" ]] && CERTDIR="${BASEDIR}/certs"
  [[ -z "${ALPNCERTDIR}" ]] && ALPNCERTDIR="${BASEDIR}/alpn-certs"
  [[ -z "${CHAINCACHE}" ]] && CHAINCACHE="${BASEDIR}/chains"
  [[ -z "${DOMAINS_TXT}" ]] && DOMAINS_TXT="${BASEDIR}/domains.txt"
  [[ -z "${WELLKNOWN}" ]] && WELLKNOWN="/var/www/dehydrated"
  [[ -z "${LOCKFILE}" ]] && LOCKFILE="${BASEDIR}/lock"
  [[ -z "${OPENSSL_CNF}" ]] && OPENSSL_CNF="$("${OPENSSL}" version -d | cut -d\" -f2)/openssl.cnf"
  [[ -n "${PARAM_LOCKFILE_SUFFIX:-}" ]] && LOCKFILE="${LOCKFILE}-${PARAM_LOCKFILE_SUFFIX}"
  [[ -n "${PARAM_NO_LOCK:-}" ]] && LOCKFILE=""

  [[ -n "${PARAM_HOOK:-}" ]] && HOOK="${PARAM_HOOK}"
  [[ -n "${PARAM_DOMAINS_TXT:-}" ]] && DOMAINS_TXT="${PARAM_DOMAINS_TXT}"
  [[ -n "${PARAM_PREFERRED_CHAIN:-}" ]] && PREFERRED_CHAIN="${PARAM_PREFERRED_CHAIN}"
  [[ -n "${PARAM_CERTDIR:-}" ]] && CERTDIR="${PARAM_CERTDIR}"
  [[ -n "${PARAM_ALPNCERTDIR:-}" ]] && ALPNCERTDIR="${PARAM_ALPNCERTDIR}"
  [[ -n "${PARAM_CHALLENGETYPE:-}" ]] && CHALLENGETYPE="${PARAM_CHALLENGETYPE}"
  [[ -n "${PARAM_KEY_ALGO:-}" ]] && KEY_ALGO="${PARAM_KEY_ALGO}"
  [[ -n "${PARAM_OCSP_MUST_STAPLE:-}" ]] && OCSP_MUST_STAPLE="${PARAM_OCSP_MUST_STAPLE}"
  [[ -n "${PARAM_IP_VERSION:-}" ]] && IP_VERSION="${PARAM_IP_VERSION}"

  if [ "${PARAM_FORCE_VALIDATION:-no}" = "yes" ] && [ "${PARAM_FORCE:-no}" = "no" ]; then
    _exiterr "Argument --force-validation can only be used in combination with --force (-x)"
  fi

  if [ ! "${1:-}" = "noverify" ]; then
    verify_config
  fi
  store_configvars
}

# Initialize system
init_system() {
  load_config

  # Lockfile handling (prevents concurrent access)
  if [[ -n "${LOCKFILE}" ]]; then
    LOCKDIR="$(dirname "${LOCKFILE}")"
    [[ -w "${LOCKDIR}" ]] || _exiterr "Directory ${LOCKDIR} for LOCKFILE ${LOCKFILE} is not writable, aborting."
    ( set -C; date > "${LOCKFILE}" ) 2>/dev/null || _exiterr "Lock file '${LOCKFILE}' present, aborting."
    remove_lock() { rm -f "${LOCKFILE}"; }
    trap 'remove_lock' EXIT
  fi

  # Get CA URLs
  CA_DIRECTORY="$(http_request get "${CA}" | jsonsh)"

  # Automatic discovery of API version
  if [[ "${API}" = "auto" ]]; then
    grep -q newOrder <<< "${CA_DIRECTORY}" && API=2 || API=1
  fi

  if [[ ${API} -eq 1 ]]; then
    # shellcheck disable=SC2015
    CA_NEW_CERT="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value new-cert)" &&
    CA_NEW_AUTHZ="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value new-authz)" &&
    CA_NEW_REG="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value new-reg)" &&
    CA_TERMS="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value terms-of-service)" &&
    CA_REQUIRES_EAB="false" &&
    CA_REVOKE_CERT="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value revoke-cert)" ||
    _exiterr "Problem retrieving ACME/CA-URLs, check if your configured CA points to the directory entrypoint."
    # Since reg URI is missing from directory we will assume it is the same as CA_NEW_REG without the new part
    CA_REG=${CA_NEW_REG/new-reg/reg}
  else
    # shellcheck disable=SC2015
    CA_NEW_ORDER="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value newOrder)" &&
    CA_NEW_NONCE="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value newNonce)" &&
    CA_NEW_ACCOUNT="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value newAccount)" &&
    CA_TERMS="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value -p '"meta","termsOfService"')" &&
    CA_REQUIRES_EAB="$(printf "%s" "${CA_DIRECTORY}" | get_json_bool_value -p '"meta","externalAccountRequired"' || echo false)" &&
    CA_REVOKE_CERT="$(printf "%s" "${CA_DIRECTORY}" | get_json_string_value revokeCert)" ||
    _exiterr "Problem retrieving ACME/CA-URLs, check if your configured CA points to the directory entrypoint."
    # Since acct URI is missing from directory we will assume it is the same as CA_NEW_ACCOUNT without the new part
    CA_ACCOUNT=${CA_NEW_ACCOUNT/new-acct/acct}
  fi

  # Export some environment variables to be used in hook script
  export WELLKNOWN BASEDIR CERTDIR ALPNCERTDIR CONFIG COMMAND

  # Checking for private key ...
  register_new_key="no"
  generated="false"
  if [[ -n "${PARAM_ACCOUNT_KEY:-}" ]]; then
    # a private key was specified from the command line so use it for this run
    echo "Using private key ${PARAM_ACCOUNT_KEY} instead of account key"
    ACCOUNT_KEY="${PARAM_ACCOUNT_KEY}"
    ACCOUNT_KEY_JSON="${PARAM_ACCOUNT_KEY}.json"
    ACCOUNT_ID_JSON="${PARAM_ACCOUNT_KEY}_id.json"
    [ "${COMMAND:-}" = "register" ] && register_new_key="yes"
  else
    # Check if private account key exists, if it doesn't exist yet generate a new one (rsa key)
    if [[ ! -e "${ACCOUNT_KEY}" ]]; then
      if [[ ! "${PARAM_ACCEPT_TERMS:-}" = "yes" ]]; then
        printf '\n' >&2
        printf 'To use dehydrated with this certificate authority you have to agree to their terms of service which you can find here: %s\n\n' "${CA_TERMS}" >&2
        printf 'To accept these terms of service run `%s --register --accept-terms`.\n' "${0}" >&2
        exit 1
      fi

      echo "+ Generating account key..."
      generated="true"
      local tmp_account_key="$(_mktemp)"
      _openssl genrsa -out "${tmp_account_key}" "${KEYSIZE}"
      cat "${tmp_account_key}" > "${ACCOUNT_KEY}"
      rm "${tmp_account_key}"
      register_new_key="yes"
    fi
  fi
  "${OPENSSL}" rsa -in "${ACCOUNT_KEY}" -check 2>/dev/null > /dev/null || _exiterr "Account key is not valid, cannot continue."

  # Get public components from private key and calculate thumbprint
  pubExponent64="$(printf '%x' "$("${OPENSSL}" rsa -in "${ACCOUNT_KEY}" -noout -text | awk '/publicExponent/ {print $2}')" | hex2bin | urlbase64)"
  pubMod64="$("${OPENSSL}" rsa -in "${ACCOUNT_KEY}" -noout -modulus | cut -d'=' -f2 | hex2bin | urlbase64)"

  thumbprint="$(printf '{"e":"%s","kty":"RSA","n":"%s"}' "${pubExponent64}" "${pubMod64}" | "${OPENSSL}" dgst -sha256 -binary | urlbase64)"

  # If we generated a new private key in the step above we have to register it with the acme-server
  if [[ "${register_new_key}" = "yes" ]]; then
    echo "+ Registering account key with ACME server..."
    FAILED=false

    if [[ ${API} -eq 1 && -z "${CA_NEW_REG}" ]] || [[ ${API} -eq 2 && -z "${CA_NEW_ACCOUNT}" ]]; then
      echo "Certificate authority doesn't allow registrations."
      FAILED=true
    fi

    # ZeroSSL special sauce
    if [[ "${CA}" = "${CA_ZEROSSL}" ]]; then
      if [[ -z "${EAB_KID:-}" ]] ||  [[ -z "${EAB_HMAC_KEY:-}" ]]; then
        if [[ -z "${CONTACT_EMAIL}" ]]; then
          echo "ZeroSSL requires contact email to be set or EAB_KID/EAB_HMAC_KEY to be manually configured"
          FAILED=true
        else
          zeroapi="$(curl -s "https://api.zerossl.com/acme/eab-credentials-email" -d "email=${CONTACT_EMAIL}" | jsonsh)"
          EAB_KID="$(printf "%s" "${zeroapi}" | get_json_string_value eab_kid)"
          EAB_HMAC_KEY="$(printf "%s" "${zeroapi}" | get_json_string_value eab_hmac_key)"
          if [[ -z "${EAB_KID:-}" ]] ||  [[ -z "${EAB_HMAC_KEY:-}" ]]; then
            echo "Unknown error retrieving ZeroSSL API credentials"
            echo "${zeroapi}"
            FAILED=true
          fi
        fi
      fi
    fi

    # Check if external account is required
    if [[ "${FAILED}" = "false" ]]; then
      if [[ "${CA_REQUIRES_EAB}" = "true" ]]; then
        if [[ -z "${EAB_KID:-}" ]] || [[ -z "${EAB_HMAC_KEY:-}" ]]; then
          FAILED=true
          echo "This CA requires an external account but no EAB_KID/EAB_HMAC_KEY has been configured"
        fi
      fi
    fi

    # If an email for the contact has been provided then adding it to the registration request
    if [[ "${FAILED}" = "false" ]]; then
      if [[ ${API} -eq 1 ]]; then
        if [[ -n "${CONTACT_EMAIL}" ]]; then
          (signed_request "${CA_NEW_REG}" '{"resource": "new-reg", "contact":["mailto:'"${CONTACT_EMAIL}"'"], "agreement": "'"${CA_TERMS}"'"}' > "${ACCOUNT_KEY_JSON}") || FAILED=true
        else
          (signed_request "${CA_NEW_REG}" '{"resource": "new-reg", "agreement": "'"${CA_TERMS}"'"}' > "${ACCOUNT_KEY_JSON}") || FAILED=true
        fi
      else
        if [[ -n "${EAB_KID:-}" ]] && [[ -n "${EAB_HMAC_KEY:-}" ]]; then
          eab_url="${CA_NEW_ACCOUNT}"
          eab_protected64="$(printf '{"alg":"HS256","kid":"%s","url":"%s"}' "${EAB_KID}" "${eab_url}" | urlbase64)"
          eab_payload64="$(printf "%s" '{"e": "'"${pubExponent64}"'", "kty": "RSA", "n": "'"${pubMod64}"'"}' | urlbase64)"
          eab_key="$(printf "%s" "${EAB_HMAC_KEY}" | deurlbase64 | bin2hex)"
          eab_signed64="$(printf '%s' "${eab_protected64}.${eab_payload64}" | "${OPENSSL}" dgst -binary -sha256 -mac HMAC -macopt "hexkey:${eab_key}" | urlbase64)"

          if [[ -n "${CONTACT_EMAIL}" ]]; then
            regjson='{"contact":["mailto:'"${CONTACT_EMAIL}"'"], "termsOfServiceAgreed": true, "externalAccountBinding": {"protected": "'"${eab_protected64}"'", "payload": "'"${eab_payload64}"'", "signature": "'"${eab_signed64}"'"}}'
          else
            regjson='{"termsOfServiceAgreed": true, "externalAccountBinding": {"protected": "'"${eab_protected64}"'", "payload": "'"${eab_payload64}"'", "signature": "'"${eab_signed64}"'"}}'
          fi
        else
          if [[ -n "${CONTACT_EMAIL}" ]]; then
            regjson='{"contact":["mailto:'"${CONTACT_EMAIL}"'"], "termsOfServiceAgreed": true}'
          else
            regjson='{"termsOfServiceAgreed": true}'
          fi
        fi
        (signed_request "${CA_NEW_ACCOUNT}" "${regjson}" > "${ACCOUNT_KEY_JSON}") || FAILED=true
      fi
    fi

    if [[ "${FAILED}" = "true" ]]; then
      echo >&2
      echo >&2
      echo "Error registering account key. See message above for more information." >&2
      if [[ "${generated}" = "true" ]]; then
        rm "${ACCOUNT_KEY}"
      fi
      rm -f "${ACCOUNT_KEY_JSON}"
      exit 1
    fi
  elif [[ "${COMMAND:-}" = "register" ]]; then
    echo "+ Account already registered!"
    exit 0
  fi

  # Read account information or request from CA if missing
  if [[ -e "${ACCOUNT_KEY_JSON}" ]]; then
    if [[ ${API} -eq 1 ]]; then
      ACCOUNT_ID="$(cat "${ACCOUNT_KEY_JSON}" | jsonsh | get_json_int_value id)"
      ACCOUNT_URL="${CA_REG}/${ACCOUNT_ID}"
    else
      if [[ -e "${ACCOUNT_ID_JSON}" ]]; then
        ACCOUNT_URL="$(cat "${ACCOUNT_ID_JSON}" | jsonsh | get_json_string_value url)"
      fi
      # if account URL is not storred, fetch it from the CA
      if [[ -z "${ACCOUNT_URL:-}" ]]; then
        echo "+ Fetching account URL..."
        ACCOUNT_URL="$(signed_request "${CA_NEW_ACCOUNT}" '{"onlyReturnExisting": true}' 4>&1 | grep -i ^Location: | cut -d':' -f2- | tr -d ' \t\r\n')"
        if [[ -z "${ACCOUNT_URL}" ]]; then
          _exiterr "Unknown error on fetching account information"
        fi
        echo '{"url":"'"${ACCOUNT_URL}"'"}' > "${ACCOUNT_ID_JSON}" # store the URL for next time
      fi
    fi
  else
    echo "Fetching missing account information from CA..."
    if [[ ${API} -eq 1 ]]; then
      _exiterr "This is not implemented for ACMEv1! Consider switching to ACMEv2 :)"
    else
      ACCOUNT_URL="$(signed_request "${CA_NEW_ACCOUNT}" '{"onlyReturnExisting": true}' 4>&1 | grep -i ^Location: | cut -d':' -f2- | tr -d ' \t\r\n')"
      ACCOUNT_INFO="$(signed_request "${ACCOUNT_URL}" '{}')"
    fi
    echo "${ACCOUNT_INFO}" > "${ACCOUNT_KEY_JSON}"
  fi
}

# Different sed version for different os types...
_sed() {
  if [[ "${OSTYPE}" = "Linux" || "${OSTYPE:0:5}" = "MINGW" ]]; then
    sed -r "${@}"
  else
    sed -E "${@}"
  fi
}

# Print error message and exit with error
_exiterr() {
  if [ -n "${1:-}" ]; then
    echo "ERROR: ${1}" >&2
  fi
  [[ "${skip_exit_hook:-no}" = "no" ]] && [[ -n "${HOOK:-}" ]] && ("${HOOK}" "exit_hook" "${1:-}" || echo 'exit_hook returned with non-zero exit code!' >&2)
  exit 1
}

# Remove newlines and whitespace from json
clean_json() {
  tr -d '\r\n' | _sed -e 's/ +/ /g' -e 's/\{ /{/g' -e 's/ \}/}/g' -e 's/\[ /[/g' -e 's/ \]/]/g'
}

# Encode data as url-safe formatted base64
urlbase64() {
  # urlbase64: base64 encoded string with '+' replaced with '-' and '/' replaced with '_'
  "${OPENSSL}" base64 -e | tr -d '\n\r' | _sed -e 's:=*$::g' -e 'y:+/:-_:'
}

# Decode data from url-safe formatted base64
deurlbase64() {
  data="$(cat | tr -d ' \n\r')"
  modlen=$((${#data} % 4))
  padding=""
  if [[ "${modlen}" = "2" ]]; then padding="==";
  elif [[ "${modlen}" = "3" ]]; then padding="="; fi
  printf "%s%s" "${data}" "${padding}" | tr -d '\n\r' | _sed -e 'y:-_:+/:' | "${OPENSSL}" base64 -d -A
}

# Convert hex string to binary data
hex2bin() {
  # Remove spaces, add leading zero, escape as hex string and parse with printf
  printf -- "$(cat | _sed -e 's/[[:space:]]//g' -e 's/^(.(.{2})*)$/0\1/' -e 's/(.{2})/\\x\1/g')"
}

# Convert binary data to hex string
bin2hex() {
  hexdump -e '16/1 "%02x"'
}

# OpenSSL writes to stderr/stdout even when there are no errors. So just
# display the output if the exit code was != 0 to simplify debugging.
_openssl() {
  set +e
  out="$("${OPENSSL}" "${@}" 2>&1)"
  res=$?
  set -e
  if [[ ${res} -ne 0 ]]; then
    echo "  + ERROR: failed to run $* (Exitcode: ${res})" >&2
    echo >&2
    echo "Details:" >&2
    echo "${out}" >&2
    echo >&2
    exit "${res}"
  fi
}

# Send http(s) request with specified method
http_request() {
  tempcont="$(_mktemp)"
  tempheaders="$(_mktemp)"

  if [[ -n "${IP_VERSION:-}" ]]; then
      ip_version="-${IP_VERSION}"
  fi

  set +e
  if [[ "${1}" = "head" ]]; then
    statuscode="$(curl ${ip_version:-} ${CURL_OPTS} -A "dehydrated/${VERSION} curl/${CURL_VERSION}" -s -w "%{http_code}" -o "${tempcont}" "${2}" -I)"
    curlret="${?}"
    touch "${tempheaders}"
  elif [[ "${1}" = "get" ]]; then
    statuscode="$(curl ${ip_version:-} ${CURL_OPTS} -A "dehydrated/${VERSION} curl/${CURL_VERSION}" -L -s -w "%{http_code}" -o "${tempcont}" -D "${tempheaders}" "${2}")"
    curlret="${?}"
  elif [[ "${1}" = "post" ]]; then
    statuscode="$(curl ${ip_version:-} ${CURL_OPTS} -A "dehydrated/${VERSION} curl/${CURL_VERSION}" -s -w "%{http_code}" -o "${tempcont}" "${2}" -D "${tempheaders}" -H 'Content-Type: application/jose+json' -d "${3}")"
    curlret="${?}"
  else
    set -e
    _exiterr "Unknown request method: ${1}"
  fi
  set -e

  if [[ ! "${curlret}" = "0" ]]; then
    _exiterr "Problem connecting to server (${1} for ${2}; curl returned with ${curlret})"
  fi

  if [[ ! "${statuscode:0:1}" = "2" ]]; then
    # check for existing registration warning
    if [[ "${API}" = "1" ]] && [[ -n "${CA_NEW_REG:-}" ]] && [[ "${2}" = "${CA_NEW_REG:-}" ]] && [[ "${statuscode}" = "409" ]] && grep -q "Registration key is already in use" "${tempcont}"; then
      # do nothing
      :
    # check for already-revoked warning
    elif [[ -n "${CA_REVOKE_CERT:-}" ]] && [[ "${2}" = "${CA_REVOKE_CERT:-}" ]] && [[ "${statuscode}" = "409" ]]; then
      grep -q "Certificate already revoked" "${tempcont}" && return
    else
      echo "  + ERROR: An error occurred while sending ${1}-request to ${2} (Status ${statuscode})" >&2
      echo >&2
      echo "Details:" >&2
      cat "${tempheaders}" >&2
      cat "${tempcont}" >&2
      echo >&2
      echo >&2

      # An exclusive hook for the {1}-request error might be useful (e.g., for sending an e-mail to admins)
      if [[ -n "${HOOK}" ]]; then
        errtxt="$(cat ${tempcont})"
        errheaders="$(cat ${tempheaders})"
        "${HOOK}" "request_failure" "${statuscode}" "${errtxt}" "${1}" "${errheaders}" || _exiterr 'request_failure hook returned with non-zero exit code'
      fi

      rm -f "${tempcont}"
      rm -f "${tempheaders}"

      # remove temporary domains.txt file if used
      [[ "${COMMAND:-}" = "sign_domains" && -n "${PARAM_DOMAIN:-}" && -n "${DOMAINS_TXT:-}" ]] && rm "${DOMAINS_TXT}"
      _exiterr
    fi
  fi

  if { true >&4; } 2>/dev/null; then
    cat "${tempheaders}" >&4
  fi
  cat "${tempcont}"
  rm -f "${tempcont}"
  rm -f "${tempheaders}"
}

# Send signed request
signed_request() {
  # Encode payload as urlbase64
  payload64="$(printf '%s' "${2}" | urlbase64)"

  # Retrieve nonce from acme-server
  if [[ ${API} -eq 1 ]]; then
    nonce="$(http_request head "${CA}" | grep -i ^Replay-Nonce: | cut -d':' -f2- | tr -d ' \t\n\r')"
  else
    nonce="$(http_request head "${CA_NEW_NONCE}" | grep -i ^Replay-Nonce: | cut -d':' -f2- | tr -d ' \t\n\r')"
  fi

  # Build header with just our public key and algorithm information
  header='{"alg": "RS256", "jwk": {"e": "'"${pubExponent64}"'", "kty": "RSA", "n": "'"${pubMod64}"'"}}'

  if [[ ${API} -eq 1 ]]; then
    # Build another header which also contains the previously received nonce and encode it as urlbase64
    protected='{"alg": "RS256", "jwk": {"e": "'"${pubExponent64}"'", "kty": "RSA", "n": "'"${pubMod64}"'"}, "nonce": "'"${nonce}"'"}'
    protected64="$(printf '%s' "${protected}" | urlbase64)"
  else
    # Build another header which also contains the previously received nonce and url and encode it as urlbase64
    if [[ -n "${ACCOUNT_URL:-}" ]]; then
      protected='{"alg": "RS256", "kid": "'"${ACCOUNT_URL}"'", "url": "'"${1}"'", "nonce": "'"${nonce}"'"}'
    else
      protected='{"alg": "RS256", "jwk": {"e": "'"${pubExponent64}"'", "kty": "RSA", "n": "'"${pubMod64}"'"}, "url": "'"${1}"'", "nonce": "'"${nonce}"'"}'
    fi
    protected64="$(printf '%s' "${protected}" | urlbase64)"
  fi

  # Sign header with nonce and our payload with our private key and encode signature as urlbase64
  signed64="$(printf '%s' "${protected64}.${payload64}" | "${OPENSSL}" dgst -sha256 -sign "${ACCOUNT_KEY}" | urlbase64)"

  if [[ ${API} -eq 1 ]]; then
    # Send header + extended header + payload + signature to the acme-server
    data='{"header": '"${header}"', "protected": "'"${protected64}"'", "payload": "'"${payload64}"'", "signature": "'"${signed64}"'"}'
  else
    # Send extended header + payload + signature to the acme-server
    data='{"protected": "'"${protected64}"'", "payload": "'"${payload64}"'", "signature": "'"${signed64}"'"}'
  fi

  http_request post "${1}" "${data}"
}

# Extracts all subject names from a CSR
# Outputs either the CN, or the SANs, one per line
extract_altnames() {
  csr="${1}" # the CSR itself (not a file)

  if ! <<<"${csr}" "${OPENSSL}" req -verify -noout 2>/dev/null; then
    _exiterr "Certificate signing request isn't valid"
  fi

  reqtext="$( <<<"${csr}" "${OPENSSL}" req -noout -text )"
  if <<<"${reqtext}" grep -q '^[[:space:]]*X509v3 Subject Alternative Name:[[:space:]]*$'; then
    # SANs used, extract these
    altnames="$( <<<"${reqtext}" awk '/X509v3 Subject Alternative Name:/{print;getline;print;}' | tail -n1 )"
    # split to one per line:
    # shellcheck disable=SC1003
    altnames="$( <<<"${altnames}" _sed -e 's/^[[:space:]]*//; s/, /\'$'\n''/g' )"
    # we can only get DNS: ones signed
    if grep -qEv '^(DNS|othername):' <<<"${altnames}"; then
      _exiterr "Certificate signing request contains non-DNS Subject Alternative Names"
    fi
    # strip away the DNS: prefix
    altnames="$( <<<"${altnames}" _sed -e 's/^(DNS:|othername:<unsupported>)//' )"
    printf "%s" "${altnames}" | tr '\n' ' '
  else
    # No SANs, extract CN
    altnames="$( <<<"${reqtext}" grep '^[[:space:]]*Subject:' | _sed -e 's/.*[ /]CN ?= ?([^ /,]*).*/\1/' )"
    printf "%s" "${altnames}"
  fi
}

# Get last issuer CN in certificate chain
get_last_cn() {
  <<<"${1}" _sed 'H;/-----BEGIN CERTIFICATE-----/h;$!d;x' | "${OPENSSL}" x509 -noout -issuer | head -n1 | _sed -e 's/.*[ /]CN ?= ?([^/,]*).*/\1/'
}

# Create certificate for domain(s) and outputs it FD 3
sign_csr() {
  csr="${1}" # the CSR itself (not a file)

  if { true >&3; } 2>/dev/null; then
    : # fd 3 looks OK
  else
    _exiterr "sign_csr: FD 3 not open"
  fi

  shift 1 || true
  export altnames="${*}"

  if [[ ${API} -eq 1 ]]; then
    if [[ -z "${CA_NEW_AUTHZ}" ]] || [[ -z "${CA_NEW_CERT}" ]]; then
      _exiterr "Certificate authority doesn't allow certificate signing"
    fi
  elif [[ ${API} -eq 2 ]] && [[ -z "${CA_NEW_ORDER}" ]]; then
    _exiterr "Certificate authority doesn't allow certificate signing"
  fi

  if [[ -n "${ZSH_VERSION:-}" ]]; then
    local -A challenge_names challenge_uris challenge_tokens authorizations keyauths deploy_args
  else
    local -a challenge_names challenge_uris challenge_tokens authorizations keyauths deploy_args
  fi

  # Initial step: Find which authorizations we're dealing with
  if [[ ${API} -eq 2 ]]; then
    # Request new order and store authorization URIs
    local challenge_identifiers=""
    for altname in ${altnames}; do
      challenge_identifiers+="$(printf '{"type": "dns", "value": "%s"}, ' "${altname}")"
    done
    challenge_identifiers="[${challenge_identifiers%, }]"

    echo " + Requesting new certificate order from CA..."
    order_location="$(signed_request "${CA_NEW_ORDER}" '{"identifiers": '"${challenge_identifiers}"'}' 4>&1 | grep -i ^Location: | cut -d':' -f2- | tr -d ' \t\r\n')"
    result="$(signed_request "${order_location}" "" | jsonsh)"

    order_authorizations="$(echo "${result}" | get_json_array_values authorizations)"
    finalize="$(echo "${result}" | get_json_string_value finalize)"

    local idx=0
    for uri in ${order_authorizations}; do
      authorizations[${idx}]="${uri}"
      idx=$((idx+1))
    done
    echo " + Received ${idx} authorizations URLs from the CA"
  else
    # Copy $altnames to $authorizations (just doing this to reduce duplicate code later on)
    local idx=0
    for altname in ${altnames}; do
      authorizations[${idx}]="${altname}"
      idx=$((idx+1))
    done
  fi

  # Check if authorizations are valid and gather challenge information for pending authorizations
  local idx=0
  for authorization in ${authorizations[*]}; do
    if [[ "${API}" -eq 2 ]]; then
      # Receive authorization ($authorization is authz uri)
      response="$(signed_request "$(echo "${authorization}" | _sed -e 's/\"(.*)".*/\1/')" "" | jsonsh)"
      identifier="$(echo "${response}" | get_json_string_value -p '"identifier","value"')"
      echo " + Handling authorization for ${identifier}"
    else
      # Request new authorization ($authorization is altname)
      identifier="${authorization}"
      echo " + Requesting authorization for ${identifier}..."
      response="$(signed_request "${CA_NEW_AUTHZ}" '{"resource": "new-authz", "identifier": {"type": "dns", "value": "'"${identifier}"'"}}' | jsonsh)"
    fi

    # Check if authorization has already been validated
    if [ "$(echo "${response}" | get_json_string_value status)" = "valid" ]; then
      if [ "${PARAM_FORCE_VALIDATION:-no}" = "yes" ]; then
        echo " + A valid authorization has been found but will be ignored"
      else
        echo " + Found valid authorization for ${identifier}"
        continue
      fi
    fi

    # Find challenge in authorization
    challengeindex="$(echo "${response}" | grep -E '^\["challenges",[0-9]+,"type"\][[:space:]]+"'"${CHALLENGETYPE}"'"' | cut -d',' -f2 || true)"

    if [ -z "${challengeindex}" ]; then
      allowed_validations="$(echo "${response}" | grep -E '^\["challenges",[0-9]+,"type"\]' | sed -e 's/\[[^\]*\][[:space:]]*//g' -e 's/^"//' -e 's/"$//' | tr '\n' ' ')"
      _exiterr "Validating this certificate is not possible using ${CHALLENGETYPE}. Possible validation methods are: ${allowed_validations}"
    fi
    challenge="$(echo "${response}" | get_json_dict_value -p '"challenges",'"${challengeindex}")"

    # Gather challenge information
    challenge_names[${idx}]="${identifier}"
    challenge_tokens[${idx}]="$(echo "${challenge}" | get_json_string_value token)"

    if [[ ${API} -eq 2 ]]; then
      challenge_uris[${idx}]="$(echo "${challenge}" | get_json_string_value url)"
    else
      if [[ "$(echo "${challenge}" | get_json_string_value type)" = "urn:acme:error:unauthorized" ]]; then
        _exiterr "Challenge unauthorized: $(echo "${challenge}" | get_json_string_value detail)"
      fi
      challenge_uris[${idx}]="$(echo "${challenge}" | get_json_dict_value validationRecord | get_json_string_value uri)"
    fi

    # Prepare challenge tokens and deployment parameters
    keyauth="${challenge_tokens[${idx}]}.${thumbprint}"

    case "${CHALLENGETYPE}" in
      "http-01")
        # Store challenge response in well-known location and make world-readable (so that a webserver can access it)
        printf '%s' "${keyauth}" > "${WELLKNOWN}/${challenge_tokens[${idx}]}"
        chmod a+r "${WELLKNOWN}/${challenge_tokens[${idx}]}"
        keyauth_hook="${keyauth}"
        ;;
      "dns-01")
        # Generate DNS entry content for dns-01 validation
        keyauth_hook="$(printf '%s' "${keyauth}" | "${OPENSSL}" dgst -sha256 -binary | urlbase64)"
        ;;
      "tls-alpn-01")
        keyauth_hook="$(printf '%s' "${keyauth}" | "${OPENSSL}" dgst -sha256 -c -hex | awk '{print $NF}')"
        generate_alpn_certificate "${identifier}" "${keyauth_hook}"
        ;;
    esac

    keyauths[${idx}]="${keyauth}"
    deploy_args[${idx}]="${identifier} ${challenge_tokens[${idx}]} ${keyauth_hook}"

    idx=$((idx+1))
  done
  local num_pending_challenges=${idx}
  echo " + ${num_pending_challenges} pending challenge(s)"

  # Deploy challenge tokens
  if [[ ${num_pending_challenges} -ne 0 ]]; then
    echo " + Deploying challenge tokens..."
    if [[ -n "${HOOK}" ]] && [[ "${HOOK_CHAIN}" = "yes" ]]; then
      "${HOOK}" "deploy_challenge" ${deploy_args[@]} || _exiterr 'deploy_challenge hook returned with non-zero exit code'
    elif [[ -n "${HOOK}" ]]; then
      # Run hook script to deploy the challenge token
      local idx=0
      while [ ${idx} -lt ${num_pending_challenges} ]; do
        "${HOOK}" "deploy_challenge" ${deploy_args[${idx}]} || _exiterr 'deploy_challenge hook returned with non-zero exit code'
        idx=$((idx+1))
      done
    fi
  fi

  # Validate pending challenges
  local idx=0
  while [ ${idx} -lt ${num_pending_challenges} ]; do
    echo " + Responding to challenge for ${challenge_names[${idx}]} authorization..."

    # Ask the acme-server to verify our challenge and wait until it is no longer pending
    if [[ ${API} -eq 1 ]]; then
      result="$(signed_request "${challenge_uris[${idx}]}" '{"resource": "challenge", "keyAuthorization": "'"${keyauths[${idx}]}"'"}' | jsonsh)"
    else
      result="$(signed_request "${challenge_uris[${idx}]}" '{}' | jsonsh)"
    fi

    reqstatus="$(echo "${result}" | get_json_string_value status)"

    while [[ "${reqstatus}" = "pending" ]] || [[ "${reqstatus}" = "processing" ]]; do
      sleep 1
      if [[ "${API}" -eq 2 ]]; then
        result="$(signed_request "${challenge_uris[${idx}]}" "" | jsonsh)"
      else
        result="$(http_request get "${challenge_uris[${idx}]}" | jsonsh)"
      fi
      reqstatus="$(echo "${result}" | get_json_string_value status)"
    done

    [[ "${CHALLENGETYPE}" = "http-01" ]] && rm -f "${WELLKNOWN}/${challenge_tokens[${idx}]}"
    [[ "${CHALLENGETYPE}" = "tls-alpn-01" ]] && rm -f "${ALPNCERTDIR}/${challenge_names[${idx}]}.crt.pem" "${ALPNCERTDIR}/${challenge_names[${idx}]}.key.pem"

    if [[ "${reqstatus}" = "valid" ]]; then
      echo " + Challenge is valid!"
    else
      [[ -n "${HOOK}" ]] && ("${HOOK}" "invalid_challenge" "${altname}" "${result}" || _exiterr 'invalid_challenge hook returned with non-zero exit code')
      break
    fi
    idx=$((idx+1))
  done

  if [[ ${num_pending_challenges} -ne 0 ]]; then
    echo " + Cleaning challenge tokens..."

    # Clean challenge tokens using chained hook
    [[ -n "${HOOK}" ]] && [[ "${HOOK_CHAIN}" = "yes" ]] && ("${HOOK}" "clean_challenge" ${deploy_args[@]} || _exiterr 'clean_challenge hook returned with non-zero exit code')

    # Clean remaining challenge tokens if validation has failed
    local idx=0
    while [ ${idx} -lt ${num_pending_challenges} ]; do
      # Delete challenge file
      [[ "${CHALLENGETYPE}" = "http-01" ]] && rm -f "${WELLKNOWN}/${challenge_tokens[${idx}]}"
      # Delete alpn verification certificates
      [[ "${CHALLENGETYPE}" = "tls-alpn-01" ]] && rm -f "${ALPNCERTDIR}/${challenge_names[${idx}]}.crt.pem" "${ALPNCERTDIR}/${challenge_names[${idx}]}.key.pem"
      # Clean challenge token using non-chained hook
      [[ -n "${HOOK}" ]] && [[ "${HOOK_CHAIN}" != "yes" ]] && ("${HOOK}" "clean_challenge" ${deploy_args[${idx}]} || _exiterr 'clean_challenge hook returned with non-zero exit code')
      idx=$((idx+1))
    done

    if [[ "${reqstatus}" != "valid" ]]; then
      echo " + Challenge validation has failed :("
      _exiterr "Challenge is invalid! (returned: ${reqstatus}) (result: ${result})"
    fi
  fi

  # Finally request certificate from the acme-server and store it in cert-${timestamp}.pem and link from cert.pem
  echo " + Requesting certificate..."
  csr64="$( <<<"${csr}" "${OPENSSL}" req -config "${OPENSSL_CNF}" -outform DER | urlbase64)"
  if [[ ${API} -eq 1 ]]; then
    crt64="$(signed_request "${CA_NEW_CERT}" '{"resource": "new-cert", "csr": "'"${csr64}"'"}' | "${OPENSSL}" base64 -e)"
    crt="$( printf -- '-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n' "${crt64}" )"
  else
    result="$(signed_request "${finalize}" '{"csr": "'"${csr64}"'"}' | jsonsh)"
    while :; do
      orderstatus="$(echo "${result}" | get_json_string_value status)"
      case "${orderstatus}"
      in
        "processing" | "pending")
          echo " + Order is ${orderstatus}..."
          sleep 2;
          ;;
        "valid")
          break;
          ;;
        *)
          _exiterr "Order in status ${orderstatus}"
          ;;
      esac
      result="$(signed_request "${order_location}" "" | jsonsh)"
    done

    resheaders="$(_mktemp)"
    certificate="$(echo "${result}" | get_json_string_value certificate)"
    crt="$(signed_request "${certificate}" "" 4>"${resheaders}")"

    if [ -n "${PREFERRED_CHAIN:-}" ]; then
      foundaltchain=0
      altcn="$(get_last_cn "${crt}")"
      altoptions="${altcn}"
      if [ "${altcn}" = "${PREFERRED_CHAIN}" ]; then
        foundaltchain=1
      fi
      if [ "${foundaltchain}" = "0" ]; then
        while read altcrturl; do
          if [ "${foundaltchain}" = "0" ]; then
            altcrt="$(signed_request "${altcrturl}" "")"
            altcn="$(get_last_cn "${altcrt}")"
            altoptions="${altoptions}, ${altcn}"
            if [ "${altcn}" = "${PREFERRED_CHAIN}" ]; then
              foundaltchain=1
              crt="${altcrt}"
            fi
          fi
        done <<< "$(grep -Ei '^link:' "${resheaders}" | grep -Ei 'rel="alternate"' | cut -d'<' -f2 | cut -d'>' -f1)"
      fi
      if [ "${foundaltchain}" = "0" ]; then
        _exiterr "Alternative chain with CN = ${PREFERRED_CHAIN} not found, available options: ${altoptions}"
      fi
      echo " + Using preferred chain with CN = ${altcn}"
    fi
    rm -f "${resheaders}"
  fi

  # Try to load the certificate to detect corruption
  echo " + Checking certificate..."
  _openssl x509 -text <<<"${crt}"

  echo "${crt}" >&3

  unset challenge_token
  echo " + Done!"
}

# grep issuer cert uri from certificate
get_issuer_cert_uri() {
  certificate="${1}"
  "${OPENSSL}" x509 -in "${certificate}" -noout -text | (grep 'CA Issuers - URI:' | cut -d':' -f2-) || true
}

get_issuer_hash() {
  certificate="${1}"
  "${OPENSSL}" x509 -in "${certificate}" -noout -issuer_hash
}

get_ocsp_url() {
  certificate="${1}"
  "${OPENSSL}" x509 -in "${certificate}" -noout -ocsp_uri
}

# walk certificate chain, retrieving all intermediate certificates
walk_chain() {
  local certificate
  certificate="${1}"

  local issuer_cert_uri
  issuer_cert_uri="${2:-}"
  if [[ -z "${issuer_cert_uri}" ]]; then issuer_cert_uri="$(get_issuer_cert_uri "${certificate}")"; fi
  if [[ -n "${issuer_cert_uri}" ]]; then
    # create temporary files
    local tmpcert
    local tmpcert_raw
    tmpcert_raw="$(_mktemp)"
    tmpcert="$(_mktemp)"

    # download certificate
    http_request get "${issuer_cert_uri}" > "${tmpcert_raw}"

    # PEM
    if grep -q "BEGIN CERTIFICATE" "${tmpcert_raw}"; then mv "${tmpcert_raw}" "${tmpcert}"
    # DER
    elif "${OPENSSL}" x509 -in "${tmpcert_raw}" -inform DER -out "${tmpcert}" -outform PEM 2> /dev/null > /dev/null; then :
    # PKCS7
    elif "${OPENSSL}" pkcs7 -in "${tmpcert_raw}" -inform DER -out "${tmpcert}" -outform PEM -print_certs 2> /dev/null > /dev/null; then :
    # Unknown certificate type
    else _exiterr "Unknown certificate type in chain"
    fi

    local next_issuer_cert_uri
    next_issuer_cert_uri="$(get_issuer_cert_uri "${tmpcert}")"
    if [[ -n "${next_issuer_cert_uri}" ]]; then
      printf "\n%s\n" "${issuer_cert_uri}"
      cat "${tmpcert}"
      walk_chain "${tmpcert}" "${next_issuer_cert_uri}"
    fi
    rm -f "${tmpcert}" "${tmpcert_raw}"
  fi
}

# Generate ALPN verification certificate
generate_alpn_certificate() {
  local altname="${1}"
  local acmevalidation="${2}"

  local alpncertdir="${ALPNCERTDIR}"
  if [[ ! -e "${alpncertdir}" ]]; then
    echo " + Creating new directory ${alpncertdir} ..."
    mkdir -p "${alpncertdir}" || _exiterr "Unable to create directory ${alpncertdir}"
  fi

  echo " + Generating ALPN certificate and key for ${1}..."
  tmp_openssl_cnf="$(_mktemp)"
  cat "${OPENSSL_CNF}" > "${tmp_openssl_cnf}"
  printf "\n[SAN]\nsubjectAltName=DNS:%s\n" "${altname}" >> "${tmp_openssl_cnf}"
  printf "1.3.6.1.5.5.7.1.31=critical,DER:04:20:${acmevalidation}\n" >> "${tmp_openssl_cnf}"
  SUBJ="/CN=${altname}/"
  [[ "${OSTYPE:0:5}" = "MINGW" ]] && SUBJ="/${SUBJ}"
  _openssl req -x509 -new -sha256 -nodes -newkey rsa:2048 -keyout "${alpncertdir}/${altname}.key.pem" -out "${alpncertdir}/${altname}.crt.pem" -subj "${SUBJ}" -extensions SAN -config "${tmp_openssl_cnf}"
  chmod g+r "${alpncertdir}/${altname}.key.pem" "${alpncertdir}/${altname}.crt.pem"
  rm -f "${tmp_openssl_cnf}"
}

# Create certificate for domain(s)
sign_domain() {
  local certdir="${1}"
  shift
  timestamp="${1}"
  shift
  domain="${1}"
  altnames="${*}"

  export altnames

  echo " + Signing domains..."
  if [[ ${API} -eq 1 ]]; then
    if [[ -z "${CA_NEW_AUTHZ}" ]] || [[ -z "${CA_NEW_CERT}" ]]; then
      _exiterr "Certificate authority doesn't allow certificate signing"
    fi
  elif [[ ${API} -eq 2 ]] && [[ -z "${CA_NEW_ORDER}" ]]; then
    _exiterr "Certificate authority doesn't allow certificate signing"
  fi

  local privkey="privkey.pem"
  if [[ ! -e "${certdir}/cert-${timestamp}.csr" ]]; then
    # generate a new private key if we need or want one
    if [[ ! -r "${certdir}/privkey.pem" ]] || [[ "${PRIVATE_KEY_RENEW}" = "yes" ]]; then
      echo " + Generating private key..."
      privkey="privkey-${timestamp}.pem"
      local tmp_privkey="$(_mktemp)"
      case "${KEY_ALGO}" in
        rsa) _openssl genrsa -out "${tmp_privkey}" "${KEYSIZE}";;
        prime256v1|secp384r1) _openssl ecparam -genkey -name "${KEY_ALGO}" -out "${tmp_privkey}";;
      esac
      cat "${tmp_privkey}" > "${certdir}/privkey-${timestamp}.pem"
      rm "${tmp_privkey}"
    fi
    # move rolloverkey into position (if any)
    if [[ -r "${certdir}/privkey.pem" && -r "${certdir}/privkey.roll.pem" && "${PRIVATE_KEY_RENEW}" = "yes" && "${PRIVATE_KEY_ROLLOVER}" = "yes" ]]; then
      echo " + Moving Rolloverkey into position....  "
      mv "${certdir}/privkey.roll.pem" "${certdir}/privkey-tmp.pem"
      mv "${certdir}/privkey-${timestamp}.pem" "${certdir}/privkey.roll.pem"
      mv "${certdir}/privkey-tmp.pem" "${certdir}/privkey-${timestamp}.pem"
    fi
    # generate a new private rollover key if we need or want one
    if [[ ! -r "${certdir}/privkey.roll.pem" && "${PRIVATE_KEY_ROLLOVER}" = "yes" && "${PRIVATE_KEY_RENEW}" = "yes" ]]; then
      echo " + Generating private rollover key..."
      case "${KEY_ALGO}" in
        rsa) _openssl genrsa -out "${certdir}/privkey.roll.pem" "${KEYSIZE}";;
        prime256v1|secp384r1) _openssl ecparam -genkey -name "${KEY_ALGO}" -out "${certdir}/privkey.roll.pem";;
      esac
    fi
    # delete rolloverkeys if disabled
    if [[ -r "${certdir}/privkey.roll.pem" && ! "${PRIVATE_KEY_ROLLOVER}" = "yes" ]]; then
      echo " + Removing Rolloverkey (feature disabled)..."
      rm -f "${certdir}/privkey.roll.pem"
    fi

    # Generate signing request config and the actual signing request
    echo " + Generating signing request..."
    SAN=""
    for altname in ${altnames}; do
      SAN="${SAN}DNS:${altname}, "
    done
    SAN="${SAN%%, }"
    local tmp_openssl_cnf
    tmp_openssl_cnf="$(_mktemp)"
    cat "${OPENSSL_CNF}" > "${tmp_openssl_cnf}"
    printf "\n[SAN]\nsubjectAltName=%s" "${SAN}" >> "${tmp_openssl_cnf}"
    if [ "${OCSP_MUST_STAPLE}" = "yes" ]; then
      printf "\n1.3.6.1.5.5.7.1.24=DER:30:03:02:01:05" >> "${tmp_openssl_cnf}"
    fi
    SUBJ="/CN=${domain}/"
    if [[ "${OSTYPE:0:5}" = "MINGW" ]]; then
      # The subject starts with a /, so MSYS will assume it's a path and convert
      # it unless we escape it with another one:
      SUBJ="/${SUBJ}"
    fi
    "${OPENSSL}" req -new -sha256 -key "${certdir}/${privkey}" -out "${certdir}/cert-${timestamp}.csr" -subj "${SUBJ}" -reqexts SAN -config "${tmp_openssl_cnf}"
    rm -f "${tmp_openssl_cnf}"
  fi

  crt_path="${certdir}/cert-${timestamp}.pem"
  # shellcheck disable=SC2086
  sign_csr "$(< "${certdir}/cert-${timestamp}.csr")" ${altnames} 3>"${crt_path}"

  # Create fullchain.pem
  echo " + Creating fullchain.pem..."
  if [[ ${API} -eq 1 ]]; then
    cat "${crt_path}" > "${certdir}/fullchain-${timestamp}.pem"
    local issuer_hash
    issuer_hash="$(get_issuer_hash "${crt_path}")"
    if [ -e "${CHAINCACHE}/${issuer_hash}.chain" ]; then
      echo " + Using cached chain!"
      cat "${CHAINCACHE}/${issuer_hash}.chain" > "${certdir}/chain-${timestamp}.pem"
    else
      echo " + Walking chain..."
      local issuer_cert_uri
      issuer_cert_uri="$(get_issuer_cert_uri "${crt_path}" || echo "unknown")"
      (walk_chain "${crt_path}" > "${certdir}/chain-${timestamp}.pem") || _exiterr "Walking chain has failed, your certificate has been created and can be found at ${crt_path}, the corresponding private key at ${privkey}. If you want you can manually continue on creating and linking all necessary files. If this error occurs again you should manually generate the certificate chain and place it under ${CHAINCACHE}/${issuer_hash}.chain (see ${issuer_cert_uri})"
      cat "${certdir}/chain-${timestamp}.pem" > "${CHAINCACHE}/${issuer_hash}.chain"
    fi
    cat "${certdir}/chain-${timestamp}.pem" >> "${certdir}/fullchain-${timestamp}.pem"
  else
    tmpcert="$(_mktemp)"
    tmpchain="$(_mktemp)"
    awk '{print >out}; /----END CERTIFICATE-----/{out=tmpchain}' out="${tmpcert}" tmpchain="${tmpchain}" "${certdir}/cert-${timestamp}.pem"
    mv "${certdir}/cert-${timestamp}.pem" "${certdir}/fullchain-${timestamp}.pem"
    cat "${tmpcert}" > "${certdir}/cert-${timestamp}.pem"
    cat "${tmpchain}" > "${certdir}/chain-${timestamp}.pem"
    rm "${tmpcert}" "${tmpchain}"
  fi

  # Wait for hook script to sync the files before creating the symlinks
  [[ -n "${HOOK}" ]] && ("${HOOK}" "sync_cert" "${certdir}/privkey-${timestamp}.pem" "${certdir}/cert-${timestamp}.pem" "${certdir}/fullchain-${timestamp}.pem" "${certdir}/chain-${timestamp}.pem" "${certdir}/cert-${timestamp}.csr" || _exiterr 'sync_cert hook returned with non-zero exit code')

  # Update symlinks
  [[ "${privkey}" = "privkey.pem" ]] || ln -sf "privkey-${timestamp}.pem" "${certdir}/privkey.pem"

  ln -sf "chain-${timestamp}.pem" "${certdir}/chain.pem"
  ln -sf "fullchain-${timestamp}.pem" "${certdir}/fullchain.pem"
  ln -sf "cert-${timestamp}.csr" "${certdir}/cert.csr"
  ln -sf "cert-${timestamp}.pem" "${certdir}/cert.pem"

  # Wait for hook script to clean the challenge and to deploy cert if used
  [[ -n "${HOOK}" ]] && ("${HOOK}" "deploy_cert" "${domain}" "${certdir}/privkey.pem" "${certdir}/cert.pem" "${certdir}/fullchain.pem" "${certdir}/chain.pem" "${timestamp}" || _exiterr 'deploy_cert hook returned with non-zero exit code')

  unset challenge_token
  echo " + Done!"
}

# Usage: --version (-v)
# Description: Print version information
command_version() {
  load_config noverify

  echo "Dehydrated by Lukas Schauer"
  echo "https://dehydrated.io"
  echo ""
  echo "Dehydrated version: ${VERSION}"
  revision="$(cd "${SCRIPTDIR}"; git rev-parse HEAD 2>/dev/null || echo "unknown")"
  echo "GIT-Revision: ${revision}"
  echo ""
  if [[ "${OSTYPE}" =~ "BSD" ]]; then
    echo "OS: $(uname -sr)"
  elif [[ -e /etc/os-release ]]; then
    ( . /etc/os-release && echo "OS: $PRETTY_NAME" )
  elif [[ -e /usr/lib/os-release ]]; then
    ( . /usr/lib/os-release && echo "OS: $PRETTY_NAME" )
  else
    echo "OS: $(cat /etc/issue | grep -v ^$ | head -n1 | _sed 's/\\(r|n|l) .*//g')"
  fi
  echo "Used software:"
  [[ -n "${BASH_VERSION:-}" ]] && echo " bash: ${BASH_VERSION}"
  [[ -n "${ZSH_VERSION:-}" ]] && echo " zsh: ${ZSH_VERSION}"
  echo " curl: ${CURL_VERSION}"
  if [[ "${OSTYPE}" =~ "BSD" ]]; then
    echo " awk, sed, mktemp, grep, diff: BSD base system versions"
  else
    echo " awk: $(awk -W version 2>&1 | head -n1)"
    echo " sed: $(sed --version 2>&1 | head -n1)"
    echo " mktemp: $(mktemp --version 2>&1 | head -n1)"
    echo " grep: $(grep --version 2>&1 | head -n1)"
    echo " diff: $(diff --version 2>&1 | head -n1)"
  fi
  echo " openssl: $("${OPENSSL}" version 2>&1)"

  exit 0
}

# Usage: --display-terms
# Description: Display current terms of service
command_terms() {
  init_system
  echo "The current terms of service: $CA_TERMS"
  echo "+ Done!"
  exit 0
}

# Usage: --register
# Description: Register account key
command_register() {
  init_system
  echo "+ Done!"
  exit 0
}

# Usage: --account
# Description: Update account contact information
command_account() {
  init_system
  FAILED=false

  NEW_ACCOUNT_KEY_JSON="$(_mktemp)"

  # Check if we have the registration url
  if [[ -z "${ACCOUNT_URL}" ]]; then
    _exiterr "Error retrieving registration url."
  fi

  echo "+ Updating registration url: ${ACCOUNT_URL} contact information..."
  if [[ ${API} -eq 1 ]]; then
    # If an email for the contact has been provided then adding it to the registered account
    if [[ -n "${CONTACT_EMAIL}" ]]; then
      (signed_request "${ACCOUNT_URL}" '{"resource": "reg", "contact":["mailto:'"${CONTACT_EMAIL}"'"]}' > "${NEW_ACCOUNT_KEY_JSON}") || FAILED=true
    else
      (signed_request "${ACCOUNT_URL}" '{"resource": "reg", "contact":[]}' > "${NEW_ACCOUNT_KEY_JSON}") || FAILED=true
    fi
  else
    # If an email for the contact has been provided then adding it to the registered account
    if [[ -n "${CONTACT_EMAIL}" ]]; then
      (signed_request "${ACCOUNT_URL}" '{"contact":["mailto:'"${CONTACT_EMAIL}"'"]}' > "${NEW_ACCOUNT_KEY_JSON}") || FAILED=true
    else
      (signed_request "${ACCOUNT_URL}" '{"contact":[]}' > "${NEW_ACCOUNT_KEY_JSON}") || FAILED=true
    fi
  fi

  if [[ "${FAILED}" = "true" ]]; then
    rm "${NEW_ACCOUNT_KEY_JSON}"
    _exiterr "Error updating account information. See message above for more information."
  fi
  if diff -q "${NEW_ACCOUNT_KEY_JSON}" "${ACCOUNT_KEY_JSON}" > /dev/null; then
    echo "+ Account information was the same after the update"
    rm "${NEW_ACCOUNT_KEY_JSON}"
  else
    ACCOUNT_KEY_JSON_BACKUP="${ACCOUNT_KEY_JSON%.*}-$(date +%s).json"
    echo "+ Backup ${ACCOUNT_KEY_JSON} as ${ACCOUNT_KEY_JSON_BACKUP}"
    cp -p "${ACCOUNT_KEY_JSON}" "${ACCOUNT_KEY_JSON_BACKUP}"
    echo "+ Populate ${ACCOUNT_KEY_JSON}"
    mv "${NEW_ACCOUNT_KEY_JSON}" "${ACCOUNT_KEY_JSON}"
  fi
  echo "+ Done!"
  exit 0
}

# Usage: --cron (-c)
# Description: Sign/renew non-existent/changed/expiring certificates.
command_sign_domains() {
  init_system
  hookscript_bricker_hook

  # Call startup hook
  [[ -n "${HOOK}" ]] && ("${HOOK}" "startup_hook" || _exiterr 'startup_hook hook returned with non-zero exit code')

  if [ ! -d "${CHAINCACHE}" ]; then
    echo " + Creating chain cache directory ${CHAINCACHE}"
    mkdir "${CHAINCACHE}"
  fi

  if [[ -n "${PARAM_DOMAIN:-}" ]]; then
    DOMAINS_TXT="$(_mktemp)"
    if [[ -n "${PARAM_ALIAS:-}" ]]; then
      printf -- "${PARAM_DOMAIN} > ${PARAM_ALIAS}" > "${DOMAINS_TXT}"
    else
      printf -- "${PARAM_DOMAIN}" > "${DOMAINS_TXT}"
    fi
  elif [[ -e "${DOMAINS_TXT}" ]]; then
    if [[ ! -r "${DOMAINS_TXT}" ]]; then
      _exiterr "domains.txt found but not readable"
    fi
  else
    _exiterr "domains.txt not found and --domain not given"
  fi

  # Generate certificates for all domains found in domains.txt. Check if existing certificate are about to expire
  ORIGIFS="${IFS}"
  IFS=$'\n'
  for line in $(<"${DOMAINS_TXT}" tr -d '\r' | awk '{print tolower($0)}' | _sed -e 's/^[[:space:]]*//g' -e 's/[[:space:]]*$//g' -e 's/[[:space:]]+/ /g' -e 's/([^ ])>/\1 >/g' -e 's/> />/g' | (grep -vE '^(#|$)' || true)); do
    reset_configvars
    IFS="${ORIGIFS}"
    alias="$(grep -Eo '>[^ ]+' <<< "${line}" || true)"
    line="$(_sed -e 's/>[^ ]+[ ]*//g' <<< "${line}")"
    aliascount="$(grep -Eo '>' <<< "${alias}" | awk 'END {print NR}' || true )"
    [ ${aliascount} -gt 1 ] && _exiterr "Only one alias per line is allowed in domains.txt!"

    domain="$(printf '%s\n' "${line}" | cut -d' ' -f1)"
    morenames="$(printf '%s\n' "${line}" | cut -s -d' ' -f2-)"
    [ ${aliascount} -lt 1 ] && alias="${domain}" || alias="${alias#>}"
    export alias

    if [[ -z "${morenames}" ]];then
      echo "Processing ${domain}"
    else
      echo "Processing ${domain} with alternative names: ${morenames}"
    fi

    if [ "${alias:0:2}" = "*." ]; then
      _exiterr "Please define a valid alias for your ${domain} wildcard-certificate. See domains.txt-documentation for more details."
    fi

    local certdir="${CERTDIR}/${alias}"
    cert="${certdir}/cert.pem"
    chain="${certdir}/chain.pem"

    force_renew="${PARAM_FORCE:-no}"

    timestamp="$(date +%s)"

    # If there is no existing certificate directory => make it
    if [[ ! -e "${certdir}" ]]; then
      echo " + Creating new directory ${certdir} ..."
      mkdir -p "${certdir}" || _exiterr "Unable to create directory ${certdir}"
    fi

    # read cert config
    # for now this loads the certificate specific config in a subshell and parses a diff of set variables.
    # we could just source the config file but i decided to go this way to protect people from accidentally overriding
    # variables used internally by this script itself.
    if [[ -n "${DOMAINS_D}" ]]; then
      certconfig="${DOMAINS_D}/${alias}"
    else
      certconfig="${certdir}/config"
    fi

    if [ -f "${certconfig}" ]; then
      echo " + Using certificate specific config file!"
      ORIGIFS="${IFS}"
      IFS=$'\n'
      for cfgline in $(
        beforevars="$(_mktemp)"
        aftervars="$(_mktemp)"
        set > "${beforevars}"
        # shellcheck disable=SC1090
        . "${certconfig}"
        set > "${aftervars}"
        diff -u "${beforevars}" "${aftervars}" | grep -E '^\+[^+]'
        rm "${beforevars}"
        rm "${aftervars}"
      ); do
        config_var="$(echo "${cfgline:1}" | cut -d'=' -f1)"
        config_value="$(echo "${cfgline:1}" | cut -d'=' -f2- | tr -d "'")"
	# All settings that are allowed here should also be stored and
	# restored in store_configvars() and reset_configvars()
        case "${config_var}" in
          KEY_ALGO|OCSP_MUST_STAPLE|OCSP_FETCH|OCSP_DAYS|PRIVATE_KEY_RENEW|PRIVATE_KEY_ROLLOVER|KEYSIZE|CHALLENGETYPE|HOOK|PREFERRED_CHAIN|WELLKNOWN|HOOK_CHAIN|OPENSSL_CNF|RENEW_DAYS)
            echo "   + ${config_var} = ${config_value}"
            declare -- "${config_var}=${config_value}"
            ;;
          _) ;;
          *) echo "   ! Setting ${config_var} on a per-certificate base is not (yet) supported" >&2
        esac
      done
      IFS="${ORIGIFS}"
    fi
    verify_config
    hookscript_bricker_hook
    export WELLKNOWN CHALLENGETYPE KEY_ALGO PRIVATE_KEY_ROLLOVER

    skip="no"

    # Allow for external CSR generation
    local csr=""
    if [[ -n "${HOOK}" ]]; then
      csr="$("${HOOK}" "generate_csr" "${domain}" "${certdir}" "${domain} ${morenames}")" || _exiterr 'generate_csr hook returned with non-zero exit code'
      if grep -qE "\-----BEGIN (NEW )?CERTIFICATE REQUEST-----" <<< "${csr}"; then
        altnames="$(extract_altnames "${csr}")"
        domain="$(cut -d' ' -f1 <<< "${altnames}")"
        morenames="$(cut -s -d' ' -f2- <<< "${altnames}")"
        echo " + Using CSR from hook script (real names: ${altnames})"
      else
        csr=""
      fi
    fi

    # Check domain names of existing certificate
    if [[ -e "${cert}" ]]; then
      printf " + Checking domain name(s) of existing cert..."

      certnames="$("${OPENSSL}" x509 -in "${cert}" -text -noout | grep DNS: | _sed 's/DNS://g' | tr -d ' ' | tr ',' '\n' | sort -u | tr '\n' ' ' | _sed 's/ $//')"
      givennames="$(echo "${domain}" "${morenames}"| tr ' ' '\n' | sort -u | tr '\n' ' ' | _sed 's/ $//' | _sed 's/^ //')"

      if [[ "${certnames}" = "${givennames}" ]]; then
        echo " unchanged."
      else
        echo " changed!"
        echo " + Domain name(s) are not matching!"
        echo " + Names in old certificate: ${certnames}"
        echo " + Configured names: ${givennames}"
        echo " + Forcing renew."
        force_renew="yes"
      fi
    fi

    # Check expire date of existing certificate
    if [[ -e "${cert}" ]]; then
      echo " + Checking expire date of existing cert..."
      valid="$("${OPENSSL}" x509 -enddate -noout -in "${cert}" | cut -d= -f2- )"

      printf " + Valid till %s " "${valid}"
      if ("${OPENSSL}" x509 -checkend $((RENEW_DAYS * 86400)) -noout -in "${cert}" > /dev/null 2>&1); then
        printf "(Longer than %d days). " "${RENEW_DAYS}"
        if [[ "${force_renew}" = "yes" ]]; then
          echo "Ignoring because renew was forced!"
        else
          # Certificate-Names unchanged and cert is still valid
          echo "Skipping renew!"
          [[ -n "${HOOK}" ]] && ("${HOOK}" "unchanged_cert" "${domain}" "${certdir}/privkey.pem" "${certdir}/cert.pem" "${certdir}/fullchain.pem" "${certdir}/chain.pem" || _exiterr 'unchanged_cert hook returned with non-zero exit code')
          skip="yes"
        fi
      else
        echo "(Less than ${RENEW_DAYS} days). Renewing!"
      fi
    fi

    local update_ocsp
    update_ocsp="no"

    # Sign certificate for this domain
    if [[ ! "${skip}" = "yes" ]]; then
      update_ocsp="yes"
      [[ -z "${csr}" ]] || printf "%s" "${csr}" > "${certdir}/cert-${timestamp}.csr"
      if [[ "${PARAM_KEEP_GOING:-}" = "yes" ]]; then
        skip_exit_hook=yes
        sign_domain "${certdir}" ${timestamp} ${domain} ${morenames} &
        wait $! || exit_with_errorcode=1
        skip_exit_hook=no
      else
        sign_domain "${certdir}" ${timestamp} ${domain} ${morenames}
      fi
    fi

    if [[ "${OCSP_FETCH}" = "yes" ]]; then
      local ocsp_url
      ocsp_url="$(get_ocsp_url "${cert}")"

      if [[ ! -e "${certdir}/ocsp.der" ]]; then
        update_ocsp="yes"
      elif ! ("${OPENSSL}" ocsp -no_nonce -issuer "${chain}" -verify_other "${chain}" -cert "${cert}" -respin "${certdir}/ocsp.der" -status_age $((OCSP_DAYS*24*3600)) 2>&1 | grep -q "${cert}: good"); then
        update_ocsp="yes"
      fi

      if [[ "${update_ocsp}" = "yes" ]]; then
        echo " + Updating OCSP stapling file"
        ocsp_timestamp="$(date +%s)"
        if grep -qE "^(openssl (0|(1\.0))\.)|(libressl (1|2|3)\.)" <<< "$(${OPENSSL} version | awk '{print tolower($0)}')"; then
          ocsp_log="$("${OPENSSL}" ocsp -no_nonce -issuer "${chain}" -verify_other "${chain}" -cert "${cert}" -respout "${certdir}/ocsp-${ocsp_timestamp}.der" -url "${ocsp_url}" -header "HOST" "$(echo "${ocsp_url}" | _sed -e 's/^http(s?):\/\///' -e 's/\/.*$//g')" 2>&1)" || _exiterr "Error while fetching OCSP information: ${ocsp_log}"
        else
          ocsp_log="$("${OPENSSL}" ocsp -no_nonce -issuer "${chain}" -verify_other "${chain}" -cert "${cert}" -respout "${certdir}/ocsp-${ocsp_timestamp}.der" -url "${ocsp_url}" 2>&1)" || _exiterr "Error while fetching OCSP information: ${ocsp_log}"
        fi
        ln -sf "ocsp-${ocsp_timestamp}.der" "${certdir}/ocsp.der"
        [[ -n "${HOOK}" ]] && (altnames="${domain} ${morenames}" "${HOOK}" "deploy_ocsp" "${domain}" "${certdir}/ocsp.der" "${ocsp_timestamp}" || _exiterr 'deploy_ocsp hook returned with non-zero exit code')
      else
        echo " + OCSP stapling file is still valid (skipping update)"
      fi
    fi
  done
  reset_configvars

  # remove temporary domains.txt file if used
  [[ -n "${PARAM_DOMAIN:-}" ]] && rm -f "${DOMAINS_TXT}"

  [[ -n "${HOOK}" ]] && ("${HOOK}" "exit_hook" || echo 'exit_hook returned with non-zero exit code!' >&2)
  if [[ "${AUTO_CLEANUP}" == "yes" ]]; then
    echo "+ Running automatic cleanup"
    command_cleanup noinit
  fi

  exit "${exit_with_errorcode}"
}

# Usage: --signcsr (-s) path/to/csr.pem
# Description: Sign a given CSR, output CRT on stdout (advanced usage)
command_sign_csr() {
  init_system

  # redirect stdout to stderr
  # leave stdout over at fd 3 to output the cert
  exec 3>&1 1>&2

  # load csr
  csrfile="${1}"
  if [ ! -r "${csrfile}" ]; then
    _exiterr "Could not read certificate signing request ${csrfile}"
  fi
  csr="$(cat "${csrfile}")"

  # extract names
  altnames="$(extract_altnames "${csr}")"

  # gen cert
  certfile="$(_mktemp)"
  sign_csr "${csr}" ${altnames} 3> "${certfile}"

  # print cert
  echo "# CERT #" >&3
  cat "${certfile}" >&3
  echo >&3

  # print chain
  if [ -n "${PARAM_FULL_CHAIN:-}" ]; then
    # get and convert ca cert
    chainfile="$(_mktemp)"
    tmpchain="$(_mktemp)"
    http_request get "$("${OPENSSL}" x509 -in "${certfile}" -noout -text | grep 'CA Issuers - URI:' | cut -d':' -f2-)" > "${tmpchain}"
    if grep -q "BEGIN CERTIFICATE" "${tmpchain}"; then
      mv "${tmpchain}" "${chainfile}"
    else
      "${OPENSSL}" x509 -in "${tmpchain}" -inform DER -out "${chainfile}" -outform PEM
      rm "${tmpchain}"
    fi

    echo "# CHAIN #" >&3
    cat "${chainfile}" >&3

    rm "${chainfile}"
  fi

  # cleanup
  rm "${certfile}"

  exit 0
}

# Usage: --revoke (-r) path/to/cert.pem
# Description: Revoke specified certificate
command_revoke() {
  init_system

  [[ -n "${CA_REVOKE_CERT}" ]] || _exiterr "Certificate authority doesn't allow certificate revocation."

  cert="${1}"
  if [[ -L "${cert}" ]]; then
    # follow symlink and use real certificate name (so we move the real file and not the symlink at the end)
    local link_target
    link_target="$(readlink -n "${cert}")"
    if [[ "${link_target}" =~ ^/ ]]; then
      cert="${link_target}"
    else
      cert="$(dirname "${cert}")/${link_target}"
    fi
  fi
  [[ -f "${cert}" ]] || _exiterr "Could not find certificate ${cert}"

  echo "Revoking ${cert}"

  cert64="$("${OPENSSL}" x509 -in "${cert}" -inform PEM -outform DER | urlbase64)"
  if [[ ${API} -eq 1 ]]; then
    response="$(signed_request "${CA_REVOKE_CERT}" '{"resource": "revoke-cert", "certificate": "'"${cert64}"'"}' | clean_json)"
  else
    response="$(signed_request "${CA_REVOKE_CERT}" '{"certificate": "'"${cert64}"'"}' | clean_json)"
  fi
  # if there is a problem with our revoke request _request (via signed_request) will report this and "exit 1" out
  # so if we are here, it is safe to assume the request was successful
  echo " + Done."
  echo " + Renaming certificate to ${cert}-revoked"
  mv -f "${cert}" "${cert}-revoked"
}

# Usage: --deactivate
# Description: Deactivate account
command_deactivate() {
  init_system

  echo "Deactivating account ${ACCOUNT_URL}"

  if [[ ${API} -eq 1 ]]; then
    echo "Deactivation for ACMEv1 is not implemented"
  else
    response="$(signed_request "${ACCOUNT_URL}" '{"status": "deactivated"}' | clean_json)"
    deactstatus=$(echo "$response" | jsonsh | get_json_string_value "status")
    if [[ "${deactstatus}" = "deactivated" ]]; then
      touch "${ACCOUNT_DEACTIVATED}"
    else
      _exiterr "Account deactivation failed!"
    fi
  fi

  echo " + Done."
}

# Usage: --cleanup (-gc)
# Description: Move unused certificate files to archive directory
command_cleanup() {
  if [ ! "${1:-}" = "noinit" ]; then
    load_config
  fi

  if [[ ! "${PARAM_CLEANUPDELETE:-}" = "yes" ]]; then
    # Create global archive directory if not existent
    if [[ ! -e "${BASEDIR}/archive" ]]; then
      mkdir "${BASEDIR}/archive"
    fi
  fi

  # Allow globbing
  [[ -n "${ZSH_VERSION:-}" ]] && set +o noglob || set +f

  # Loop over all certificate directories
  for certdir in "${CERTDIR}/"*; do
    # Skip if entry is not a folder
    [[ -d "${certdir}" ]] || continue

    # Get certificate name
    certname="$(basename "${certdir}")"

    # Create certificates archive directory if not existent
    if [[ ! "${PARAM_CLEANUPDELETE:-}" = "yes" ]]; then
      archivedir="${BASEDIR}/archive/${certname}"
      if [[ ! -e "${archivedir}" ]]; then
        mkdir "${archivedir}"
      fi
    fi

    # Loop over file-types (certificates, keys, signing-requests, ...)
    for filetype in cert.csr cert.pem chain.pem fullchain.pem privkey.pem ocsp.der; do
      # Delete all if symlink is broken
      if [[ -r "${certdir}/${filetype}" ]]; then
        # Look up current file in use
        current="$(basename "$(readlink "${certdir}/${filetype}")")"
      else
        if [[ -h "${certdir}/${filetype}" ]]; then
          echo "Removing broken symlink: ${certdir}/${filetype}"
          rm -f "${certdir}/${filetype}"
        fi
        current=""
      fi

      # Split filetype into name and extension
      filebase="$(echo "${filetype}" | cut -d. -f1)"
      fileext="$(echo "${filetype}" | cut -d. -f2)"

      # Loop over all files of this type
      for file in "${certdir}/${filebase}-"*".${fileext}" "${certdir}/${filebase}-"*".${fileext}-revoked"; do
        # Check if current file is in use, if unused move to archive directory
        filename="$(basename "${file}")"
        if [[ ! "${filename}" = "${current}" ]] && [[ -f "${certdir}/${filename}" ]]; then
          echo "${filename}"
          if [[ "${PARAM_CLEANUPDELETE:-}" = "yes" ]]; then
            echo "Deleting unused file: ${certname}/${filename}"
            rm "${certdir}/${filename}"
          else
            echo "Moving unused file to archive directory: ${certname}/${filename}"
            mv "${certdir}/${filename}" "${archivedir}/${filename}"
          fi
        fi
      done
    done
  done

  exit "${exit_with_errorcode}"
}

# Usage: --cleanup-delete (-gcd)
# Description: Deletes (!) unused certificate files
command_cleanupdelete() {
  command_cleanup
}


# Usage: --help (-h)
# Description: Show help text
command_help() {
  printf "Usage: %s [-h] [command [argument]] [parameter [argument]] [parameter [argument]] ...\n\n" "${0}"
  printf "Default command: help\n\n"
  echo "Commands:"
  grep -e '^[[:space:]]*# Usage:' -e '^[[:space:]]*# Description:' -e '^command_.*()[[:space:]]*{' "${0}" | while read -r usage; read -r description; read -r command; do
    if [[ ! "${usage}" =~ Usage ]] || [[ ! "${description}" =~ Description ]] || [[ ! "${command}" =~ ^command_ ]]; then
      _exiterr "Error generating help text."
    fi
    printf " %-32s %s\n" "${usage##"# Usage: "}" "${description##"# Description: "}"
  done
  printf -- "\nParameters:\n"
  grep -E -e '^[[:space:]]*# PARAM_Usage:' -e '^[[:space:]]*# PARAM_Description:' "${0}" | while read -r usage; read -r description; do
    if [[ ! "${usage}" =~ Usage ]] || [[ ! "${description}" =~ Description ]]; then
      _exiterr "Error generating help text."
    fi
    printf " %-32s %s\n" "${usage##"# PARAM_Usage: "}" "${description##"# PARAM_Description: "}"
  done
}

# Usage: --env (-e)
# Description: Output configuration variables for use in other scripts
command_env() {
  echo "# dehydrated configuration"
  load_config
  typeset -p CA CERTDIR ALPNCERTDIR CHALLENGETYPE DOMAINS_D DOMAINS_TXT HOOK HOOK_CHAIN RENEW_DAYS ACCOUNT_KEY ACCOUNT_KEY_JSON ACCOUNT_ID_JSON KEYSIZE WELLKNOWN PRIVATE_KEY_RENEW OPENSSL_CNF CONTACT_EMAIL LOCKFILE
}

# Main method (parses script arguments and calls command_* methods)
main() {
  exit_with_errorcode=0
  skip_exit_hook=no
  COMMAND=""
  set_command() {
    [[ -z "${COMMAND}" ]] || _exiterr "Only one command can be executed at a time. See help (-h) for more information."
    COMMAND="${1}"
  }

  check_parameters() {
    if [[ -z "${1:-}" ]]; then
      echo "The specified command requires additional parameters. See help:" >&2
      echo >&2
      command_help >&2
      exit 1
    elif [[ "${1:0:1}" = "-" ]]; then
      _exiterr "Invalid argument: ${1}"
    fi
  }

  # shellcheck disable=SC2199
  [[ -z "${@}" ]] && eval set -- "--help"

  while (( ${#} )); do
    case "${1}" in
      --help|-h)
        command_help
        exit 0
        ;;

      --env|-e)
        set_command env
        ;;

      --cron|-c)
        set_command sign_domains
        ;;

      --register)
        set_command register
        ;;

      --account)
        set_command account
        ;;

      # PARAM_Usage: --accept-terms
      # PARAM_Description: Accept CAs terms of service
      --accept-terms)
        PARAM_ACCEPT_TERMS="yes"
        ;;

      --display-terms)
        set_command terms
        ;;

      --signcsr|-s)
        shift 1
        set_command sign_csr
        check_parameters "${1:-}"
        PARAM_CSR="${1}"
        ;;

      --revoke|-r)
        shift 1
        set_command revoke
        check_parameters "${1:-}"
        PARAM_REVOKECERT="${1}"
        ;;

      --deactivate)
        set_command deactivate
        ;;

      --version|-v)
        set_command version
        ;;

      --cleanup|-gc)
        set_command cleanup
        ;;

      --cleanup-delete|-gcd)
        set_command cleanupdelete
        PARAM_CLEANUPDELETE="yes"
        ;;

      # PARAM_Usage: --full-chain (-fc)
      # PARAM_Description: Print full chain when using --signcsr
      --full-chain|-fc)
        PARAM_FULL_CHAIN="1"
        ;;

      # PARAM_Usage: --ipv4 (-4)
      # PARAM_Description: Resolve names to IPv4 addresses only
      --ipv4|-4)
        PARAM_IP_VERSION="4"
        ;;

      # PARAM_Usage: --ipv6 (-6)
      # PARAM_Description: Resolve names to IPv6 addresses only
      --ipv6|-6)
        PARAM_IP_VERSION="6"
        ;;

      # PARAM_Usage: --domain (-d) domain.tld
      # PARAM_Description: Use specified domain name(s) instead of domains.txt entry (one certificate!)
      --domain|-d)
        shift 1
        check_parameters "${1:-}"
        if [[ -z "${PARAM_DOMAIN:-}" ]]; then
          PARAM_DOMAIN="${1}"
        else
          PARAM_DOMAIN="${PARAM_DOMAIN} ${1}"
         fi
        ;;

      # PARAM_Usage: --ca url/preset
      # PARAM_Description: Use specified CA URL or preset
      --ca)
        shift 1
        check_parameters "${1:-}"
        [[ -n "${PARAM_CA:-}" ]] && _exiterr "CA can only be specified once!"
        PARAM_CA="${1}"
        ;;

      # PARAM_Usage: --alias certalias
      # PARAM_Description: Use specified name for certificate directory (and per-certificate config) instead of the primary domain (only used if --domain is specified)
      --alias)
        shift 1
        check_parameters "${1:-}"
        [[ -n "${PARAM_ALIAS:-}" ]] && _exiterr "Alias can only be specified once!"
        PARAM_ALIAS="${1}"
        ;;

      # PARAM_Usage: --keep-going (-g)
      # PARAM_Description: Keep going after encountering an error while creating/renewing multiple certificates in cron mode
      --keep-going|-g)
        PARAM_KEEP_GOING="yes"
        ;;

      # PARAM_Usage: --force (-x)
      # PARAM_Description: Force renew of certificate even if it is longer valid than value in RENEW_DAYS
      --force|-x)
        PARAM_FORCE="yes"
        ;;

      # PARAM_Usage: --force-validation
      # PARAM_Description: Force revalidation of domain names (used in combination with --force)
      --force-validation)
        PARAM_FORCE_VALIDATION="yes"
        ;;

      # PARAM_Usage: --no-lock (-n)
      # PARAM_Description: Don't use lockfile (potentially dangerous!)
      --no-lock|-n)
        PARAM_NO_LOCK="yes"
        ;;

      # PARAM_Usage: --lock-suffix example.com
      # PARAM_Description: Suffix lockfile name with a string (useful for with -d)
      --lock-suffix)
        shift 1
        check_parameters "${1:-}"
        PARAM_LOCKFILE_SUFFIX="${1}"
        ;;

      # PARAM_Usage: --ocsp
      # PARAM_Description: Sets option in CSR indicating OCSP stapling to be mandatory
      --ocsp)
        PARAM_OCSP_MUST_STAPLE="yes"
        ;;

      # PARAM_Usage: --privkey (-p) path/to/key.pem
      # PARAM_Description: Use specified private key instead of account key (useful for revocation)
      --privkey|-p)
        shift 1
        check_parameters "${1:-}"
        PARAM_ACCOUNT_KEY="${1}"
        ;;

      # PARAM_Usage: --domains-txt path/to/domains.txt
      # PARAM_Description: Use specified domains.txt instead of default/configured one
      --domains-txt)
        shift 1
        check_parameters "${1:-}"
        PARAM_DOMAINS_TXT="${1}"
        ;;

      # PARAM_Usage: --config (-f) path/to/config
      # PARAM_Description: Use specified config file
      --config|-f)
        shift 1
        check_parameters "${1:-}"
        CONFIG="${1}"
        ;;

      # PARAM_Usage: --hook (-k) path/to/hook.sh
      # PARAM_Description: Use specified script for hooks
      --hook|-k)
        shift 1
        check_parameters "${1:-}"
        PARAM_HOOK="${1}"
        ;;

      # PARAM_Usage: --preferred-chain issuer-cn
      # PARAM_Description: Use alternative certificate chain identified by issuer CN
      --preferred-chain)
        shift 1
        check_parameters "${1:-}"
        PARAM_PREFERRED_CHAIN="${1}"
        ;;

      # PARAM_Usage: --out (-o) certs/directory
      # PARAM_Description: Output certificates into the specified directory
      --out|-o)
        shift 1
        check_parameters "${1:-}"
        PARAM_CERTDIR="${1}"
        ;;

      # PARAM_Usage: --alpn alpn-certs/directory
      # PARAM_Description: Output alpn verification certificates into the specified directory
      --alpn)
        shift 1
        check_parameters "${1:-}"
        PARAM_ALPNCERTDIR="${1}"
        ;;

      # PARAM_Usage: --challenge (-t) http-01|dns-01|tls-alpn-01
      # PARAM_Description: Which challenge should be used? Currently http-01, dns-01, and tls-alpn-01 are supported
      --challenge|-t)
        shift 1
        check_parameters "${1:-}"
        PARAM_CHALLENGETYPE="${1}"
        ;;

      # PARAM_Usage: --algo (-a) rsa|prime256v1|secp384r1
      # PARAM_Description: Which public key algorithm should be used? Supported: rsa, prime256v1 and secp384r1
      --algo|-a)
        shift 1
        check_parameters "${1:-}"
        PARAM_KEY_ALGO="${1}"
        ;;
      *)
        echo "Unknown parameter detected: ${1}" >&2
        echo >&2
        command_help >&2
        exit 1
        ;;
    esac

    shift 1
  done

  case "${COMMAND}" in
    env) command_env;;
    sign_domains) command_sign_domains;;
    register) command_register;;
    account) command_account;;
    sign_csr) command_sign_csr "${PARAM_CSR}";;
    revoke) command_revoke "${PARAM_REVOKECERT}";;
    deactivate) command_deactivate;;
    cleanup) command_cleanup;;
    terms) command_terms;;
    cleanupdelete) command_cleanupdelete;;
    version) command_version;;
    *) command_help; exit 1;;
  esac

  exit "${exit_with_errorcode}"
}

# Determine OS type
OSTYPE="$(uname)"

if [[ ! "${DEHYDRATED_NOOP:-}" = "NOOP" ]]; then
  # Run script
  main "${@:-}"
fi

# vi: expandtab sw=2 ts=2
