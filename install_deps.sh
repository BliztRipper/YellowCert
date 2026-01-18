#!/bin/bash

echo "🔧 Installing YellowCert Dependencies"
echo "======================================"

# Source conda
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh

# Activate environment
conda activate yellowcert

# Check Python version
echo ""
echo "Python version:"
python --version

echo ""
echo "📦 Installing Python packages (this may take 5-10 minutes)..."
echo ""

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. conda activate yellowcert"
echo "2. python train_model.py       # Train the model (takes time)"
echo "3. ./start_backend.sh          # Start backend server"
echo "4. ./start_frontend.sh         # Start frontend (in new terminal)"
