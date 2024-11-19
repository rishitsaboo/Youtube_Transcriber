from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

@app.route("/api/summarize", methods=["GET"])
def summarize_youtube_video():
    # Get the YouTube URL from the query parameters
    youtube_url = request.args.get("youtube_url")

    try:
        # Extract the video ID from the YouTube URL
        video_id = get_video_id(youtube_url)

        # Get the transcript for the provided YouTube video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

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

def get_video_id(youtube_url):
    # Extract the video ID from a YouTube URL
    parts = youtube_url.split("?v=BmYv8XGl-YU")
    if len(parts) > 1:
        video_id = parts[1]
        return video_id
    else:
        return youtube_url  # Handle the case where the URL is just the video ID

if __name__ == "__main__":
    app.run(debug=True)

#  http://localhost:5000/api/summarize?youtube_url=YOUR-YOUTBE-ID-OR-URL