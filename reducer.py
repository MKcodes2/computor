def reduce_polynomial(left: dict[int, float],
					right: dict[int, float]) -> dict[int, float]:
	
	reduced = {}

	# each side is already reduced, so i fill first the dictionary with the reduced left side:
	reduced = left.copy()

	# and then subtract right side
	for power, coef in right.items():
		reduced[power] = reduced.get(power, 0.0) - coef

	return reduced


