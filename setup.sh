#!/bin/bash

# Setup script for granite-docling-258M-mlx environment
# This script creates a virtual environment and installs all dependencies

set -e

echo "Setting up granite-docling-258M-mlx environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

echo ""
echo "Setup complete! To use the environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the example, use:"
echo "  python example_granite_docling.py"
