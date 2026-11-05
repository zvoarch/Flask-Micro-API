from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = [
    {"id":1,"campus":"MMC","lat":25.76057810,"lon":-80.36934121},
    {"id":2,"campus":"BBC","lat":25.90932603,"lon":-80.13842127},
]
next_id = 3

@app.route('/')
def index():
    return ("""<h1>Welcome to my First API</h1>
            <p>Try these routs: </p>
            <ul>
            <li><a href="/api/health">/api/health</a></li>
            <li><a href="/api/items">/api/items</a></li>
            <li><a href="/api/items/1">/api/items/1</a></li>""")

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/api/items', methods=['GET'])
def list_items():
    return jsonify(DATA),200

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in DATA:
        if item['id'] == item_id:
            return jsonify(item),200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)