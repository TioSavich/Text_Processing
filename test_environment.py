#!/usr/bin/env python3
"""
Test script to verify the granite-docling-258M-mlx environment setup.
This script can be run before or after installing dependencies.
"""

import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python version must be 3.8 or higher")
        return False

def check_venv():
    """Check if running in a virtual environment."""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    if in_venv:
        print("✓ Running in virtual environment")
        return True
    else:
        print("⚠ Not running in virtual environment (recommended)")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed."""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✓ {package_name} is installed")
        return True
    except ImportError:
        print(f"✗ {package_name} is not installed")
        return False

def check_files():
    """Check if required files exist."""
    import os
    required_files = [
        'requirements.txt',
        'setup.sh',
        'example_granite_docling.py',
        'README.md'
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✓ {filename} exists")
        else:
            print(f"✗ {filename} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all checks."""
    print("=" * 60)
    print("Granite-Docling-258M-MLX Environment Test")
    print("=" * 60)
    print()
    
    print("Checking environment setup...\n")
    
    # Check Python version
    check_python_version()
    print()
    
    # Check virtual environment
    check_venv()
    print()
    
    # Check required files
    print("Checking required files...")
    check_files()
    print()
    
    # Check for installed packages (optional)
    print("Checking installed packages (optional)...")
    packages_to_check = [
        ('docling', 'docling'),
        ('mlx', 'mlx'),
        ('mlx-lm', 'mlx_lm'),
        ('pypdf', 'pypdf'),
        ('python-docx', 'docx'),
        ('Pillow', 'PIL'),
    ]
    
    installed_count = 0
    for package_name, import_name in packages_to_check:
        if check_package(package_name, import_name):
            installed_count += 1
    
    print()
    print(f"Installed packages: {installed_count}/{len(packages_to_check)}")
    
    if installed_count == 0:
        print("\nℹ To install dependencies, run:")
        print("  ./setup.sh")
        print("  or")
        print("  pip install -r requirements.txt")
    elif installed_count == len(packages_to_check):
        print("\n✓ All packages are installed!")
        print("\nYou can now use the environment:")
        print("  python example_granite_docling.py <document.pdf>")
    else:
        print("\n⚠ Some packages are missing. Run:")
        print("  pip install -r requirements.txt")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
