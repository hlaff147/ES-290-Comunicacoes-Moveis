from math import sqrt

T_A = (-8.04342, -34.952) # BTS_1
T_B = (-8.05289, -34.944672) # BTS_2
T_C = (-8.05532, -34.9579) # BTS_3

def search_a_guess(delay_a : int, delay_b : int, delay_c : int):
	"""This function searches a coordinate that could be a reasonable approximation based on the
	given delays from each tower centre"""
	lb_a, ub_a = 234 * (delay_a - 2), 234 * (delay_a+1) # distances lower bound and upper bound for a tower centre
	lb_b, ub_b = 234 * (delay_b - 2), 234 * (delay_b+1) # distances lower bound and upper bound for a tower centre
	lb_c, ub_c = 234 * (delay_c - 2), 234 * (delay_c+1) # distances lower bound and upper bound for a tower centre
	dist = lambda lat_0, lon_0, lat_t, lon_t : sqrt((lat_0 - lat_t)**2 + (lon_0 - lon_t)**2) * 111000.139 # dist in meters
	for lat_g in range(1, 140):
		for lon_g in range(1, 120):
			lat = lat_g / 10000  + T_C[0]
			lon = lon_g / 10000 + T_C[1]
			guess_a = dist(lat, lon, T_A[0], T_A[1])
			guess_b = dist(lat, lon, T_B[0], T_B[1])
			guess_c = dist(lat, lon, T_C[0], T_C[1])
			if ((lb_a <= guess_a <= ub_a) and 
       			(lb_b <= guess_b <= ub_b) and 
				(lb_c <= guess_c <= ub_c)):
				return lat,lon
	return -1,-1

lat, lon = search_a_guess(
	5,
	3,
	2
)

print(lat, lon)