import Flask from flask
import emotion_detector from emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector", methods=['POST'])
def analyze_text():
    text_to_analyze = request.json
    if not text_to_analyze:
        return {"message": "Invalid input parameter"}, 422
    try:
        emotions = emotion_detector(text_to_analyze)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{emotions}"}, 200