from flask import Flask
import json
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def sub():
    
    video_id_or_url = 'zPx5N6Lh3sw'

    try:
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id_or_url)

       
        text_paragraph = "\n".join([item['text'] for item in transcript])
        abc=json.dumps(text_paragraph)
        zuv=json.loads(abc)

        return zuv
    except Exception as e:
        return str(e)

app.run(debug=True)










