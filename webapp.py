from flask import Flask, request, jsonify
import unittest

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a + b})

@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a * b})

if __name__ == '__main__':
    app.run(debug=True)

# Unit Tests
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=3&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 7})
    
    def test_multiply(self):
        response = self.app.get('/multiply?a=3&b=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 12})

if __name__ == '__main__':
    unittest.main()
