import os
import time
from flask import Flask,jsonify,render_template,request
from flask_socketio import SocketIO,emit
from flask_cors import CORS


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
counter = 0
socketio=SocketIO(app,cors_allowed_origins="*")
def mock_mapping_computation(req_data):
  # mock computation
  # time.sleep(0.1)
  return {"result_A":req_data["mapping_method"],"result_B":req_data["mapping_two"],"result_C":req_data["mapping_three"]}


@socketio.on("do_mapping")
def handle_form(data):
  results  = mock_mapping_computation(data)


  emit("mapping_results",results)
@app.route("/mapping")
def run_mapping():
    return render_template("client.html")

if __name__ == '__main__':
    socketio.run(app,debug=True)

