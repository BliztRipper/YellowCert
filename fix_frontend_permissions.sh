#!/bin/bash

echo "🔧 Fixing frontend permissions and reinstalling..."

cd "$(dirname "$0")/frontend"

# Remove node_modules with sudo
echo "Step 1: Removing old node_modules (requires your password)..."
sudo rm -rf node_modules package-lock.json .cache

echo ""
echo "Step 2: Installing npm packages (this may take a few minutes)..."
npm install

echo ""
echo "✅ Done! Frontend is ready."
echo ""
echo "To start the frontend:"
echo "   cd frontend"
echo "   npm start"
