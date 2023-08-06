# -*- coding=utf-8 -*-
from IPython.display import display, HTML
import mammoth


def display_docx(docx_file_path):
    with open(docx_file_path, "rb") as f:
        result = mammoth.convert_to_html(f)
        display(HTML(result.value))
