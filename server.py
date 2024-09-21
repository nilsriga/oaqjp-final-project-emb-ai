# pylint: disable=E0401
"""
This imports the API library flask and the Watson AI analysis custom library
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

"""
This module creates a Flask web application for emotion detection.
It renders an index page and analyzes text for emotions using a GET request.
"""

@app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET'])
def analyze_text():
    """
    Analyzes the provided text and detects emotions.
    Returns a message if the text is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    analyzed_text = emotion_detection.emotion_detector(text_to_analyze)

    if analyzed_text["dominant_emotion"] is None:
        return {"message": "Invalid text! Please try again!"}, 200

    return analyzed_text, 200
