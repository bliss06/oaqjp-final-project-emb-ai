''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion detector")

@app.route("/emotionDetector")
def run_nalysis():
    ''' This function performs the sentiment analysis '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    anger_score, disgust_score, sadness_score, fear_score, joy_score, dominant_emotion = \
    response["anger"], response["disgust"], response["sadness"], response["fear"], \
    response["joy"], response["dominant_emotion"]

    # Check if the label is None, indicating an error or invalid input
    if text_to_analyze == "" or dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Extract the scores and dominant emotion
    response_string = f"For the given statement, the system response is 'anger': \
    {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and \
    'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    return response_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
