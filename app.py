from flask import Flask, render_template, request

app = Flask(__name__)

OPERATIONS = ["+", "-", "*", "/"]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/twonumber', methods=['GET', 'POST'])
def calc():  # put application's code here
    output = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        if operation == "+":
            output = num1 + num2
        elif operation == "-":
            output = num1 - num2
        elif operation == "*":
            output = num1 * num2
        elif operation == "/":
            if num2 == 0:
                output = 0
            output = num1 / num2
    return render_template('output.html', OPERATION=operation, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run()