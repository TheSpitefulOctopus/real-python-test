#import the Flask class from the flask package
from flask import Flask

# create the applicatioin object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
@app.route('/hello')
# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"


# adding a dynamic route
@app.route('/test/<search_query>')
def search(search_query):
	return "Hello " + search_query


#dynamic with int
@app.route('/integer/<int:value>')
def int_type(value):
	print value + 1
	return "correct"

#dynamic with float
@app.route('/float/<float:value>')
def float_type(value):
	print value + 1
	return "correct"

#dynamic route that accepts slashes
@app.route('/path/<path:value>')
def path_type(value):
	print value
	return  "correct"


@app.route('/name/<name>')
def index(name):
	if name.lower() == "michael":
		return "Hello {}".format(name), 200
	else:
		return "Not Found", 404

# start the development server using the run method
if __name__ == "__main__":
	app.run(debug=True)