import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    print(response)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            # 'dominant_emotion': '<name of the dominant emotion>'
            }
        dominant_emotion = max(result, key=result.get)

        #add the dominant emnotion to the above dictionary
        result['dominant_emotion'] = dominant_emotion

    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        result = {}

    # Return the label and score in a dictionary
    return {}
    