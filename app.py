from flask import Flask, render_template, request

app = Flask(__name__)

OPERATIONS = ["+", "-", "*", "/"]


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", operations=OPERATIONS)


@app.route('/calculate', methods=['POST'])
def calc():  # put application's code here
    output = None
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    operation = request.form.get("operation")
    if operation == "+":
        output = int(num1) + int(num2)
    elif operation == "-":
        output = int(num1) - int(num2)
    elif operation == "*":
        output = int(num1) * int(num2)
    elif operation == "/":
        if num2 == 0:
            output = 0
        output = int(num1) / int(num2)
    return render_template('output.html', operation=request.form.get("operation"),
                           num1=request.form.get("num1"), num2=request.form.get("num2"), output=output)


if __name__ == '__main__':
    app.run()
