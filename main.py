from flask import Flask, render_template, request
import chat
import braille
import time
app = Flask(__name__)

# initialize braille
usbport = '/dev/tty.usbmodem141101'
servo_ports=[1,2,3,4,5,6]
br = braille.braille(90,30,97,37,90,30,90,150,90,157,100,167,usbport,servo_ports)

br.AllUp()
time.sleep(2)
br.AllDown()
time.sleep(1)

bot = chat.df(DIALOGFLOW_PROJECT_ID='prime-moment-265717')


@app.route("/")
def home():    
    return render_template("home.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    returnval = str(bot.GetResponse(userText)) 
    # write to arduino
    br.WriteStr(returnval) 

    return returnval

if __name__ == "__main__":    
    app.run(debug=True)