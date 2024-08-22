import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt', quiet=True)

import streamlit as st
from llama_parse import LlamaParse
import tempfile
import os

st.set_page_config(page_title="PDF to Markdown Converter", page_icon="📄")

st.title("PDF to Markdown Converter")

# Get API key from user input
LLAMA_CLOUD_API_KEY = st.text_input("Enter your LlamaParse API key:", type="password")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None and LLAMA_CLOUD_API_KEY:
    # Set up LlamaParse
    parser = LlamaParse(result_type="markdown", api_key=LLAMA_CLOUD_API_KEY)

    # Create a temporary file to store the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Parse the PDF
    try:
        with st.spinner("Converting PDF to Markdown..."):
            documents = parser.load_data(tmp_file_path)

        # Extract markdown content from Document objects
        markdown_text = [doc.text for doc in documents]

        # Combine the markdown content into a single string
        markdown_string = "\n\n".join(markdown_text)

        st.success("Conversion complete!")

        # Display a preview of the Markdown
        st.subheader("Markdown Preview")
        st.markdown(markdown_string[:1000] + "..." if len(markdown_string) > 1000 else markdown_string)

        # Create download button
        st.download_button(
            label="Download Markdown",
            data=markdown_string,
            file_name="converted.md",
            mime="text/markdown",
        )

    except Exception as e:
        st.error(f"Error parsing the PDF: {str(e)}")
    finally:
        # Clean up the temporary file
        os.unlink(tmp_file_path)

elif uploaded_file is not None and not LLAMA_CLOUD_API_KEY:
    st.warning("Please enter your LlamaParse API key to convert the PDF.")

st.markdown("---")
st.markdown("This app uses LlamaParse to convert PDF files to Markdown format. Please ensure you have a valid API key.")
