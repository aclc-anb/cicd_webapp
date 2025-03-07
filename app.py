from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name', 'Guest')
    return jsonify({
        'message': f'Hello, {name}! Welcome to the Flask webapp.'
    })

# Simple error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)