from flask import Flask, request
from enigma import *

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def enigmaroute():
    if request.method == 'GET':
        return 'No input has been given'
    else:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            if json['action'] == 'enigma':
                return {'Msg':enigma(json['msg'],encoder,encoder2)}
                # return "enigma"
            elif json['action'] == 'de_nigma':
                return {"Msg":de_nigma(json['msg'],encoder,encoder2)}
                # return "de_nigma"
            else:
                return {'ErrorType':"404",'Msg':'Action type not supported'}
        else:
            return {'ErrorType':"404",'Msg':'Input type not supported'}

if __name__ == "__main__":
    app.run()