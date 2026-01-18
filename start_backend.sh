#!/bin/bash

echo "🚀 Starting YellowCert Backend Server..."
echo "========================================="

# Source conda
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh

# Activate environment
conda activate yellowcert

echo "Using Python: $(which python)"
echo "Python version: $(python --version)"
echo ""

cd backend
python main.py
