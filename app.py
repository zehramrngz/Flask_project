from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Updated questions and answers
questions = {
    "question1": "natural_language_processing",  # Correct answer: A) Natural Language Processing
    "question2": "text_classification",           # Correct answer: B) Text Classification
    "question3": "nltk",                          # Correct answer: A) NLTK
    "question4": "tokenization"                    # Correct answer: A) Tokenization
}

@app.route('/', methods=['GET', 'POST'])
def quiz():
    score_percentage = None
    if request.method == 'POST':
        answer1 = request.form.get('question1')
        answer2 = request.form.get('question2')
        answer3 = request.form.get('question3')
        answer4 = request.form.get('question4')

        # Calculate score
        score = 0
        if answer1 == questions["question1"]:
            score += 1
        if answer2 == questions["question2"]:
            score += 1
        if answer3 == questions["question3"]:
            score += 1
        if answer4 == questions["question4"]:
            score += 1

        # Calculate score percentage
        total_questions = len(questions)
        score_percentage = (score / total_questions) * 100

        # Update session with user's score percentage
        session['score_percentage'] = score_percentage

        # Update highest score percentage
        if 'highest_score_percentage' not in session or score_percentage > session['highest_score_percentage']:
            session['highest_score_percentage'] = score_percentage

    highest_score_percentage = session.get('highest_score_percentage', 0)
    return render_template('quiz.html', score_percentage=score_percentage, highest_score_percentage=highest_score_percentage)

if __name__ == '__main__':
    app.run(debug=True)
