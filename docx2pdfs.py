"""
Name: docx2pdfs.py
Description: Batch convert docx files to pdf files.
Author: hdaojin
Version: 1.0.0
created: 2022-11-30
updated: 2022-11-30
"""

from pathlib import Path
from docx2pdf import convert
import click


@click.command()
@click.argument('dir', type=click.Path(exists=True, path_type=Path), default='.')
@click.option('--output', '-o', type=click.Path(exists=True, path_type=Path))

def convert_docx_to_pdf(dir, output=None):
    # for docx_file in list(dir.rglob('*.docx')):
    for docx_file in dir.rglob('*.docx'):
        if not output:
            output = docx_file.parent
        pdf_file = output / docx_file.with_suffix('.pdf').name
        convert(docx_file, pdf_file)
        print(f'Convert {docx_file} to {pdf_file} successfully.')


if __name__ == "__main__":
    convert_docx_to_pdf()

# Importent: You just need to install docx2pdf and run docx2pdf.exe. ^_^ 