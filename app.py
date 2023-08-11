from flask import Flask

app = Flask(__name__)

@app.route('/init', methods = ['GET'])
def init():
  return {"payload":"welcome to my project"}
  
@app.route('/read/:<content>', methods = ['GET'])
def read(content):
    return {'payload': content}


@app.route('/init/content', methods = ['GET'])
def admin():
  return {"payload":alfa}

if __name__ == '__main__':
    app.run(debug=True)
