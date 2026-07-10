# Day-17: QiuzBrain Project in OOP
## Project Objective
In Day 17 of my Python journey. I learned how to worked with classes, object attributes, constructors (`__init__()` methods), and class methods to build a structured application. I also learned how to create objects from classes, organize data using lists and dictionaries, and separate program logic into multiple modules. By combining these concepts, I developed a fully functional Quiz Game that allows users to answer a series of True/False questions, get score for each question after each response, and view their final score at the end of the quiz.

## What I Learnt
1. Learned how to define and use classes in Python.
2. Understood how to initialize object attributes using the __init__() constructor.
3. Gained experience creating methods to define a class's behavior.
4. Practiced creating multiple objects and managing them within a list.
5. Learned how to pass objects between classes to build more organized and interactive programs.
6. Improved my ability to structure Python projects by separating code into multiple modules for better readability and maintainability.
## How It Works
* The `question_data` list stores a collection of True/False questions, with each question represented as a dictionary containing the question text and the correct answer.

* Each dictionary is converted into a `Question` object, providing a structured way to store the question and its corresponding answer.

* All `Question` objects are added to a list called `question_bank`, which groups the quiz questions together for easy management.

* A `QuizBrain` object is created by passing the `question_bank` list to the `QuizBrain` class. This object manages the overall flow of the quiz and keeps track of the user's progress and score.

* The `still_has_questions()` method checks whether there are any remaining questions to be answered.

* The `next_question()` method displays the next question, accepts the user's input, and passes the response for validation.

* The `check_answer()` method compares the user's answer with the correct answer, provides immediate feedback, and updates the score when the answer is correct.

* After all questions have been answered, the program displays the user's final score, showing the total number of correct answers out of the total questions asked.

   ## Output
![alt text](<2026-07-10 (1).png>)
 ![alt text](<2026-07-10 (4).png>)
