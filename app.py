from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "...........HELLO..............."
@app.route("/home")
def home():
    return "My Home Page::::::::::::::" 
@app.route("/contact")
def contact():
    return "My Contact Page_____________"   
if(__name__=="__main__"):
    app.run()