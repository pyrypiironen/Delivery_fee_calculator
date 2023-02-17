from flask import Flask, jsonify, request
from schema import schema
import jsonschema
import pytz
from datetime import datetime
from dateutil import parser


app = Flask(__name__)


@app.route('/api/wolt/', methods=['POST'])
def	main():
	error = error_handling()
	if (error):
		return jsonify(delivery_fee=error), 400

	data = request.get_json()

	delivery_fee = (distance_fee(data['delivery_distance']) \
					+ items_surcharge(data['number_of_items']) \
					+ small_order_surcharge(data['cart_value'])) \
					* rush_delivery_multiplier(data['time'])
	delivery_fee = verify_delivery_fee(delivery_fee, data['cart_value'])
	
	return jsonify(delivery_fee=int(delivery_fee)), 200


# Validate the data get from json. Return an error message if there is an error. 
def	error_handling():
	try:
		data = request.get_json()
		jsonschema.validate(instance=data, schema=schema)
		parser.parse(data['time'])
	except jsonschema.ValidationError as verror:
		return (f"Validation error: {verror}")
	except ValueError:
		return "Value error: time is not in ISO format."
	except Exception:
		return "Bad request"
	return None

# Count the delivery fee based on delivery distance. 2€ is base fee for first 1km
# and after that additional 1€ for every 500m (which has begun).
def	distance_fee(delivery_distance):
	fee = 200
	delivery_distance -= 1000
	while delivery_distance > 0:
		fee += 100
		delivery_distance -= 500
	return fee

# Count additional surcharge based on number of items. Both surcharges, the "bulk" fee and
# additional 50 cent for each item above and including the fifth item, will take in count. 
def	items_surcharge(number_of_items):
	fee = 0
	if number_of_items > 12:
		fee += 120
	number_of_items -= 4
	while number_of_items > 0:
		fee += 50
		number_of_items -= 1
	return fee

# Check if cart value is less than 10€ and return difference between cart value and
# 10€ if necessary.
def	small_order_surcharge(cart_value):
	fee = 0
	if cart_value < 1000:
		fee = 1000 - cart_value
	return fee

# Check if rush hours are going (fridays 3-7 PM UTC, including 19:00:00)
# and return multiplier based on that.
# Before that, set the timezone to UTC ("Europe/London"), then localize and normalize
# time (now), if timezone is given. Astimezone set the time to UTC and normalize correct
# possible ambiguities due to daylight saving time (DST) transitions.
# If timezone is not given, time is supposed to be in UTC already and will be used as it is.
def	rush_delivery_multiplier(time):
	now = parser.parse(time)
	if (now.tzinfo):
		utc = pytz.timezone("Europe/London")
		now = now.astimezone(utc)
		now = pytz.UTC.normalize(now)
	if (datetime.weekday(now) == 4) & (16 <= now.hour < 19) | \
		(datetime.weekday(now) == 4) & (now.hour == 19) & (now.minute == 0) & (now.second == 0):
		return 1.2
	else:
		return 1

# Check if the cart value is equal or more than 100€ in which case the delivery is free (0€).
# Then checks if the delivery fee is over 15€ and cut the fee to 15€ because it can never
# be more than 15€, including possible surcharges.
def	verify_delivery_fee(delivery_fee, cart_value):
	if cart_value >= 10000:
		delivery_fee = 0
	if delivery_fee > 1500:
		delivery_fee = 1500
	return delivery_fee


if __name__ == '__main__':
	app.run(port=5000)
