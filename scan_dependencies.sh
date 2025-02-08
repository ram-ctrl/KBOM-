#!/bin/bash

if ! command -v trivy &> /dev/null
then
    echo "Installing Trivy..."
    brew install trivy
fi

echo "Scanning dependencies..."
trivy fs --format json --output kbom.json .


#!/bin/bash

echo "Generating KBOM using Syft..."
syft backend -o json > backend-kbom.json
syft frontend -o json > frontend-kbom.json

echo "Scanning for vulnerabilities using Trivy..."
trivy fs --format json --output backend-vulnerabilities.json backend
trivy fs --format json --output frontend-vulnerabilities.json frontend

echo "Merging KBOM & Vulnerabilities..."

python3 merge_kbom.py


