#import pyttsx3 as speech
'''
engine=speech.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-75)
'''

from chatbot import *
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    ans,flag=get_bot_resp(userText)
    if(flag):
        #command=ans1
        #speech.speak(command)
        return ans
    else:
        ans1=""
        ans=[1:]
        if(len(ans)==0):
        	return str("I did not understand please search again")
        for statements in ans:
        	ans1=ans1+str(statements)
        	ans1+='\n'
    #command=ans1
    #speech.speak(command)
    return ans1



if __name__ == '__main__':
	app.run()