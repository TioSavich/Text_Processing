# Granite-Docling-258M-MLX Architecture

## Overview

This document describes the architecture and setup for calling the granite-docling-258M-mlx model for document processing.

## What is Granite-Docling-258M-MLX?

Granite-Docling is IBM's document understanding model optimized for the MLX framework. The "258M" refers to the model size (258 million parameters), and "MLX" indicates it's optimized for Apple's MLX framework, which provides efficient machine learning on Apple Silicon.

## Architecture Components

### 1. Core Framework: Docling

Docling is IBM's open-source document processing framework that provides:
- Document parsing and conversion
- OCR (Optical Character Recognition)
- Table structure recognition
- Layout analysis
- Multi-format support (PDF, DOCX, PPTX, HTML, etc.)

### 2. MLX Framework

MLX is Apple's machine learning framework optimized for Apple Silicon (M1/M2/M3 chips):
- Efficient neural network inference
- Optimized for ARM architecture
- Low memory footprint
- Fast execution on Apple hardware

### 3. Granite Model

The Granite-258M model provides:
- Advanced document understanding
- Text extraction and formatting
- Layout preservation
- Semantic understanding

## How It Works

```
┌─────────────────┐
│  Input Document │
│  (PDF/DOCX/etc) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Docling Core  │
│  - File parsing │
│  - Layout det.  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Granite-258M-MLX│
│  - OCR/Extract  │
│  - Understanding│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Output Format   │
│ (HTML/MD/JSON)  │
└─────────────────┘
```

## Environment Components

### Dependencies

1. **docling** (>=2.0.0)
   - Main framework for document processing
   - Handles document parsing and conversion
   - Coordinates the processing pipeline

2. **mlx** (>=0.19.0)
   - Apple's machine learning framework
   - Provides efficient model inference
   - Optimized for Apple Silicon

3. **mlx-lm** (>=0.18.0)
   - Language model support for MLX
   - Enables text understanding capabilities

4. **pypdf** (>=4.0.0)
   - PDF file handling
   - Low-level PDF operations

5. **python-docx** (>=1.0.0)
   - DOCX file processing
   - Microsoft Word document support

### File Structure

```
Text_Processing/
├── requirements.txt           # Python dependencies
├── setup.sh                   # Setup automation script
├── example_granite_docling.py # Usage example
├── test_environment.py        # Environment verification
├── ARCHITECTURE.md           # This file
├── README.md                 # User documentation
└── venv/                     # Virtual environment (created)
```

## Usage Flow

### 1. Environment Setup

```bash
./setup.sh
source venv/bin/activate
```

### 2. Document Processing

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("document.pdf")
markdown_output = result.document.export_to_markdown()
```

### 3. Output Generation

The model can generate multiple output formats:
- **Markdown**: Plain text with formatting
- **HTML**: Web-ready format
- **JSON**: Structured data for programmatic use

## Performance Considerations

### MLX Optimization

On Apple Silicon:
- Fast inference times
- Low memory usage
- Efficient batch processing

On x86/Linux:
- Falls back to CPU processing
- Slower but still functional
- May use alternative backends

### Best Practices

1. **Use virtual environments** to isolate dependencies
2. **Process in batches** for multiple documents
3. **Cache results** to avoid reprocessing
4. **Monitor memory** for large documents

## Model Details

### Capabilities

- **OCR**: Extract text from scanned documents
- **Layout Analysis**: Preserve document structure
- **Table Recognition**: Detect and extract tables
- **Multi-language**: Support for various languages
- **Format Preservation**: Maintain original formatting

### Limitations

- Model size (258M parameters) balances accuracy and speed
- Best performance on Apple Silicon with MLX
- May require significant memory for large documents
- Processing time varies with document complexity

## Extension Points

The environment can be extended to:
1. Add custom document processors
2. Integrate with different backends
3. Support additional output formats
4. Implement batch processing pipelines
5. Add API endpoints for remote processing

## Troubleshooting

### Common Issues

1. **MLX not available**: Falls back to CPU processing
2. **Memory errors**: Reduce batch size or document resolution
3. **Import errors**: Ensure virtual environment is activated
4. **Slow processing**: Check if MLX acceleration is enabled

### Solutions

- Verify Python version (3.8+)
- Check virtual environment activation
- Ensure all dependencies are installed
- Monitor system resources

## References

- [Docling Documentation](https://github.com/DS4SD/docling)
- [MLX Framework](https://github.com/ml-explore/mlx)
- [Granite Models](https://github.com/ibm-granite)
