from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def replace_content_with_newline(json_data):
    if "content" in json_data:
        json_data["\n"] = json_data.pop("content")
    return json_data

@app.route('/get_response', methods=['GET'])
def get_response():
    query = request.args.get('query')
    custom = request.args.get('custom', "detailed recipe of ")
    if query:
        api_url = f"https://api.easy-api.online/v1/globalgpt?q={custom}{query}"
        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                modified_json_response = replace_content_with_newline(response.json())
                return jsonify(modified_json_response), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Failed to fetch response from the API"}), 500
    else:
        return jsonify({"error": "Query parameter 'query' is missing"}), 400

@app.route('/food_benefits', methods=['GET'])
def food_benefits():
    query = request.args.get('query')
    custom = request.args.get('custom', "display the nutrition facts, nutrients and benefits of ")
    if query:
        api_url = f"https://api.easy-api.online/v1/globalgpt?q={custom}{query}"
        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                modified_json_response = replace_content_with_newline(response.json())
                return jsonify(modified_json_response), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Failed to fetch response from the API"}), 500
    else:
        return jsonify({"error": "Query parameter 'query' is missing"}), 400

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('query')
    custom = request.args.get('custom', "suggest a recipe or dishes and show grocery list based on the ingredient/ingredients ")
    if query:
        api_url = f"https://api.easy-api.online/v1/globalgpt?q={custom}{query}"
        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                modified_json_response = replace_content_with_newline(response.json())
                return jsonify(modified_json_response), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Failed to fetch response from the API"}), 500
    else:
        return jsonify({"error": "Query parameter 'query' is missing"}), 400

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/recipe_assistant')
def recipe():
    return render_template('recipe.html')

@app.route('/suggest_recipe')
def planner():
    return render_template('suggest.html')

@app.route('/food_benefit')
def benefits():
    return render_template('benefits.html')

@app.route('/measure')
def measure():
    return render_template('measure.html')
       
if __name__ == '__main__':
    app.run(debug=True, port=5002)
