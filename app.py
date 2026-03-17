from flask import Flask, render_template, request, redirect, url_for, session
from models import QUESTION_BANK, TestResult
from datetime import datetime

app = Flask(__name__)
app.secret_key = "csc202_secret_key_2024"

# Stack (LIFO) to store recent results history — implements Requirement A
results_history = []


@app.route("/")
def home():
    """Home page: shows instructions and recent results history."""
    # Show the top 5 most recent results (stack — last in, first out view)
    recent = list(reversed(results_history[-5:])) if results_history else []
    return render_template("home.html", recent=recent, total_questions=len(QUESTION_BANK))


@app.route("/test", methods=["GET", "POST"])
def test():
    """Test page: displays all 20 questions in a single form."""
    if request.method == "POST":
        student_name = request.form.get("student_name", "Anonymous").strip()
        if not student_name:
            student_name = "Anonymous"

        # Collect answers from form
        answers = {}
        for q in QUESTION_BANK:
            ans = request.form.get(f"q{q.question_id}", "")
            answers[str(q.question_id)] = ans

        # Create result object (calculates score automatically)
        result = TestResult(student_name, answers, QUESTION_BANK)

        # Push result onto the stack
        results_history.append(result)

        # Store result index in session so result page can retrieve it
        session["last_result_index"] = len(results_history) - 1

        return redirect(url_for("result"))

    return render_template("test.html", questions=QUESTION_BANK)



