# Quick Start Guide

This guide helps you get started with the granite-docling-258M-mlx environment quickly.

## Prerequisites Check

Before starting, verify:
- [ ] Python 3.8 or higher installed
- [ ] pip package manager available
- [ ] Git installed
- [ ] Terminal/command line access

## Step-by-Step Setup

### 1. Clone the Repository (if not already done)

```bash
git clone https://github.com/TioSavich/Text_Processing.git
cd Text_Processing
```

### 2. Test Your Environment

Run the test script to verify your setup:

```bash
python3 test_environment.py
```

This will check:
- Python version compatibility
- Required files existence
- Package installation status

### 3. Automated Setup (Recommended)

Use the provided setup script:

```bash
./setup.sh
```

This will:
1. Create a Python virtual environment
2. Activate the environment
3. Upgrade pip to the latest version
4. Install all required dependencies

**Note**: The installation may take 5-10 minutes depending on your internet connection.

### 4. Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### 5. Verify Installation

After installation completes, verify everything is working:

```bash
python3 test_environment.py
```

You should see all packages marked with ✓.

## Your First Document Conversion

### Basic Usage

1. **Prepare a test document** (PDF or DOCX file)

2. **Activate the virtual environment** (if not already active):
   ```bash
   source venv/bin/activate
   ```

3. **Run the example script**:
   ```bash
   python example_granite_docling.py your_document.pdf
   ```

4. **Check the output**: The converted file will be saved in the current directory.

### Advanced Usage

Convert to HTML:
```bash
python example_granite_docling.py document.pdf html
```

Convert to JSON:
```bash
python example_granite_docling.py document.pdf json
```

Convert to Markdown (default):
```bash
python example_granite_docling.py document.pdf markdown
```

## Understanding the Output

The model will generate output in your chosen format:

- **Markdown (.md)**: Text-based format with formatting markers
- **HTML (.html)**: Web-ready format with styling
- **JSON (.json)**: Structured data format for programmatic use

## Common First-Time Issues

### Issue: "Command not found: ./setup.sh"

**Solution**: Make the script executable:
```bash
chmod +x setup.sh
./setup.sh
```

### Issue: "No module named 'docling'"

**Solution**: Activate the virtual environment:
```bash
source venv/bin/activate
```

### Issue: "File not found: your_document.pdf"

**Solution**: Ensure the document path is correct:
```bash
# Use absolute path
python example_granite_docling.py /full/path/to/document.pdf

# Or relative path from current directory
python example_granite_docling.py ./documents/document.pdf
```

### Issue: Installation takes too long or times out

**Solution**: 
- Check your internet connection
- Try installing with increased timeout:
  ```bash
  pip install -r requirements.txt --timeout=300
  ```
- Install packages individually if needed

## Platform-Specific Notes

### macOS (Apple Silicon M1/M2/M3)

- MLX will provide optimal performance
- Installation is straightforward
- All features fully supported

### macOS (Intel)

- MLX may not be fully optimized
- Will use CPU-based processing
- All features still available, just slower

### Linux

- MLX support is limited
- Will fall back to CPU processing
- All core features still work
- May need additional system dependencies

### Windows

- MLX is not natively supported
- Use WSL2 (Windows Subsystem for Linux) for best experience
- Or accept CPU-based processing

## Next Steps

After successful setup:

1. **Read the full README.md** for detailed usage information
2. **Check ARCHITECTURE.md** to understand how it works
3. **Experiment with different document types**
4. **Explore output format options**
5. **Integrate into your workflow**

## Getting Help

If you encounter issues:

1. Run `python test_environment.py` to diagnose problems
2. Check error messages carefully
3. Verify virtual environment is activated
4. Review installation logs
5. Open an issue on GitHub with details

## Success Checklist

You're ready when:
- [ ] `test_environment.py` shows all packages installed
- [ ] You can activate the virtual environment
- [ ] Example script runs without import errors
- [ ] You've successfully converted a test document
- [ ] Output files are generated correctly

Congratulations! You now have a working granite-docling-258M-mlx environment!
