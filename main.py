
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def homepage():
    # Render the index.html file
    return render_template('index.html')

# Define the story progression route
@app.route('/story', methods=['GET', 'POST'])
def story():
    # Get the user's choice from the form submission
    choice = request.form.get('choice')

    # Check if the user is at the beginning of the story
    if choice == 'start':
        # Render the story.html file with the introduction
        return render_template('story.html', story='Once upon a time...')

    # Otherwise, the user is continuing the story
    else:
        # Get the current story chapter
        story = request.form.get('story')

        # Update the story based on the user's choice
        if choice == 'option1':
            story += ' The user chose option 1.'
        elif choice == 'option2':
            story += ' The user chose option 2.'

        # Check if the story has reached an ending
        if story.endswith('... The End.'):
            # Render the endings.html file with the ending
            return render_template('endings.html', ending=story)

        # Otherwise, continue the story
        else:
            # Render the story.html file with the updated story
            return render_template('story.html', story=story)

# Define the endings route
@app.route('/endings')
def endings():
    # Get the ending from the request
    ending = request.args.get('ending')

    # Render the endings.html file with the ending
    return render_template('endings.html', ending=ending)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
