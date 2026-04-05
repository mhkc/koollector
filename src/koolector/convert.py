"""Convert documents to markdown files."""

from docling.document_converter import DocumentConverter



def convert(source, format="markdown"):
    """Convert the input document to markdown format."""
    converter = DocumentConverter()
    doc = converter.convert(source).document