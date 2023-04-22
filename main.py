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
    "What is course code of cs5331":"hasCoursecode(X, cs5331)",
    "What is course code of Mobile Data Management":"hasCoursecode(MDM, X)",
    "What is the minimum credit hour requirement for graduate students during each semester (fall and spring)?":"requiresCredithrs(masters, X)",
    "What is the maximum time limit for completing coursework in an M.S. program? (6 years)":"maximumyears(masters, X)",
    "In which language is the graduate coursework at TTU conducted?": "teachinglang(grad, X)",
    "What is the minimum average grade requirement for graduate students?":"minavegrade(grad, X)",
    "When will graduate student’s progress be evaluated?":"programeval(grad, X)",
    "What is the minimum number of CS courses required for Ph.D. students?":"minimumcourses(phd, X)",
    "What is the annual attendance requirement for Ph.D. students in CS seminars?":"requiredseminars(phd, X)",
    "How many credit hours of 8000-level courses are required for Ph.D. students?":"req8000credithrs(phd, X)",
    "How many credit hours of 8000-level courses are required during the graduating semester for Ph.D. students?":"gradsemreq8000hrs(phd, X)",
    "How many accepted publications are required for Ph.D students to graduate?":"phdreqpublications(phd, X)",
    "What is the minimum cumulative GPA requirement for students to maintain every semester as per the policy of the Graduate School?":"mincumulativeGPA(X)",
    "List the core coureses in Computer Science":"isCoreCS(X)",
    "List the core coureses in Software Engineering":"isCoreSE(X)",
    "Is CS 5375 core course for cs?":"coursetypeCS(cs5375, X)",
    "What is the total number of credits required for degree plan for an MS Thesis program,as per the program guidelines?":"requiresCredits(masterst, X)",
    "What is the total number of credits required for degree plan for an MS non-Thesis program,as per the program guidelines?":"requiresCredits(mastersnt, X)",
    "Is CS 5373 is core course in MS3E degree?":"coursetypeSE(cs5373, X)",
    "What is the total number of credits required for degree plan for an MS3E Thesis program,as per the program guidelines?":"requiresCredits(masterst,X)",
    "What is the total number of credits required for degree plan for an MS3E non-Thesis program,as per the program guidelines?":"requiresCredits(mastersnt, X)",
    "List the electives in SE":"isElectiveSE(X)",
    "List the cores in SE":"isCoreSE(X)",
    "What is the total number of elective hours required for the MS3E program ?":"electivehour(X)",
    "how many of the elective hours must be from the Software Engineering Electives category, as per the MS3E program guidelines?":"electivehourfromse(X)"

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
