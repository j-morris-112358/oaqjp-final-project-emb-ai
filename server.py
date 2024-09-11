"""
module docstring
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def sent_detector():
    """ function docstring """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dom_emotion = response['dominant_emotion']

    if dom_emotion is not None:
        # Return a formatted string with the sentiment label and score
        return "For the given statement, the system response is 'anger': " \
        + str(anger) + ", 'disgust': " + str(disgust) + ", 'fear': " \
        + str(fear) + ", 'joy': " + str(joy) + ", 'sadness': " \
        + str(sadness) + ". The dominant emotion is <b>" + dom_emotion + "</b>."

    return "<b>Invalid text! Please try again!</b>"

@app.route("/")
def render_index_page():
    """ function docstring """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
