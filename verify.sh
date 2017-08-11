#!/bin/bash
# Verify a file with a public key using OpenSSL
# Decode the signature from Base64 format
#
# Usage: verify <file> <public_key_location> <signature>

filename=$1
public_key_location=$2
signature=$3

if [[ $# -lt 2 ]] ; then
  echo "Usage: verify <file> <signature>"
  exit 1
fi

openssl base64 -d -in $signature -out $filename.sha256
openssl dgst -sha256 -verify $public_key_location -signature $filename.sha256 $filename
rm $filename.sha256
rm $signature
