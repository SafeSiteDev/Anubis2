from flask import Flask, request, jsonify
import your_ai_model  # Replace with your actual AI model import

app = Flask(__name__)

@app.route('/start_ai', methods=['POST'])
def start_ai():
    try:
        data = request.get_json()
        input_data = data['inputData']  # Retrieve input data from frontend

        # Pass data to your AI model for processing
        ai_result = your_ai_model.process(input_data)

        return jsonify({"response": ai_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
