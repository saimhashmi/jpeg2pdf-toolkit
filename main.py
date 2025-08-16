import os
import tkinter
from tkinter import filedialog
from PIL import Image, ImageOps
from pypdf import PdfWriter  # For merging PDFs
import pikepdf               # For lossless PDF optimization

# Hide the main Tkinter window (only want file dialog, not empty window)
root = tkinter.Tk()
root.withdraw()

# Prompt user to select a folder containing images or PDFs
folder_path = filedialog.askdirectory(title="Select the folder")

def get_files(folder_path, file_type):
    """
    Get list of files of a given type from the folder.
    Args:
        folder_path (str): path to folder
        file_type (tuple): extensions to filter (e.g., ('.jpg', '.jpeg'))
    Returns:
        list: list of matching files
    """
    if not folder_path:
        print("❌ No folder selected.")
        return []
    files = [file for file in os.listdir(folder_path) if file.lower().endswith(file_type)]
    print(f"📂 Found {len(files)} files in {folder_path}: {files}")
    return files

def JPEG_to_PDF(folder_path, img_file):
    """
    Convert a single JPEG/JPG file to PDF.
    Args:
        folder_path (str): path to folder
        img_file (str): image filename
    """
    file = os.path.join(folder_path, img_file)
    # Fix orientation using EXIF metadata, convert to RGB
    img = ImageOps.exif_transpose(Image.open(file)).convert("RGB")
    output_file = file.rsplit(".", 1)[0] + ".pdf"
    try:
        img.save(output_file)
        print(f"✅ {img_file} → {os.path.basename(output_file)}")
    except Exception as e:
        print(f"⚠️ Error converting {img_file}: {e}")

def merge_pdfs(folder_path, pdf_files, output_name="merged.pdf"):
    """
    Merge multiple PDF files into one.
    Args:
        folder_path (str): path to folder
        pdf_files (list): list of PDF filenames
        output_name (str): name of output PDF
    """
    merger = PdfWriter()
    for pdf in pdf_files:
        merger.append(os.path.join(folder_path, pdf))
    output_path = os.path.join(folder_path, output_name)
    with open(output_path, "wb") as f_out:
        merger.write(f_out)
    print(f"📑 Merged PDF saved as {output_path}")
    return output_path

def compress_pdf(input_pdf, output_pdf="compressed.pdf"):
    """
    Optimize (lossless) a PDF using pikepdf.
    Args:
        input_pdf (str): path to input PDF
        output_pdf (str): path to output PDF
    """
    with pikepdf.open(input_pdf) as pdf:
        pdf.save(output_pdf, linearize=True)  # linearize = fast web view
    print(f"🔧 Compressed PDF saved as {output_pdf}")

# --- MAIN EXECUTION ---
# Step 1: Convert images to PDFs
img_files = get_files(folder_path, ('.jpg', '.jpeg'))
for img_file in img_files:
    JPEG_to_PDF(folder_path, img_file)

# Step 2: Merge PDFs
pdf_files = get_files(folder_path, ('.pdf',))
merged_pdf = merge_pdfs(folder_path, pdf_files)

# Step 3: Compress merged PDF (lossless)
compress_pdf(merged_pdf, os.path.join(folder_path, "lossless-compressed.pdf"))
