from flask import Flask, json
from waitress import serve

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

app = Flask(__name__)

@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@app.route('/companies', methods=['POST'])
def post_companies():
  return json.dumps({"success": True}), 201

if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=8000)
