#!/bin/bash

# YellowCert - Prepare Dataset for Google Colab Training
# This script creates a ZIP file of your dataset ready for Colab upload

echo "=========================================="
echo "🏥 YellowCert - Prepare for Colab"
echo "=========================================="
echo ""

# Check if required directories exist
echo "Checking dataset directories..."

missing_dirs=()

if [ ! -d "train" ]; then
    missing_dirs+=("train/")
fi

if [ ! -d "valid" ]; then
    missing_dirs+=("valid/")
fi

if [ ! -d "test" ]; then
    missing_dirs+=("test/")
fi

if [ ! -f "data.yaml" ]; then
    missing_dirs+=("data.yaml")
fi

if [ ${#missing_dirs[@]} -gt 0 ]; then
    echo "❌ Error: Missing required files/directories:"
    for dir in "${missing_dirs[@]}"; do
        echo "   - $dir"
    done
    echo ""
    echo "Please ensure your dataset is properly organized:"
    echo "  YellowCert/"
    echo "  ├── train/"
    echo "  │   ├── images/"
    echo "  │   └── labels/"
    echo "  ├── valid/"
    echo "  │   ├── images/"
    echo "  │   └── labels/"
    echo "  ├── test/"
    echo "  │   ├── images/"
    echo "  │   └── labels/"
    echo "  └── data.yaml"
    exit 1
fi

echo "✓ All required directories found"
echo ""

# Count images
train_count=$(find train/images -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) 2>/dev/null | wc -l | tr -d ' ')
valid_count=$(find valid/images -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) 2>/dev/null | wc -l | tr -d ' ')
test_count=$(find test/images -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) 2>/dev/null | wc -l | tr -d ' ')

echo "Dataset Summary:"
echo "  Training images: $train_count"
echo "  Validation images: $valid_count"
echo "  Test images: $test_count"
echo "  Total: $((train_count + valid_count + test_count))"
echo ""

# Create ZIP file
output_file="yellowcert_dataset.zip"

if [ -f "$output_file" ]; then
    echo "⚠️  Warning: $output_file already exists"
    read -p "Do you want to overwrite it? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi
    rm "$output_file"
fi

echo "Creating ZIP archive..."
echo "(This may take a few minutes depending on dataset size)"
echo ""

# Create ZIP with progress
zip -r "$output_file" train/ valid/ test/ data.yaml -x "*.DS_Store" "*__pycache__*" "*.cache" 2>&1 | \
    grep -i "adding" | head -20

echo ""
echo "=========================================="
echo "✓ Dataset prepared successfully!"
echo "=========================================="
echo ""

# Get file size
file_size=$(du -h "$output_file" | cut -f1)
echo "📦 File: $output_file"
echo "📏 Size: $file_size"
echo ""

echo "Next steps:"
echo "1. Go to https://colab.research.google.com/"
echo "2. Upload YellowCert_Training_Colab.ipynb"
echo "3. Enable GPU: Runtime → Change runtime type → T4 GPU"
echo "4. In Section 2, upload $output_file"
echo "5. Run the cells and start training!"
echo ""
echo "📖 For detailed instructions, see COLAB_TRAINING_GUIDE.md"
echo ""
echo "Happy training! 🚀"
