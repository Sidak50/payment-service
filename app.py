from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    return jsonify({
        "status": "success",
        "message": "Payment processed successfully (mock)."
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#Test
