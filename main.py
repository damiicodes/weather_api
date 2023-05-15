from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the homepage
@app.route('/')
def home():
    # Render the 'tutorial.html' template and return it as the response
    return render_template('home.html')


# Define a route for the about page
@app.route('/about/')
def about():
    # Render the 'about.html' template and return it as the response
    return render_template('about.html')


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
