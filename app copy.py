import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "deepdoc"))

import streamlit as st
from deepdoc.parser import PdfParser, PlainParser, DocxParser, ExcelParser, PptParser, HtmlParser, JsonParser, MarkdownParser, TxtParser
from deepdoc.vision import OCR, LayoutRecognizer, TableStructureRecognizer

st.title("DeepDoc Parser and Vision Demo")

# 文件上传
uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "xlsx", "ppt", "html", "json", "md", "txt", "png"])

if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Parser 功能
    if st.button("Parse PDF"):
        parser = PdfParser()
        result = parser(file_path)
        st.write("PDF Result:", result)

    if st.button("Parse DOCX"):
        parser = DocxParser()
        sections, tables = parser(file_path)
        st.write("DOCX Sections:", sections)
        st.write("DOCX Tables:", tables)

    if st.button("Parse Excel"):
        parser = ExcelParser()
        result = parser(file_path)
        st.write("Excel Result:", result)

    # Vision 功能
    if st.button("Run OCR"):
        ocr = OCR()
        result = ocr([file_path])
        st.write("OCR Result:", result)

    if st.button("Recognize Layout"):
        recognizer = LayoutRecognizer()
        result = recognizer([file_path], thr=0.2)
        st.write("Layout Result:", result)

    if st.button("Recognize Table"):
        recognizer = TableStructureRecognizer()
        result = recognizer([file_path], thr=0.2)
        st.write("Table Result:", result)

    # 清理临时文件
    os.remove(file_path)

if __name__ == "__main__":
    st.write("Upload a file to start processing.")