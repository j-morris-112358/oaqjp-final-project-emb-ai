import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    # convert to JSON
    formatted_response = json.loads(response.text) 
   
    # if response.status_code is 200 extract emotions and scores
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness'] 
        # find dominant emotion
        emotion_names = ["anger", "disgust", "fear", "joy", "sadness"]
        emotion_scores = [anger, disgust, fear, joy, sadness]
        high_score = 0.0
        dom_emotion_name = ""
        index = -1
        for item in emotion_scores:
            index += 1
            score = item
            if score > high_score:
                high_score = score
                dom_emotion_name = emotion_names[index]
    # cover explict case in Task 7 instructions and 500 etc.
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dom_emotion_name = None
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dom_emotion_name = None

        
    
    # format output as dictionary
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dom_emotion_name}

    