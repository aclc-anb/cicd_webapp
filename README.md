# cicd_webapp

Flask Web App with Unit Tests

This is a simple Flask web application that provides two endpoints for basic arithmetic operations (addition and multiplication). It also includes unit tests using Python's unittest framework.

Features

GET /add?a=<num>&b=<num>: Returns the sum of a and b.

GET /multiply?a=<num>&b=<num>: Returns the product of a and b.

Installation

Clone the repository:

git clone <repository_url>
cd <repository_folder>

Install dependencies:

pip install flask

Running the Application

Start the Flask server:

python app.py

The server will run at http://127.0.0.1:5000/.

Running the Tests

Run the unit tests with:

python -m unittest app.py

Example Usage

Adding two numbers:

curl "http://127.0.0.1:5000/add?a=3&b=4"

Response: { "result": 7 }

Multiplying two numbers:

curl "http://127.0.0.1:5000/multiply?a=3&b=4"

Response: { "result": 12 }

License

This project is open-source and free to use.

MIT License

Copyright (c) 2025 aclc-anb



Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.
