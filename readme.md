YouTube Transcriber and Summarizer
==================================

A Flask-based API to extract, transcribe, and summarize content from YouTube videos, integrated with Hugging Face's transformers. Includes a basic Google Chrome extension for ease of use.

Features
--------
- Extracts video transcripts using `youtube-transcript-api`.
- Summarizes the transcript using a pre-trained Hugging Face summarization model.
- Simple REST API to integrate into other applications.
- Basic Google Chrome extension for seamless use.


Requirements
------------
The following Python libraries are required:
- accelerate==0.22.0
- blinker==1.6.2
- certifi==2023.7.22
- charset-normalizer==3.2.0
- click==8.1.7
- colorama==0.4.6
- filelock==3.12.4
- Flask==2.3.3
- fsspec==2023.9.0
- huggingface-hub==0.17.1
- idna==3.4
- importlib-metadata==6.8.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- mpmath==1.3.0
- networkx==3.1
- numpy==1.25.2
- packaging==23.1
- psutil==5.9.5
- PyYAML==6.0.1
- regex==2023.8.8
- requests==2.31.0
- safetensors==0.3.3
- sympy==1.12
- tokenizers==0.13.3
- torch==2.0.1
- tqdm==4.66.1
- transformers==4.33.1
- typing_extensions==4.7.1
- urllib3==2.0.4
- Werkzeug==2.3.7
- youtube-transcript-api==0.6.1
- zipp==3.16.2

Installation
------------
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-transcriber-summarizer.git
   cd youtube-transcriber-summarizer

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

Running the Application:
------------------------
1. Start the Flask server:
   python app.py


2.Access the API endpoint in your browser or via tools like Postman:
  http://localhost:5000/api/summarize?youtube_url=YOUR-YOUTUBE-ID-OR-URL

Project Structure:
-----------------
plaintext
Copy code
├── app.py                   # Main Flask application
├── requirements.txt         # Dependencies list
├── static/                  # Static files for web UI (if applicable)
├── templates/               # HTML templates for Flask
├── chrome-extension/        # Chrome extension source code
├── README.txt               # Project documentation

Acknowledgments:
---------------

1. Crio.io for the development framework.
2. Hugging Face for the summarization model.
3. YouTube Transcript API for transcript extraction.
 