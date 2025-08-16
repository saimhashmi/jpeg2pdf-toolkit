# PDF Compression Utility

A simple Python utility to:
1. Convert JPEG/JPG images to PDF
2. Merge multiple PDFs into one
3. Perform **lossless compression** of the final PDF

---

## 🚀 Features
- Select a folder with JPEGs/PDFs using a file dialog
- Automatically converts JPEGs to PDFs
- Merges all PDFs in the folder into one
- Compresses the merged PDF using [pikepdf](https://pikepdf.readthedocs.io/)

---

## 📦 Installation
1. Clone this repository
   cd into the directory
   
2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows

3. Install dependencies
   pip install -r requirements.txt