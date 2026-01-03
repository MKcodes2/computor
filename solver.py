def polynomial_degree(poly: dict[int, float]) -> int:

	degree = 0
	for power, coef in poly.items():
		if coef != 0.0:
			if power > degree:
				degree = power

	return degree


def solve_degree_one(poly: dict[int, float]):
	"""
	Solves the `bx + c = 0` scenarios
	equivalent to: b * X^1 + c * X^0 = 0
	"""
	b = poly.get(1, 0.0)
	c = poly.get(0, 0.0)

def solve_polynomial(poly: dict[int, float]):

	degree = polynomial_degree(poly)
	print(f"Polynomial degree: {degree}")

	if degree > 2:
		print("The polynomial degree is strictly greater than 2, I can't solve.")
		return

	# to handle input like "42*X^0 = 42*X^0", "21*X^2 = 21*X^2" or "42*X^0 = 43*X^0"
	if degree == 0:
		if poly.get(0, 0.0) == 0.0:
			print("All real number are solutions")
		else:
			print("No solution")
		return
	
	# for the `bx + c = 0` scenarios, aka "b * X^1 + c * X^0 = 0"
	if degree == 1:
		b = poly[1]
		c = poly.get(0, 0.0)

		x = -c / b
		print("The solution is:")
		print(x)
		return