# PDF Toolkit (WIP)

A simple Python utility to:
- Convert JPEG images to PDF
- Merge multiple PDFs into one
- (Planned) Apply **lossless PDF compression** to reduce file size

⚠️ **Note:** Compression is not fully implemented yet. Current compression attempts via `pikepdf` do not reduce size meaningfully. Future updates will explore advanced optimization techniques.

---

## Features
- Convert `.jpg` and `.jpeg` images to `.pdf`
- Merge multiple PDFs into a single file
- GUI folder selection via `tkinter`
- Clean, modular code with comments
- Easy to extend (planned features: compression, splitting, watermarking)

---

## Limitations
- **Compression is incomplete** → current output files are not reduced in size.
- Only supports `.jpg` and `.jpeg` inputs (not `.png` or `.tiff` yet).
- Orientation fixes depend on EXIF data — may not always behave as expected.
- No CLI arguments (GUI only at the moment).
- Windows tested only — Linux/macOS compatibility not confirmed.

---

## Dependencies
Install the required libraries:

```bash
pip install pillow pypdf pikepdf