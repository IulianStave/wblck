from flask import Flask, render_template

#instantiate the class
app=Flask(__name__)

#decorator url where you will view the web app

@app.route('/')
#a function that defines what the website contains
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

#when the script is executed the __name__ variable gets value __main__
if __name__=="__main__":
    app.run(debug=True)