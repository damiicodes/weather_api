from flask import Flask, render_template
import pandas as pd

# Create a Flask application instance
app = Flask(__name__)

station_data = pd.read_csv('data_small/stations.txt', skiprows=17)
station_data = station_data[['STAID','STANAME                                 ']]

# Define a route for the homepage
@app.route('/')
def home():
    # Render the 'tutorial.html' template and return it as the response
    return render_template('home.html', station_data=station_data.to_html())


# Define a route for the about page
@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = ('data_small/TG_STAID' + str(station).zfill(6) + '.txt')
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # Render the 'about.html' template and return it as the response
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
