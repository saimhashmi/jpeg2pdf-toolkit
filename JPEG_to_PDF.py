import os
import tkinter
from tkinter import filedialog
from PIL import Image, ImageOps
from pypdf import PdfWriter
import pikepdf

root = tkinter.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(title="select the folder")

def get_files(folder_path, file_type):
    if not folder_path:
        print("❌ No folder selected.")
    else:
        img_files = [file for file in os.listdir(folder_path) if file.lower().endswith((file_type))]
    print(folder_path, img_files)
    return img_files

def JPEG_to_PDF(folder_path, img_file):
    file = folder_path + "/" + img_file
    img = ImageOps.exif_transpose(Image.open(file)).convert("RGB")
    try:
        img.save(file.replace(".jpeg", ".pdf"))
        print(f"image {img_file} successfully converted to PDF {img_file.replace(".jpeg", ".pdf")}")
    except Exception:
        print(f"An unexpected error occurred: {Exception}")

def merge_pdfs(folder_path, pdf_files, output_name="merged.pdf"):
    """Merge all PDFs in folder into one file"""
    if not pdf_files:
        print("⚠️ No PDF files found to merge.")
        return

    merger = PdfWriter()
    for pdf_file in pdf_files:
        merger.append(os.path.join(folder_path, pdf_file))

    output_path = os.path.join(folder_path, output_name)
    with open(output_path, "wb") as f_out:
        merger.write(f_out)

    print(f"📕 Merged PDF saved as {output_path}")
    return output_path

# def lossless_PDF_Compression(file_path):
#     pdf = pikepdf.open(file_path)
#     pdf.save("lossless-compressed.pdf", object_stream_mode=pikepdf.ObjectStreamMode.generate, linearize=True)
#     pdf.close()

img_files = get_files(folder_path, file_type="'.jpg', '.jpeg'")
pdf_files = get_files(folder_path, file_type=".pdf")

for img_file in img_files:
    JPEG_to_PDF(folder_path, img_file)

merged_pdf = merge_pdfs(folder_path, pdf_files)

# pdf_for_compression = merged_pdf
# lossless_PDF_Compression(pdf_for_compression)
