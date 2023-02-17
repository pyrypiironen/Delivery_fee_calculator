schema = {
	"type": "object",
	"properties": {
		"cart_value":			{"type": "integer", "minimum": 0},
		"delivery_distance":	{"type": "integer", "minimum": 0},
		"number_of_items":		{"type": "integer", "minimum": 1},
		"time":					{"type": "string"}
		},
		"required": ["cart_value", "delivery_distance", "number_of_items", "time"],
		"additionalProperties": True
}
