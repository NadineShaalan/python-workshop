from flask import Flask, request, render_template
app = Flask(__name__)

## Lesson 1: Getting something to show up!
@app.route('/')
def show_something_on_site():
    pass # TODO: Finish this function!

## Lesson 2: Getting something custom to show up
@app.route('/hello/<name>')
def show_something_custom(name):
    pass # TODO: Finish this function!

## Lesson 3: Quiz Time!
@app.route('/quiz')
def quiz():
    title = "Boring Quiz Name" # TODO: Change this title
    questions = [] # TODO: Fill this in with your questions!

    return render_template('main_page.html', title=title, questions=questions)

## Lesson 4: Results!
@app.route('/results', methods=["POST"])
def results():
    answers = [] # We're gonna keep track of all the answers we get
    yes_counter = 0 # How many yes answers have we seen
    no_counter = 0 # How many no answers have we seen

    answers.append(request.form["question1"])
    answers.append(request.form["question2"])
    ## Make sure you have the exact number of questions in your list!

    ## For loop...

    ## For Each Loop
    for answer in answers:
        if answer == 'yes':
            ## TODO
            continue
        else:
            ## TODO
            continue
    # TODO:
    ## Calculate our result!
    result = ""
   
    return result
