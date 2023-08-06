import json

from .constants import city_fields


def cities_list(es_conn, query=None, size=None, source=None, redis_conn=None, pin_code=None):
	if pin_code:
		cities = get_city_from_pin_code(pin_code, es_conn, redis_conn)

	else:
		if query is None:
			query = {
				"match_all": {},
			}

		if size is None:
			size = 1000

		body = {
			"query": query,
			"size": size,
		}

		es_resp = es_conn.search(index="cities_index", doc_type="city", body=body, _source=source)
		hits = es_resp.get("hits", {}).get("hits", [])

		cities = []

		for hit in hits:
			source = hit.get("_source")

			if source:
				city = {field: source.get(field) for field in city_fields}
				cities.append(city)

	return cities


def get_city_from_pin_code(pin_code, es, redis):
	if redis:
		cached_city = redis.get(redis_pin_code_key(pin_code))
	else:
		cached_city = None

	if cached_city:
		cities = [json.loads(cached_city)]
	else:
		cities = cities_list(es, query={"terms": {"pincodes": [pin_code]}}, size=1)

		if cities:
			redis.set(redis_pin_code_key(pin_code), json.dumps(cities[0]))

	return cities


def redis_pin_code_key(pin_code):
	return f"city_pin_{pin_code}"
