from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

@app.route("/", methods=["GET"])
def get_transcript_summary():
    video_url = 'BmYv8XGl-YU'

    try:
        # Get the transcript for the provided YouTube video URL
        transcript = YouTubeTranscriptApi.get_transcript(video_url)

        # Extract text from the transcript
        text_paragraph = "".join([item['text'] for item in transcript])

        # Split the text into chunks
        chunk_size = 1024
        chunks = [text_paragraph[i:i + chunk_size] for i in range(0, len(text_paragraph), chunk_size)]

        # Initialize a list to store summaries
        summaries = []

        # Summarize each chunk using the model
        for chunk in chunks:
            summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # Combine the summaries if needed
        combined_summary = " ".join(summaries)

        return jsonify({
            "transcript": text_paragraph,
            "summary": combined_summary
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
