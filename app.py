# app.py - Flask Birthday API for Render
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/birthday')
def birthday_wish():
    return jsonify({
        "status": "200 OK 🎂",
        "message": "HAPPY BIRTHDAY Bhai Anas!",
        "celebration": {
            "event": "Birthday Celebration",
            "honoree": "Muhammad Anas",
            "date": "today",
            "mood": "🎭 Wah Shampy Wah! 🔥"
        },
        "wishes": [
            "✨ May you find joy in every git push",
            "✨ May your migrations always run smoothly",
            "✨ May your queries be optimized",
            "✨ May your database always be in sync",
            "✨ May your deployments be zero-downtime",
            "✨ May CORS never block your requests"   
        ],
        "gifts": {
            "bugs": "∞",
            "tickets": "unlimited",
            "unsuccessful_deploys": "guaranteed",
            "merge_conflicts": "daily",
        },
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
