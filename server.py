from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['GET','POST'])         
def checkout():
    import datetime
    now = datetime.datetime.now()
    date =now.strftime("%m-%d-%Y- %H:%M:%S")
    print(request.form)
    data = {
        'strawberry':request.form['strawberry'],
        'raspberry': request.form['raspberry'],
        'apple':request.form['apple'],
        'blackberry':request.form['blackberry'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'student_id':request.form['student_id']
    }
    print("Charging {{first_name}} {{last_name}} for (count) fruits.")
    return render_template("checkout.html", date = date, data = data)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    