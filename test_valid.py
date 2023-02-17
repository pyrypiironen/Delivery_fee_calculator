import pytest
import json
from main import app


@pytest.fixture
def	generator():
	client = app.test_client()
	yield client


# In first part, valid delivery fee range is 0 to 15 so you can use test functions
# even after modified delivery fee calculator.

def	test_zero_cart_value(generator):
	input = {
		"cart_value": 0,
		"delivery_distance": 4200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_middle_cart_value(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 4200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_big_cart_value(generator):
	input = {
		"cart_value": 12000,
		"delivery_distance": 4200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_zero_delivery_distance(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 0,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_middle_delivery_distance(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 4200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_big_delivery_distance(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 14200,
		"number_of_items": 12,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_one_item(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_ten_items(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 10,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_fourtytwo_items(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 42,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200

def	test_min_values(generator):
	input = {
		"cart_value": 0,
		"delivery_distance": 0,
		"number_of_items": 1,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert 0 <= output['delivery_fee'] <= 1500
	assert response.status_code == 200


# In second part delivery fee required to be sharp so you cannot use these tests
# if delivery fee calculator has modified.

def	test_small_cart_value_surcharge(generator):
	input = {
		"cart_value": 800,
		"delivery_distance": 2200,
		"number_of_items": 7,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 850
	assert response.status_code == 200

def	test_bulk_surcharge(generator):
	input = {
		"cart_value": 800,
		"delivery_distance": 2200,
		"number_of_items": 15,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 1370
	assert response.status_code == 200

def	test_nb_of_items_surcharge(generator):
	input = {
		"cart_value": 800,
		"delivery_distance": 2200,
		"number_of_items": 6,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 800
	assert response.status_code == 200

def	test_only_delivery_distance_fee(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2021-10-12T13:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 500
	assert response.status_code == 200



# Third part is for testing rush hour multipier and time zone transitions.
# In this part delivery fee should always be 500 is there is no Friday rush and
# 600 if there is Friday rush.

def	test_basic_rush(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T17:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 600
	assert response.status_code == 200

def	test_rush_with_no_timezone_given(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T17:00:00"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 600
	assert response.status_code == 200

def	test_rush_160000(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T16:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 600
	assert response.status_code == 200

def	test_rush_190000(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T19:00:00Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 600
	assert response.status_code == 200

def	test_no_rush_190001(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T19:00:01Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 500
	assert response.status_code == 200

def	test_no_rush_thursday(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-02T17:42:42Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 500
	assert response.status_code == 200

def	test_no_rush_saturday(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-04T17:42:42Z"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 500
	assert response.status_code == 200

def	test_rush_different_tz(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T22:00:00+05:00"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 600
	assert response.status_code == 200

def	test_no_rush_different_tz(generator):
	input = {
		"cart_value": 1200,
		"delivery_distance": 2200,
		"number_of_items": 2,
		"time": "2023-02-03T17:00:00+05:00"
	}
	headers = {'Content-Type': 'application/json'}
	response = generator.post('/api/wolt/', data=json.dumps(input), headers=headers)
	output = json.loads(response.data)
	assert output['delivery_fee'] == 500
	assert response.status_code == 200
