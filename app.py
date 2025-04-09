from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    if (num1 + num2) > 5.8:
        return jsonify({"prediction": 1, "features": {"num1": num1, "num2": num2}})
    else:
        return jsonfify({"prediction": 0, "features": {"num1": num1, "num2": num2}})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')
