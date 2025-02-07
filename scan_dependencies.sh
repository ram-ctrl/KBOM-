#!/bin/bash

if ! command -v trivy &> /dev/null
then
    echo "Installing Trivy..."
    brew install trivy
fi

echo "Scanning dependencies..."
trivy fs --format json --output kbom.json .

