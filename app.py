from flask import Flask, render_template, request
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():
	resp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=CJIKeQKz4nuOpRSiMmW2qWB7qylNrE717O2q30Va")
	string = rep.read()
	dictionary = json.loads(string)
	return render_template('index.html', pic = dictionary['url'], info = dictionary["explanation"])
	
if __name__ == '__main__':
	app.run(debug = True)