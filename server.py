''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  
import json

#Initiate the flask app 
app = Flask("Emotion detector")

@app.route("/emotionDetector")
def runAnalysis():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    print(response)

    # Check if the label is None, indicating an error or invalid input
    if not text_to_analyze:
        return "Invalid input! Try again."
    else:
        # Extract the scores and dominant emotion

        anger_score = response["anger"]
        disgust_score = response["disgust"]
        sadness_score = response["sadness"]
        fear_score = response["fear"]
        joy_score = response["joy"]
        dominant_emotion = response["dominant_emotion"]
        response_string = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
        return response_string


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run()
