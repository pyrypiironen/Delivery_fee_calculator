import pytest
import json
from main import app


@pytest.fixture
def	generator():
	client = app.test_client()
	yield client


def	test_invalid_cart_value(generator):
	input = {
		"cart_value": -1,
		"delivery_distance": 4200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_delivery_distance(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": -1,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_nb_of_items(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"number_of_items": 0,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_ISO_format(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"number_of_items": 7,
		"time": "17 PM utc"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_cart_value_format(generator):
	input = {
		"cart_value": "FourFourTwo",
		"delivery_distance": 4200,
		"number_of_items": 7,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_delivery_distance_format(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": "Far far away",
		"number_of_items": 7,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_nb_of_items_format(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"number_of_items": 4.2,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_invalid_time_format(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"number_of_items": 4,
		"time": 17
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_no_cart_value(generator):
	input = {
		"delivery_distance": 4200,
		"number_of_items": 4,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_no_delivery_distance(generator):
	input = {
		"cart_value": 420,
		"number_of_items": 4,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_no_nb_of_items(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_no_time(generator):
	input = {
		"cart_value": 420,
		"delivery_distance": 4200,
		"number_of_items": 4
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400

def	test_empty_json(generator):
	input = {
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	assert response.status_code == 400
