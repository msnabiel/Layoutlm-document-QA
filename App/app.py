import streamlit as st
from transformers import pipeline
import requests
from PIL import Image
from io import BytesIO

# Initialize the pipeline for document question answering
nlp = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa",
    device=0  # Specify the GPU device if available (optional)
)

# Define a function to perform QA and display results
def perform_question_answering(file_input, question):
    try:
        if isinstance(file_input, str):  # If input is a URL
            response = requests.get(file_input)
            file_input = BytesIO(response.content)
            image = Image.open(file_input)
        elif isinstance(file_input, BytesIO):  # If input is BytesIO (PIL image)
            image = Image.open(file_input)
        elif isinstance(file_input, Image.Image):  # If input is already a PIL image
            image = file_input
        else:
            st.error("Unsupported file format. Please provide an image URL or upload a supported file.")
            return None
        
        result = nlp(image, question)
        
        # Handle cases where result is a list of answers
        if isinstance(result, list):
            answers = []
            for res in result:
                answers.append(f"Answer: {res['answer']}, Confidence Score: {res['score']:.4f}")
            return answers
        elif isinstance(result, dict):  # Handle case where result is a single answer
            return [f"Answer: {result['answer']}, Confidence Score: {result['score']:.4f}"]
        else:
            st.error("Unexpected result format from model.")
            return None

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# Define prompts for suggestions
next_prompt_suggestions = [
    "What is the total amount due?",
    "Who is the billing address for?",
    "What are the terms of payment?"
]

# Streamlit app layout
def main():
    st.title("Document QA with LayoutLM")
    
    st.sidebar.title("Next Prompt Suggestions")
    selected_prompt = st.sidebar.selectbox("Select a prompt", next_prompt_suggestions)
    
    st.markdown("---")
    st.header("Upload Your Document or Image")
    
    file_upload = st.file_uploader("Upload a file (PDF, image, etc.)", type=["pdf", "png", "jpg", "jpeg"])
    if file_upload is not None:
        st.image(file_upload, caption="Uploaded Image", use_column_width=True)
        
        question = st.text_input("Enter your question:")
        if st.button("Ask"):
            st.markdown("### Answer:")
            with st.spinner('Searching for answer...'):
                result = perform_question_answering(file_upload, question)
                if result:
                    for answer in result:
                        st.write(answer)
                else:
                    st.error("Failed to get answer.")
    
if __name__ == '__main__':
    main()
