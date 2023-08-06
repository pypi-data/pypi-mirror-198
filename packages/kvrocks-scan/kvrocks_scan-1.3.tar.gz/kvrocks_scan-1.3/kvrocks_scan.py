import redis
def parse_scan(response, **options):
	cursor, r = response
	if cursor == b"0" or cursor == "0":
		return int(cursor),r;
	return cursor, r

def parse_hscan(response, **options):
	cursor, r = response
	if cursor == b"0" or cursor == "0":
		return int(cursor),r and pairs_to_dict(r) or {};
	return cursor, r and pairs_to_dict(r) or {}


def parse_zscan(response, **options):
	score_cast_func = options.get("score_cast_func", float)
	cursor, r = response
	it = iter(r)
	if cursor == b"0" or cursor == "0":
		return int(cursor),list(zip(it, map(score_cast_func, it)));
	return cursor, list(zip(it, map(score_cast_func, it)))


redis.client.AbstractRedis.RESPONSE_CALLBACKS["SCAN"] = parse_scan;
redis.client.AbstractRedis.RESPONSE_CALLBACKS["SSCAN"] = parse_scan;
redis.client.AbstractRedis.RESPONSE_CALLBACKS["HSCAN"] = parse_hscan;
redis.client.AbstractRedis.RESPONSE_CALLBACKS["ZSCAN"] = parse_zscan;
