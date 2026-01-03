def sqrt_newton(num: float) -> float:

	if num == 0.0:
		return 0.0

	if num < 0.0:
		raise ValueError("sqrt_newton expects non-negative input")

	# starting guess:
	if num >= 1.0: 
		guess = num # if x >= 1, starting at x is fine
	else:
		guess = 1.0 # f x < 1, starting at x would be too small -> division instability. 1.0 is always safe

	#newton's method coverges quickly.(~10 iterations -> very good precision, 100 is a bit of overkill, but i guess okay)
	for _ in range(100):
		new_guess = 0.5 * (guess + (num / guess))
		if abs(new_guess - guess) < 1e-12: # without EPS i would loop forever cause floats never become exact
			return new_guess
		guess = new_guess

	return guess
#
# For example:
# guess = 9
# new = (9 + 9/9)/2 = 5
# new = (5 + 9/5)/2 = 3.4
# new = (3.4 + 9/3.4)/2 ≈ 3.0235
# new = 3.00009
# new = 3.0000000001
# new = 3.0000000000000004
# new = 3.0
#

def polynomial_degree(poly: dict[int, float]) -> int:

	degree = 0
	for power, coef in poly.items():
		if coef != 0.0:
			if power > degree:
				degree = power

	return degree


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

	# for the `ax^2 + bx + c = 0` scenarios, aka "a * X^2 + b * X^1 + c * X^0 = 0"
	if degree == 2:
		a = poly[2]
		b = poly.get(1, 0.0)
		c = poly.get(0, 0.0)

	print(sqrt_newton(144))