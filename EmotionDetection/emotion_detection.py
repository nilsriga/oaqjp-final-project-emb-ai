import requests
import json

def emotion_detector(text_to_analyze):

    response = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json =  { "raw_document": { "text": text_to_analyze } }
        )

    emotion_scores = json.loads(response.text)["emotionPredictions"][0]["emotion"]

    dominant_emotion = sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True)[0][0]

    emotion_scores |= {"dominant_emotion": dominant_emotion}

    desired_order = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]
    
    sorted_emotions = {key: emotion_scores[key] for key in desired_order if key in emotion_scores}

    json_response = json.dumps(sorted_emotions, indent=4, separators=(',', ': '))

    return json_response

print(emotion_detector("I love this new technology"))