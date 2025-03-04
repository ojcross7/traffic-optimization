from flask import Flask, render_template, jsonify  
import redis  

app = Flask(__name__)  
redis_client = redis.Redis(host='localhost', port=6379)  

@app.route("/")  
def dashboard():  
    return render_template("dashboard.html")  

@app.route("/traffic_data")  
def get_traffic_data():  
    data = redis_client.get("traffic:intersection_A")  
    return jsonify(data)  

@app.route("/adjust_signal", methods=["POST"])  
def adjust_signal():  
    # Logic to override signal timings  
    return jsonify({"status": "success"})  

if __name__ == "__main__":  
    app.run(debug=True)  