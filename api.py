from flask import Flask,jsonify,request
app = Flask(__name__)
global contador
contador = 0
global acum
acum = 0
global prom
prom=0
@app.route("/",methods=['Get'])
@app.route("/home",methods=['Get'])
def home():
    return "welcome"
@app.route("/info",methods=['Get'])
def inf():
    return jsonify("hola"),200
     
@app.route('/sum',methods=['Post'])
def sumx():
    global contador
    global acum
    global prom
    value=None
    value=int(request.args['value'])
    if not value:
        return '"you must send the value URL param',400
    if value>=0:
        contador=contador+1
        acum=acum+contador
        prom=acum/contador
        return "",200
    if value<0:
        return  "value param must be an integer equal or greater than 0",400
@app.route('/res',methods=['Get'])
def res():
    value = {
        "total": acum,
        "count": contador,
        "prom":prom
       
    }
    return jsonify(value)
        
    

if __name__ =='main':
    app.run(debug=True)  