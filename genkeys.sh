#!/bin/bash
# Generate private and public key pair
#
# Usage: genkeys <folder_name>
private_key_location=$1
public_key_location=$2


openssl genrsa -aes128 -passout file:passphrase.txt -out $private_key_location 4096
openssl rsa -in $private_key_location -passin file:passphrase.txt -pubout -out $public_key_location