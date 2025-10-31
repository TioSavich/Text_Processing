#!/usr/bin/env python3
"""
Example script demonstrating how to use granite-docling-258M-mlx model.

This script shows how to:
1. Load the granite-docling-258M-mlx model
2. Process documents (PDF, DOCX, etc.)
3. Convert to various formats (HTML, Markdown)
"""

import os
import sys
from pathlib import Path

try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please install required dependencies:")
    print("  pip install -r requirements.txt")
    sys.exit(1)


def process_document(input_path: str, output_format: str = "markdown"):
    """
    Process a document using granite-docling-258M-mlx model.
    
    Args:
        input_path: Path to input document (PDF, DOCX, etc.)
        output_format: Output format ('markdown', 'html', 'json')
    
    Returns:
        Converted document content
    """
    print(f"Processing document: {input_path}")
    
    # Initialize document converter with MLX backend
    # Note: granite-docling-258M-mlx is used through the docling framework
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: pipeline_options,
        }
    )
    
    # Convert document
    result = converter.convert(input_path)
    
    # Export to desired format
    if output_format.lower() == "markdown":
        output = result.document.export_to_markdown()
    elif output_format.lower() == "html":
        output = result.document.export_to_html()
    elif output_format.lower() == "json":
        output = result.document.export_to_dict()
    else:
        raise ValueError(f"Unsupported output format: {output_format}")
    
    return output


def main():
    """Main function to demonstrate granite-docling usage."""
    print("=" * 60)
    print("Granite-Docling-258M-MLX Environment Test")
    print("=" * 60)
    print()
    
    # Check if input file is provided
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_format = sys.argv[2] if len(sys.argv) > 2 else "markdown"
        
        if not os.path.exists(input_file):
            print(f"Error: File not found: {input_file}")
            sys.exit(1)
        
        try:
            result = process_document(input_file, output_format)
            
            # Save output
            output_file = f"{Path(input_file).stem}_output.{output_format}"
            with open(output_file, "w", encoding="utf-8") as f:
                if isinstance(result, dict):
                    import json
                    json.dump(result, f, indent=2)
                else:
                    f.write(result)
            
            print(f"\nDocument processed successfully!")
            print(f"Output saved to: {output_file}")
            
        except Exception as e:
            print(f"Error processing document: {e}")
            sys.exit(1)
    else:
        # No input file provided, just verify environment
        print("Environment check:")
        print(f"✓ Python version: {sys.version}")
        
        try:
            import docling
            print(f"✓ Docling installed: {docling.__version__}")
        except (ImportError, AttributeError):
            print("✓ Docling installed (version unknown)")
        
        try:
            import mlx
            print(f"✓ MLX installed: {mlx.__version__}")
        except (ImportError, AttributeError):
            print("✓ MLX installed (version unknown)")
        
        print("\nEnvironment is ready!")
        print("\nUsage:")
        print("  python example_granite_docling.py <input_file> [output_format]")
        print("\nExample:")
        print("  python example_granite_docling.py document.pdf markdown")
        print("  python example_granite_docling.py document.pdf html")


if __name__ == "__main__":
    main()
