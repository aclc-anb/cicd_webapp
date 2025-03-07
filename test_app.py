import pytest
from app import app
import json

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    
def test_submit_endpoint(client):
    """Test the submit endpoint with a name parameter"""
    test_data = {'name': 'TestUser'}
    response = client.post('/submit', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Hello, TestUser! Welcome to the Flask webapp.'

def test_submit_endpoint_no_name(client):
    """Test the submit endpoint without a name parameter"""
    test_data = {}
    response = client.post('/submit', 
                          data=json.dumps(test_data),
                          content_type='application/json')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Hello, Guest! Welcome to the Flask webapp.'

def test_404_page(client):
    """Test that 404 error handler works"""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404