"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [
    'you suck', 'you"re boring', 'you look like a melon', 'you look really really tired today',
    'your mother was a hamster and your father smelt of elderberries']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>Hi! This is the home page.
    <br><br>
    <a href="/hello">CLICK ME</a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    part_1 = """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          What compliment would you like?
          <select name="compliment">
          """
    for word in AWESOMENESS:
        part_1 = part_1 + "<option value={word}>{word}</option>".format(word = word)

    part_2 = """ </select>
          <input type="submit" value="Submit">
        </form>
        <h2>Take a chance instead!</h2>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
    return part_1 + part_2

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = choice(DISSES)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
