# PDF to Markdown Converter

This Streamlit application converts PDF files to Markdown format using the LlamaParse API. It provides a simple web interface for users to upload PDF files and receive the converted Markdown content.

## Features

- Upload PDF files
- Convert PDF to Markdown using LlamaParse API
- Preview converted Markdown content
- Download converted Markdown file

## Requirements

- Python 3.6+
- Streamlit
- LlamaParse
- A valid LlamaParse API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pdf-to-markdown-converter.git
   cd pdf-to-markdown-converter
   ```

2. Install the required packages:
   ```
   pip install streamlit llama-parse
   ```

3. Run the Streamlit app:
   ```
   streamlit run main_03.py
   ```

## Usage

1. Start the Streamlit app by running `streamlit run main_03.py`.
2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).
3. Enter your LlamaParse API key in the provided input field.
4. Upload a PDF file using the file uploader.
5. Wait for the conversion process to complete.
6. Preview the converted Markdown content.
7. Download the converted Markdown file using the "Download Markdown" button.

## Note

This application requires a valid LlamaParse API key to function. Make sure you have an active subscription or trial account with LlamaParse to use this converter.

## License

[Specify the license here, e.g., MIT, GPL, etc.]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This application uses the LlamaParse API for PDF to Markdown conversion. Please ensure you comply with LlamaParse's terms of service and have the necessary rights to convert and use the content of the PDF files you upload.
