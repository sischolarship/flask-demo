from flask import Flask, redirect, request, render_template


app = Flask(__name__)

# this is what happens when a user loads the page
# think of it as the homescreen
@app.route("/")
def index():
    return render_template('index.html', prompt="i lost the game")

# this is what happens when a user hits "send" on the page
# basically we recreate the page with the new text they typed
#   in a text-based game, for example, you can decide where the story should go to next
@app.route("/", methods=['POST'])
def response():
    # this is how to get what the user typed
    #   "response" matches the `name` set in the html input tag
    user_input = request.form.get("response")
    return render_template("index.html", prompt=user_input)


if __name__ == '__main__':
    app.run(debug=True)
