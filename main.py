from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

def compute_hash(input_str):
    return hashlib.sha256(input_str.encode()).hexdigest()

def proof_of_work(client_id, target_prefix, params):
    n = 0
    while True:
        combined = f"{client_id}:{n}:{','.join(params)}"
        hash_result = compute_hash(combined)
        if hash_result.startswith(target_prefix):
            return {
                "nonce": n,
                "hash": hash_result,
                "combined": combined
            }
        n += 1

@app.route('/proof', methods=['GET'])
def get_proof():
    client_id = request.args.get('client_id')
    prefix = request.args.get('prefix', '000')
    params = request.args.get('params')

    if not client_id or not params:
        return jsonify({"error": "Missing required parameters: client_id and params"}), 400

    param_list = params.split(',')
    result = proof_of_work(client_id, prefix, param_list)

    return jsonify({
        "client_id": client_id,
        "target_prefix": prefix,
        "params": param_list,
        "result": result
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
