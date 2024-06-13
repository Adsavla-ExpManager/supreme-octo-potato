# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pytesseract pdf2image streamlit

# Install Tesseract OCR and poppler-utils
RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

# Set the path to the Tesseract library executable file
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/4.00/tessdata/

# Set the Streamlit port
ENV PORT 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "your_script.py"]
