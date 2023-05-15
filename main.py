from flask import Flask, render_template

# Create a Flask application instance
app = Flask('Website')

# Define a route for the homepage
@app.route('/home')
def home():
    # Render the 'tutorial.html' template and return it as the response
    return render_template('tutorial.html')

# Define a route for the about page
@app.route('/about/')
def about():
    # Render the 'about.html' template and return it as the response
    return render_template('about.html')

# Run the Flask application in debug mode
app.run(debug=True)
