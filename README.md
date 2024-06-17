# Document QA with LayoutLM Impira

This Streamlit application allows users to perform question answering on documents and images using the LayoutLM model. Users can upload a document or image file and ask specific questions related to the content. Additionally, prompt suggestions are available to help users formulate questions quickly.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Support](#file-support)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/msnabiel/Layoutlm-document-QA.git
   cd Layoutlm-document-QA
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you have Python installed along with pip.

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Access the application through the URL provided by Streamlit in your terminal.

3. Upload a document or image file (PDF, PNG, JPG, JPEG) using the file uploader.

4. Enter your question in the text input field.

5. Click the "Ask" button to submit your question and see the model's answer.

## Features

- **File Upload:** Supports uploading PDF, PNG, JPG, and JPEG files for document analysis.
- **Question Input:** Users can enter custom questions related to the uploaded document or image.
- **Prompt Suggestions:** Sidebar provides quick prompts to assist in formulating questions.
- **Real-time Answering:** Displays answers from the LayoutLM model with confidence scores.
- **Error Handling:** Provides error messages for unsupported file formats or processing issues.

## File Support

Supported file formats for uploading:

- PDF files containing text or images.
- Image files (PNG, JPG, JPEG) of documents or screenshots.

## Troubleshooting

- **Unsupported File Formats:** If you encounter an error stating "Unsupported file format," ensure you are uploading a supported file type.
- **Model Errors:** If the model encounters issues while processing the document or image, an error message will be displayed. Check the error details for troubleshooting steps.

Certainly! Adding licensing information and collaboration details to your README file is important for clarity on usage rights and potential contributions. Here’s an updated version of your README.md file that includes the MIT license and collaboration information:

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository and create your branch (`git checkout -b feature/your-feature`).
2. Make your changes and commit them (`git commit -am 'Add some feature'`).
3. Push to the branch (`git push origin feature/your-feature`).
4. Create a new Pull Request.

Please ensure your pull request adheres to the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) code of conduct.

## Credits

- **LayoutLM Model:** Powered by Hugging Face Transformers library.
- **Streamlit:** Used for creating interactive and user-friendly web applications.

