def polynomial_degree(poly: dict[int, float]) -> int:

	degree = 0
	for power, coef in poly.items():
		if coef != 0.0:
			if power > degree:
				degree = power

	return degree


def solve_polynomial(poly: dict[int, float]):

	print("Polynomial degree:", polynomial_degree(poly))
