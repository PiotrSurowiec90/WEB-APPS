import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==


# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route("/emoji", methods=["GET"])
def get_emoji():
    return ":)"


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = request.form.get("message")
    return f"Thanks {name}, you sent this message: {message}"


@app.route("/wave", methods=["GET"])
def wave():
    name = request.args.get("name")
    return f"I am waving at {name}"


@app.route("/count_vowels", methods=["POST"])
def count_vowels():
    text = request.form.get("text").lower()
    num_of_vowels = sum([1 for letter in text if letter in "aeiou"])
    return f'There are {num_of_vowels} vowels in "{text}"'


@app.route("/sort_names", methods=["POST"])
def sort_names():
    names_list = request.form.get("list").split(",")
    return ",".join(sorted(names_list))


@app.route("/names", methods=["GET"])
def names():
    names_list = ["Alice", "Karim", "Julia"]
    extra_names = request.args.get("add")
    if extra_names:
        names_list += extra_names.split(",")

    return ", ".join(sorted(names_list))


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes

apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
