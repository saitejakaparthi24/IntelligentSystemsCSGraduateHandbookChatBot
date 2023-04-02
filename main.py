import os
from flask import Flask, render_template, request
from gtts import gTTS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# define dictionary of abstract questions and corresponding ASP queries
asp_queries = {
    "How many credits requires for PhD in Computer Science": "requiresCredits(phd, X).",
    "How many credits requires for Thesis Masters in Computer Science": "credits(MSCSThesis,X)",
    "How many credits requires for Non Thesis Masters in Computer Science": "credits(MSCSNonThesis,X)",
    "How many credits requires for Masters of Science in Software and Security Engineering": "credits(MSSSE,X)",
    "How many credits requires for Certificate in Software Engineering": "credits(SE,X)",
    "How many credits requires for Certificate in Security": "credits(Security,X)",
    "What is course code of cs5331":"hasCoursecode(X, cs5331)"
    # add more abstract questions and corresponding ASP queries here
}

# def asp_queries_dict():
#     input_strings = [
#         "What is gender of Alex?",
#         "What is course code of cs5363?"
#     ]
#
#     output_regex_patterns = {
#         r"What is gender of (\w+)\?": "gender(\\1,X)",
#         r"What is course code of (\w+)\?": "coursecode(\\1,X)"
#     }
#
#     output_dict = {}
#
#     for input_str in input_strings:
#         for pattern, regex in output_regex_patterns.items():
#             match = re.match(pattern, input_str)
#             if match:
#                 output_dict[input_str] = regex.replace('\\1', match.group(1))
#                 break
#
#     print(output_dict)

# function to get the corresponding ASP query for a given input text
def get_query(input_text):
    tfidf_vectorizer = TfidfVectorizer()
    # convert the input text and the abstract questions to vectors
    text_vectors = tfidf_vectorizer.fit_transform([input_text] + list(asp_queries.keys()))
    # calculate the cosine similarity between the input text and the abstract questions
    similarity_scores = cosine_similarity(text_vectors[0:1], text_vectors[1:])
    # get the index of the abstract question with the highest similarity score
    closest_index = similarity_scores.argmax()
    if similarity_scores[0][closest_index] > 0:
        closest_question = list(asp_queries.keys())[closest_index]
        return asp_queries[closest_question]
    else:
        return None


# function to convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("static/output.mp3")


#input_texts = request.form['input_text']


# route for home page that renders the HTML template with a form for user input
@app.route('/', endpoint='home')
def home():
    return render_template('index.html')


# route for form submission that handles the user input, gets the corresponding ASP query, and adds it to the ASP query text field
@app.route('/submit', methods=['POST'],endpoint='submit')
def submit():
    # get user input text from form
    input_text = request.form['input_text']
    # get corresponding ASP query
    query = get_query(input_text)
    if query:
        # add query to ASP query text field
        return render_template('index.html', asp_query=query, text_query=input_text)
    else:
        output_text = "Sorry, I could not find a matching query for your input"
        # convert output text to speech and play it
        # text_to_speech(output_text)
        # os.system("mpg321 static/output.mp3")
        # return to home page
        return render_template('index.html', asp_query=output_text, text_query=input_text)


# @app.route('/submitsparc', methods=['POST'],endpoint='submitsparc')
# def submitsparc():
#     input_text = request.form['input_text_hidden']
#     return render_template('index.html', text_query=input_text)

@app.route('/clearall', methods=['POST'],endpoint='clearall')
def clearall():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
