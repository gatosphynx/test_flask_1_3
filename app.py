from flask import Flask

app = Flask(name)

@app.route('/init', methods = ['GET'])
def init():
  return {"payload":"welcome to my project"}

@app.route('/read/:<content>', methods = ['GET'])
def read(content):
    return {'payload': content}


@app.route('/init/content', methods = ['GET'])
def admin():
  return {"payload":alfa}

@app.route('/delete/:<content>', methods = ['DELETE'])
def read(content):
    return {"payload":qux}

@app.route('/create/:<content>', methods = ['POST'])
def read(content):
    return {"payload":bar} 
  
if name == 'main':
    app.run(debug=True)
