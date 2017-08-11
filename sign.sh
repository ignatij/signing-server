#!/bin/bash
# Sign a file with a private key using OpenSSL
# Encode the signature in Base64 format
#
# Usage: sign <file> <private_key_location> <output_filename>

filename=$1
private_key_location=$2
output_filename=$3
if [[ $# -lt 1 ]] ; then
  echo "Usage: sign <file>"
  exit 1
fi

openssl dgst -sha256 -sign $private_key_location -out $filename.sha256 -passin file:passphrase.txt $filename
openssl base64 -in $filename.sha256 -out $output_filename.signature
rm $filename.sha256
