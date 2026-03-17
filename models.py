from datetime import datetime


class Question:
    def __init__(self, question_id, text, options, correct_answer, topic):
        self.question_id = question_id
        self.text = text
        self.options = options  # dict: {"A": "...", "B": "...", "C": "...", "D": "..."}
        self.correct_answer = correct_answer  # "A", "B", "C", or "D"
        self.topic = topic

    def check_answer(self, user_answer):
        """Returns True if user_answer matches correct_answer."""
        return user_answer.upper() == self.correct_answer.upper()

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "text": self.text,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "topic": self.topic,
        }


class TestResult:
    def __init__(self, student_name, answers, questions):
        self.student_name = student_name
        self.answers = answers  # dict: {question_id: user_answer}
        self.questions = questions
        self.timestamp = datetime.now()
        self.score, self.total, self.details = self._calculate_score()

    def _calculate_score(self):
        """Calculate score and return (score, total, details list)."""
        score = 0
        total = len(self.questions)
        details = []
        for q in self.questions:
            user_ans = self.answers.get(str(q.question_id), "")
            correct = q.check_answer(user_ans)
            if correct:
                score += 1
            details.append({
                "question": q.text,
                "topic": q.topic,
                "user_answer": user_ans,
                "correct_answer": q.correct_answer,
                "options": q.options,
                "is_correct": correct,
            })
        return score, total, details

    def get_percentage(self):
        if self.total == 0:
            return 0
        return round((self.score / self.total) * 100, 1)

    def get_grade(self):
        pct = self.get_percentage()
        if pct >= 90:
            return "A"
        elif pct >= 80:
            return "B"
        elif pct >= 70:
            return "C"
        elif pct >= 60:
            return "D"
        else:
            return "F"

    def get_formatted_timestamp(self):
        return self.timestamp.strftime("%B %d, %Y at %I:%M %p")

# ── Question Bank (20 CS questions) ──────────────────────────────────────────

QUESTION_BANK = [
    Question(1, "What does OOP stand for?",
             {"A": "Object-Oriented Programming", "B": "Open Operational Protocol",
              "C": "Ordered Output Processing", "D": "Object Output Programming"},
             "A", "OOP"),

    Question(2, "Which data structure follows the LIFO (Last-In, First-Out) principle?",
             {"A": "Queue", "B": "Linked List", "C": "Stack", "D": "Heap"},
             "C", "Data Structures"),

    Question(3, "Which data structure follows the FIFO (First-In, First-Out) principle?",
             {"A": "Stack", "B": "Queue", "C": "Tree", "D": "Graph"},
             "B", "Data Structures"),

    Question(4, "What is the time complexity of binary search on a sorted array?",
             {"A": "O(n)", "B": "O(n²)", "C": "O(log n)", "D": "O(1)"},
             "C", "Algorithms"),

    Question(5, "In Python, which keyword is used to define a class?",
             {"A": "def", "B": "object", "C": "struct", "D": "class"},
             "D", "Python"),

    Question(6, "What does the __init__ method do in a Python class?",
             {"A": "Destroys the object", "B": "Initializes/constructs the object",
              "C": "Imports the class", "D": "Inherits a parent class"},
             "B", "OOP"),

    Question(7, "Which of the following is NOT a pillar of OOP?",
             {"A": "Encapsulation", "B": "Inheritance", "C": "Compilation", "D": "Polymorphism"},
             "C", "OOP"),

    Question(8, "What is the worst-case time complexity of Bubble Sort?",
             {"A": "O(n log n)", "B": "O(n)", "C": "O(n²)", "D": "O(log n)"},
             "C", "Algorithms"),

    Question(9, "In Python, what method removes and returns the last element of a list?",
             {"A": ".remove()", "B": ".delete()", "C": ".pull()", "D": ".pop()"},
             "D", "Python"),

    Question(10, "What does SQL stand for?",
             {"A": "Structured Query Language", "B": "Simple Queue Logic",
              "C": "System Query Layer", "D": "Structured Queue List"},
             "A", "Databases"),

    Question(11, "Which HTTP method is typically used to submit a form and send data to a server?",
             {"A": "GET", "B": "DELETE", "C": "POST", "D": "HEAD"},
             "C", "Web Development"),

    Question(12, "What is a Python decorator?",
             {"A": "A CSS styling rule", "B": "A function that modifies another function",
              "C": "A loop construct", "D": "A database query tool"},
             "B", "Python"),

    Question(13, "In Git, which command stages changes for a commit?",
             {"A": "git push", "B": "git commit", "C": "git add", "D": "git merge"},
             "C", "Version Control"),

    Question(14, "What is the primary purpose of an API?",
             {"A": "To style web pages", "B": "To allow different software systems to communicate",
              "C": "To store data in a database", "D": "To compile code"},
             "B", "Web Development"),

    Question(15, "Which sorting algorithm has an average time complexity of O(n log n)?",
             {"A": "Bubble Sort", "B": "Insertion Sort", "C": "Merge Sort", "D": "Selection Sort"},
             "C", "Algorithms"),

    Question(16, "What does HTML stand for?",
             {"A": "Hyper Transfer Markup Language", "B": "HyperText Markup Language",
              "C": "High-level Text Making Language", "D": "Hyper Tool Markup Loader"},
             "B", "Web Development"),

    Question(17, "In Python, which built-in module is used to work with dates and times?",
             {"A": "calendar", "B": "time_module", "C": "datetime", "D": "clock"},
             "C", "Python"),

    Question(18, "What is encapsulation in OOP?",
             {"A": "Creating multiple instances of a class",
              "B": "Bundling data and methods that operate on that data within one unit",
              "C": "Inheriting attributes from a parent class",
              "D": "Converting one data type to another"},
             "B", "OOP"),

    Question(19, "Which data structure would you use to check if parentheses in an expression are balanced?",
             {"A": "Queue", "B": "Array", "C": "Stack", "D": "Hash Map"},
             "C", "Data Structures"),

    Question(20, "What is the purpose of a README.md file in a GitHub repository?",
             {"A": "To store the database schema", "B": "To configure the server",
              "C": "To explain what the project does and how to run it", "D": "To list all contributors"},
             "C", "Version Control"),
]
