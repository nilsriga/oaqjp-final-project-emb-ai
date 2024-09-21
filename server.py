from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detection
from pprint import pprint
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET'])
def analyze_text():
    
    text_to_analyze = request.args.get("textToAnalyze")

    return emotion_detection.emotion_detector(text_to_analyze), 200