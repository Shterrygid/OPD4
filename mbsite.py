from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

def age(s):
    try:
        if type(s) == float:
            return "That's wrong"
        var = int(s)
        if var < 1 or var > 120:
            return "That's wrong"
    except:
        return "That's wrong"
    return str(var)

def uvlech(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var
def month(var):
    HEI = {"Январь", "Февраль", "Март", "Апрель", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Май", "январь", "февраль", "март", "апрель", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь", "май"}
    for i in HEI:
        if i == var:
            return i
    return "That's wrong"

def names(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var

def secondnames(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var

def lastnames(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var


def rain(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':

        firstname = request.form.get('name1')
        secondname = request.form.get('name2')
        lastname = request.form.get('name3')
        age1 = request.form.get('name4')
        uvlech1 = request.form.get('name5')
        rain1 = request.form.get('name6')
        month1 = request.form.get('name7')

        str = "" + names(firstname) + " " + secondnames(secondname) + " " + lastnames(lastname) + " " + age(age1) + " | " + uvlech(uvlech1) + " | " + rain(rain1) + " | " + month(month1) + '\n'
        with open('answers.txt', 'a') as file:
            file.write(str)
        return render_template('main.html')

def start():
    app.run(debug=True)