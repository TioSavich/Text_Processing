#!/usr/bin/env python3
"""
Demo script showing a complete workflow with granite-docling-258M-mlx.

This demonstrates:
1. Batch processing multiple documents
2. Different output formats
3. Error handling
4. Progress tracking
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import docling
        return True
    except ImportError:
        print("Error: Required dependencies not installed.")
        print("\nPlease install dependencies first:")
        print("  1. Activate virtual environment: source venv/bin/activate")
        print("  2. Install requirements: pip install -r requirements.txt")
        print("\nOr run the setup script: ./setup.sh")
        return False

def process_single_document(input_path: str, output_format: str = "markdown", output_dir: str = "."):
    """
    Process a single document.
    
    Args:
        input_path: Path to input document
        output_format: Desired output format
        output_dir: Directory to save output
    
    Returns:
        Path to output file or None on error
    """
    from docling.document_converter import DocumentConverter
    
    try:
        print(f"Processing: {input_path}")
        
        # Initialize converter
        converter = DocumentConverter()
        
        # Convert document
        result = converter.convert(input_path)
        
        # Export to desired format
        if output_format.lower() == "markdown":
            content = result.document.export_to_markdown()
            ext = "md"
        elif output_format.lower() == "html":
            content = result.document.export_to_html()
            ext = "html"
        elif output_format.lower() == "json":
            import json
            content = json.dumps(result.document.export_to_dict(), indent=2)
            ext = "json"
        else:
            raise ValueError(f"Unsupported format: {output_format}")
        
        # Create output path
        input_name = Path(input_path).stem
        output_path = Path(output_dir) / f"{input_name}_converted.{ext}"
        
        # Save output
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"  ✓ Saved to: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None

def process_batch(input_paths: List[str], output_format: str = "markdown", output_dir: str = "."):
    """
    Process multiple documents in batch.
    
    Args:
        input_paths: List of input document paths
        output_format: Desired output format
        output_dir: Directory to save outputs
    """
    # Create output directory if needed
    os.makedirs(output_dir, exist_ok=True)
    
    successful = 0
    failed = 0
    
    print(f"\nProcessing {len(input_paths)} document(s)...")
    print(f"Output format: {output_format}")
    print(f"Output directory: {output_dir}\n")
    
    for i, input_path in enumerate(input_paths, 1):
        print(f"[{i}/{len(input_paths)}] ", end="")
        
        result = process_single_document(input_path, output_format, output_dir)
        
        if result:
            successful += 1
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Batch processing complete:")
    print(f"  ✓ Successful: {successful}")
    if failed > 0:
        print(f"  ✗ Failed: {failed}")
    print(f"{'='*60}\n")

def find_documents(directory: str, extensions: List[str] = None) -> List[str]:
    """
    Find all documents in a directory with given extensions.
    
    Args:
        directory: Directory to search
        extensions: List of file extensions (e.g., ['.pdf', '.docx'])
    
    Returns:
        List of document paths
    """
    if extensions is None:
        extensions = ['.pdf', '.docx', '.pptx', '.html']
    
    documents = []
    for ext in extensions:
        documents.extend(Path(directory).glob(f"*{ext}"))
    
    return [str(doc) for doc in sorted(documents)]

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Demo: Batch process documents with granite-docling-258M-mlx",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single file
  %(prog)s document.pdf
  
  # Process multiple files
  %(prog)s doc1.pdf doc2.docx doc3.pdf
  
  # Process all PDFs in a directory
  %(prog)s --directory ./documents --extensions .pdf
  
  # Convert to HTML instead of Markdown
  %(prog)s document.pdf --format html
  
  # Save outputs to specific directory
  %(prog)s document.pdf --output ./converted
        """
    )
    
    parser.add_argument(
        'files',
        nargs='*',
        help='Document files to process'
    )
    
    parser.add_argument(
        '-d', '--directory',
        help='Process all documents in this directory'
    )
    
    parser.add_argument(
        '-e', '--extensions',
        nargs='+',
        default=['.pdf', '.docx', '.pptx'],
        help='File extensions to process (default: .pdf .docx .pptx)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['markdown', 'html', 'json'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Collect files to process
    files_to_process = []
    
    if args.directory:
        print(f"Searching for documents in: {args.directory}")
        files_to_process = find_documents(args.directory, args.extensions)
        if not files_to_process:
            print(f"No documents found with extensions: {args.extensions}")
            sys.exit(1)
        print(f"Found {len(files_to_process)} document(s)")
    elif args.files:
        files_to_process = args.files
    else:
        parser.print_help()
        sys.exit(0)
    
    # Validate files exist
    missing_files = [f for f in files_to_process if not os.path.exists(f)]
    if missing_files:
        print("Error: The following files do not exist:")
        for f in missing_files:
            print(f"  - {f}")
        sys.exit(1)
    
    # Process documents
    process_batch(files_to_process, args.format, args.output)

if __name__ == "__main__":
    main()
