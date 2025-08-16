# Documentation - PDF Toolkit (WIP)

This document provides details on the internal structure and functionality of the PDF Toolkit.

---

## Overview
PDF Toolkit is a Python script designed to simplify PDF handling by:
1. Converting JPEG images to PDF.
2. Merging multiple PDFs into a single file.
3. (Planned) Compressing the final PDF to reduce file size.

---

## How It Works
- **Folder Selection**  
  The user selects a folder using a `tkinter` file dialog.  
- **File Detection**  
  The script identifies:
  - `.jpg` / `.jpeg` images
  - `.pdf` files  
- **JPEG → PDF Conversion**  
  Each JPEG is processed using `Pillow`. Orientation is corrected via `ImageOps.exif_transpose`.  
- **PDF Merging**  
  PDFs are merged with `pypdf.PdfMerger`.  
- **Compression (Planned)**  
  Future versions will optimize the merged PDF using `pikepdf` and/or external tools (e.g., Ghostscript).

---

## Current Limitations
- Compression not functional yet — merged PDFs remain the same size as input.
- Only JPEGs are supported as image inputs.
- The script is GUI-only (no CLI/automation yet).
- Output filename is fixed (`merged.pdf`).

---

## Dependencies
- **Pillow** → image handling (`pip install pillow`)  
- **pypdf** → PDF merging (`pip install pypdf`)  
- **pikepdf** → planned compression (`pip install pikepdf`)  

---

## Next Steps
- Implement true lossless compression (likely with Ghostscript or `qpdf` optimizations).
- Add CLI flags (`--merge`, `--compress`, `--split`).
- Expand input support (PNG, TIFF).
- Add output customization (filenames, destination folder).

---

## Example Workflow
1. Place your JPEGs and/or PDFs in a folder.
2. Run the script:
   ```bash
   python main.py
