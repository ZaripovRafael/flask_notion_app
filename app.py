from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
async def index():
    return jsonify({'msg': 'Success'})


@app.route('/notnotion/api/v0/profile/<int:user_id>', methods=['GET'])
async def profile(user_id):
    return jsonify(
        {
            'profile': 'User',
            'user_id': user_id
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
