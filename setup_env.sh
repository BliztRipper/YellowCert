#!/bin/bash

echo "🔧 Setting up YellowCert Python Environment"
echo "==========================================="

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo "Current Python version: $PYTHON_VERSION"

# Check if Python 3.13+
if [[ "$PYTHON_VERSION" == 3.13* ]] || [[ "$PYTHON_VERSION" > "3.13" ]]; then
    echo ""
    echo "⚠️  WARNING: Python 3.13+ detected!"
    echo "Many ML packages don't support Python 3.13 yet."
    echo ""
    echo "Please use Python 3.11 or 3.12 instead."
    echo ""
    echo "Options:"
    echo "1. Install Python 3.12 via conda:"
    echo "   conda create -n yellowcert python=3.12"
    echo "   conda activate yellowcert"
    echo ""
    echo "2. Install Python 3.12 via pyenv:"
    echo "   pyenv install 3.12.0"
    echo "   pyenv local 3.12.0"
    echo ""
    echo "3. Use system Python 3.11/3.12 if available"
    exit 1
fi

echo "✅ Python version compatible"
echo ""
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Train model: python train_model.py"
echo "2. Start backend: ./start_backend.sh"
echo "3. Start frontend: cd frontend && npm install && npm start"
