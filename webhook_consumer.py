from flask import Flask,request,json

app = Flask(__name__)

@app.route('/')
def hello():    
    return 'Webhooks with Python'

@app.route('/githubevent',methods=['POST'])
def githubIssue():
    data = request.json
    print(data)
    return data
 
if __name__ == '__main__':
    app.run(host="localhost", port=8088, debug=True)
