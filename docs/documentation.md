### PDF Compression Utility — Documentation

## Functions

### `get_files(folder_path, file_type)`
Scans the folder for files with matching extensions.

- **Args**:
  - `folder_path (str)` → Folder path
  - `file_type (tuple)` → File extensions (e.g., `('.jpg', '.jpeg')`)
- **Returns**: `list` of matching files

---

### `JPEG_to_PDF(folder_path, img_file)`
Converts a single image into a PDF.

- Corrects EXIF orientation
- Saves as `<filename>.pdf`

---

### `merge_pdfs(folder_path, pdf_files, output_name="merged.pdf")`
Merges multiple PDF files into one single PDF.

- **Args**:
  - `folder_path (str)`
  - `pdf_files (list)`
  - `output_name (str)` → Defaults to `merged.pdf`
- **Returns**: Path to merged PDF

---

### `compress_pdf(input_pdf, output_pdf="compressed.pdf")`
Optimizes a PDF file using pikepdf (lossless).

- **Args**:
  - `input_pdf (str)`
  - `output_pdf (str)` → Defaults to `compressed.pdf`
- Uses `linearize=True` for web optimization

---

## Workflow
1. User selects a folder  
2. JPEGs → PDFs  
3. PDFs merged  
4. Merged PDF losslessly compressed  

---

## Current Limitations
- Works only with `.jpg`, `.jpeg`, `.pdf`  
- Lossless compression only (no significant size reduction for images)  
- No parallel processing (large folders may be slow)  
