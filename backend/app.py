from flask import Flask, jsonify
from monitor import ping_host, get_latency

app = Flask(__name__)

@app.route("/api/status/<host>")
def status(host):
    return jsonify({
        "host": host,
        "reachable": ping_host(host),
        "latency": get_latency(host)
    })

if __name__ == "__main__":
    app.run(debug=True)
