from flask import Flask, request
from enigma import *

app = Flask(__name__)

@app.route("/denigma/<msg>/",methods=['GET'])
def deenigmaroute(msg):
    content_type = request.headers.get('Content-Type')
    if not (content_type == 'application/json'):
        return {'ErrorType':"404",'Msg':'Input type not supported'}
    
    return {'msg decodificada':de_nigma(msg,encoder,encoder2)}

@app.route("/enigma/",methods=['POST'])
def enigmaroute():
    content_type = request.headers.get('Content-Type')
    if not (content_type == 'application/json'):
        return {'ErrorType':"404",'Msg':'Input type not supported'}
    
    msg = request.json['msg']
    if msg == '':
        return {'ErrorType':"404",'Msg':'No input has been given'}

    print(msg)
    return {'msg':enigma(msg, encoder, encoder2)}


if __name__ == "__main__":
    app.run()