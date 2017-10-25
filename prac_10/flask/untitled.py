from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! :)'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return  "Hello {}".format(name)

@app.route('/temp_convertor')
@app.route('/temp_convertor/<temp>')
def temp_convertor(temp=''):
    celsius = float(temp)
    fahrenheit = celsius * 9 / 5 + 32
    # return fahrenheit
    return "{} degress celcius is {} degrees fahrenheit".format(celsius,fahrenheit)

if __name__ == '__main__':
    app.run()
