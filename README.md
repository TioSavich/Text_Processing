# Text_Processing

Repository for building a pdf -> html, docling, markdown conversion system using granite-docling-258M-mlx.

## Overview

This repository provides an environment to use the granite-docling-258M-mlx model for document processing. The model can convert various document formats (PDF, DOCX, etc.) into HTML, Markdown, or JSON formats.

## Features

- **Document Conversion**: Convert PDF and DOCX files to HTML, Markdown, or JSON
- **OCR Support**: Extract text from scanned documents
- **Table Structure Recognition**: Preserve table structures during conversion
- **MLX Optimization**: Uses MLX-optimized granite-docling model for efficient processing

## Prerequisites

- Python 3.8 or higher
- macOS (for MLX support) or Linux
- pip package manager

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/TioSavich/Text_Processing.git
cd Text_Processing
```

### 2. Set Up the Environment

Run the setup script to create a virtual environment and install dependencies:

```bash
./setup.sh
```

This will:
- Create a Python virtual environment
- Install all required dependencies including docling and MLX
- Set up the granite-docling-258M-mlx environment

### 3. Activate the Virtual Environment

```bash
source venv/bin/activate
```

## Usage

### Basic Usage

Process a document with default settings (converts to Markdown):

```bash
python example_granite_docling.py document.pdf
```

### Convert to Different Formats

```bash
# Convert to Markdown
python example_granite_docling.py document.pdf markdown

# Convert to HTML
python example_granite_docling.py document.pdf html

# Convert to JSON
python example_granite_docling.py document.pdf json
```

### Check Environment

To verify the environment is set up correctly:

```bash
python example_granite_docling.py
```

### Batch Processing

Process multiple documents at once:

```bash
# Process all PDFs in a directory
python batch_process.py --directory ./documents --format markdown

# Process specific files
python batch_process.py file1.pdf file2.docx file3.pdf --output ./converted

# Process all documents with specific extensions
python batch_process.py --directory ./docs --extensions .pdf .docx --format html
```

Run with `--help` for more options:

```bash
python batch_process.py --help
```

## Project Structure

```
Text_Processing/
├── README.md                      # This file
├── QUICKSTART.md                  # Quick start guide
├── ARCHITECTURE.md                # Architecture documentation
├── requirements.txt               # Python dependencies
├── setup.sh                       # Environment setup script
├── example_granite_docling.py     # Single document example
├── batch_process.py               # Batch processing script
├── test_environment.py            # Environment verification
├── .gitignore                     # Git ignore rules
└── venv/                          # Virtual environment (created by setup.sh)
```

## Dependencies

The main dependencies are:

- **docling** (>=2.0.0): Core document processing framework
- **mlx** (>=0.19.0): Apple MLX framework for optimized model inference
- **mlx-lm** (>=0.18.0): MLX language model support
- **pypdf** (>=4.0.0): PDF processing
- **python-docx** (>=1.0.0): DOCX file handling
- **markdown** (>=3.5.0): Markdown processing

See `requirements.txt` for the complete list.

## Manual Installation

If you prefer to install dependencies manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Troubleshooting

### MLX Not Available

MLX is primarily designed for Apple Silicon (M1/M2/M3) Macs. If you're on a different platform, the docling library will fall back to CPU-based processing.

### Module Import Errors

If you encounter import errors, ensure you've activated the virtual environment:

```bash
source venv/bin/activate
```

### Document Processing Errors

- Ensure your input file exists and is readable
- Check that the file format is supported (PDF, DOCX)
- For scanned PDFs, OCR processing may take longer

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source. Please check the repository for license information.
