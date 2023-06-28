#!/bin/bash
set -e
rm -rf package
mkdir package
pip install --target ./package openai
cd package
zip -r ../function.zip .
cd ..
rm -rf package