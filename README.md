# IntelligentSystemsCSGraduateHandbookChatBot

**Website:**
https://ttugradhandbook.saitejakaparthi.repl.co/  **(Working Prototype)**
https://saitejakaparthi24.github.io/IntelligentSystemsCSGraduateHandbookChatBot/ **(Just UI)**

Before you start playing with replit prototype Click on **Request temporary access to the demo server** from this link https://cors-anywhere.herokuapp.com/http://wave.ttu.edu/ajax.php for every session.

**Implementation of the Application:**
![image](https://github.com/saitejakaparthi24/IntelligentSystemsCSGraduateHandbookChatBot/assets/114630408/b519d3ec-13e7-4127-b674-fbb8e687442f)

Pseudocode
1.	User asks query via Text or Voice Command
2.	The query is converted to ASP_Query based on the Python program which uses Scikit Learn.
3.	When the Submit button is Clicked Knowledge and ASP_Query is sent to API and response is sent back to UI.
4.	The response is displayed in the UI.
5.	“Clear All” button is used to clear everything and make the application ready for the next query.

Technologies Used:
•	The tool is developed in a Flask environment (a micro web framework written in Python). We developed this chat bot using HTML, CSS, JS as front end, Python acts as Back end to this chat bot.
•	We used Google Text to Speech (gTTS) to convert voice command to text query.
•	To make the chatbot more efficient in converting normal queries to ASP Query, we used cosine similarity, TfidfVectorizer, pairwise similarity, Scikit learn to make the model understand knowledge base and convert the text query to ASP query model accordingly.
•	Used provided API for sending sorts, predicates, rules, ASP Query to http://wave.ttu.edu and captured response. The response is then manipulated using string manipulation techniques in JavaScript and displayed in the result box.
•	Replit – Replit is an online integrated software development environment just like GitHub(but it can perform few backend activities and much more). We used Replit to deploy our Flask project and published the chatbot to live.

![image](https://github.com/saitejakaparthi24/IntelligentSystemsCSGraduateHandbookChatBot/assets/114630408/da013b0e-6e19-4b55-94a8-ae0220789bfa)

Few Questions you can try asking the chatbot are

  "How many credits requires for PhD in Computer Science"
  "How many credits requires for Thesis Masters in Computer Science"
  "How many credits requires for Non Thesis Masters in Computer Science"
  "What is course code of cs5331"
  "What is course code of Mobile Data Management"
  "What is the minimum credit hour requirement for graduate students during each semester (fall and spring)?"
  "What is the maximum time limit for completing coursework in an M.S. program? (6 years)"
  "In which language is the graduate coursework at TTU conducted?"
  "What is the minimum average grade requirement for graduate students?"
  "When will graduate student’s progress be evaluated?"
  "What is the minimum number of CS courses required for Ph.D. students?"
  "What is the annual attendance requirement for Ph.D. students in CS seminars?"
  "How many credit hours of 8000-level courses are required for Ph.D. students?"
  "How many credit hours of 8000-level courses are required during the graduating semester for Ph.D. students?"
  "How many accepted publications are required for Ph.D students to graduate?"
  "What is the minimum cumulative GPA requirement for students to maintain every semester as per the policy of the Graduate School?"
  "List the core coureses in Computer Science"
  "List the core coureses in Software Engineering"
  "Is CS 5375 core course for cs?"
  "What is the total number of credits required for degree plan for an MS Thesis program,as per the program guidelines?"
  "What is the total number of credits required for degree plan for an MS non-Thesis program,as per the program guidelines?"
  "Is CS 5373 is core course in MS3E degree?"
  "What is the total number of credits required for degree plan for an MS3E Thesis program,as per the program guidelines?"
  "What is the total number of credits required for degree plan for an MS3E non-Thesis program,as per the program guidelines?"
  "List the electives in SE"
  "List the cores in SE"
  "What is the total number of elective hours required for the MS3E program ?"
  "how many of the elective hours must be from the Software Engineering Electives category, as per the MS3E program guidelines?"

![image](https://github.com/saitejakaparthi24/IntelligentSystemsCSGraduateHandbookChatBot/assets/114630408/a8903ff9-f091-4622-8b01-d69123e500ac)
![image](https://github.com/saitejakaparthi24/IntelligentSystemsCSGraduateHandbookChatBot/assets/114630408/420f3e76-9eb6-46e8-b628-fe38d87741fb)

  
