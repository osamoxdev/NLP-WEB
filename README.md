
# NLP-WEB

NLP-WEB is a web application that integrates various Natural Language Processing (NLP) tasks, including text generation, sentiment analysis, fill-mask, machine translation, question answering, and text summarization. The application leverages pre-trained models from Hugging Face's Transformers library and is built using the Django web framework.

## Features

- **Text Generation**: Generate coherent and contextually relevant text based on user input.
- **Sentiment Analysis**: Determine the sentiment (positive, negative, neutral) of a given text.
- **Fill-Mask**: Predict masked words within a sentence to understand context.
- **Machine Translation**: Translate text between different languages.
- **Question Answering**: Provide accurate answers to user-posed questions based on context.
- **Text Summarization**: Generate concise summaries of longer texts.

## Installation

To set up the NLP-WEB application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/osamoxdev/NLP-WEB.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd NLP-WEB/NLP_WebApplication
   ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Usage

Once the application is running, you can access various NLP functionalities through the web interface:

- **Text Generation**: Input a prompt to generate text.
- **Sentiment Analysis**: Enter text to analyze its sentiment.
- **Fill-Mask**: Provide a sentence with a masked word to predict the missing word.
- **Machine Translation**: Input text to translate between supported languages.
- **Question Answering**: Ask a question based on a provided context.
- **Text Summarization**: Paste a long text to receive a concise summary.

## Dependencies

- **Django**: Web framework used for building the application.
- **Hugging Face Transformers**: Library for accessing pre-trained NLP models.
- **PyTorch**: Deep learning framework required for model operations.

Ensure that all dependencies listed in `requirements.txt` are installed in your virtual environment.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing access to a wide range of pre-trained NLP models.
- [Django](https://www.djangoproject.com/) for the robust web framework.
- [PyTorch](https://pytorch.org/) for the deep learning capabilities.

For more information, visit the [NLP-WEB GitHub Repository](https://github.com/osamoxdev/NLP-WEB). 
