from flask import Flask, request, render_template
app = Flask(__name__)

## Lesson 1: Getting something to show up!
@app.route('/')
def show_something_on_site():
    return "Hello World!"

## Lesson 2: Getting something custom to show up
@app.route('/hello/<name>')
def show_something_custom(name):
    return 'Hey {}! Nice to meet you!'.format(name)

## Lesson 3: Quiz Time!
@app.route('/quiz')
def quiz():
    title = "Spooky Halloween Quiz"
    questions = [
        "Do you like garlic?",
        "Are you a morning person?",
        "Do you like your steak well done?"
    ]

    return render_template('main_page.html', title=title, questions=questions)

## Lesson 4: Results!
@app.route('/results', methods=["POST"])
def results():
    answers = [] # We're gonna keep track of all the answers we get
    yes_counter = 0 # How many yes answers have we seen
    no_counter = 0 # How many no answers have we seen

    # answers.append(request.form["question1"])
    # answers.append(request.form["question2"])
    ## Make sure you have all of your questions!

    ## For loop...
    for i in range(2): ## In order to show this we also have to explain about counting from 0
        answers.append(request.form["question{}".format(i + 1)])

    ## For Each Loop
    for answer in answers:
        if answer == 'yes':
            yes_counter = yes_counter + 1
        else:
            no_counter = no_counter + 1

    ## Compare our results!
    if  yes_counter > no_counter:
        result = "You're NOT a vampire"
    else:
        result = "AHH! You're a vampire"

    return result
