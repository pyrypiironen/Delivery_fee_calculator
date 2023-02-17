# Delivery fee calculator

This is my delivery fee calculator based on Wolt Summer 2023 Engineering Internship preliminary assignment for backend position.

[The full assignment.](https://github.com/woltapp/engineering-summer-intern-2023)

## Preliminaries

To run this program you need `Python version 3.7` or newer and following modules:
- `flask`
- `schema`
- `jsonschema`
- `pytz`
- `datetime`
- `pytest`
- `json`
- `dateutil`


## Usage

Command `python3 main.py` start running the program.

### The request payload (JSON)

When the program is running, you can send POST request to `http://localhost:5000/api/wolt` on JSON format:


```
{
	"cart_value": 1200,
	"delivery_distance": 2200,
	"number_of_items": 2,
	"time": "2023-02-03T17:00:00+05:00"
}
```

- Request payload can include additional properties without causing error.
- Missing key-value pair or invalid value will cause error.
- Cart value and delivery distance can be zero on valid request payload, but number of items must be atleast 1.
- Time must be on ISO format. It can still be set to different timezone than UTC. In this case program will transit it to UTC.


### The response payload (JSON)


The calculated delivery fee or error message will be return on the response payload on JSON format:

```
{
	"delivery_fee": 710
}
```

or for example case of invalid ISO format.
```
{
	"delivery_fee": "Value error: time is not in ISO format."
}
```

### Response status codes

Response status code is 200 when request has succeeded and 400 if error message has been sent. These status codes has been used on test functions.


### Port

I use port 5000 to run locale server. If this port is blocked on your computer, change the code till example to 8000.



## Testing

There is separate test files to test that calculator works correct with valid request payloads and request payloads with errors.
Tests are build using pytest environment and can be run by following commands:
- `pytest test_valid.py -v`
- `pytest test_errors.py -v`
