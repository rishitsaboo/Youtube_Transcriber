def extract(data, keys):
    out = []
    queue = [data]
    while len(queue) > 0:
        current = queue.pop(0)
        if type(current) == dict:
            for key in keys:
                if key in current:
                    out.append({key:current[key]})
            
            for val in current.values():
                if type(val) in [list, dict]:
                    queue.append(val)
        elif type(current) == list:
            queue.extend(current)
    return out
x = extract(data, ["videoID"])
print(x)









  for item in range(len(resp)):
        print(resp[item]['text'])










from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import json



app = Flask(__name__)

@app.route("/")
def api():
    abc=YouTubeTranscriptApi.get_transcript("zPx5N6Lh3sw")
    cde= json.dumps(abc)
    resp = json.loads(cde)
    for item in range(len(resp)):
        print(resp[item]['text'])
  
        
    return resp
    

app.run(debug=True)
