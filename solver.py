EPS = 1e-12

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
		if abs(new_guess - guess) < EPS: # without EPS i would loop forever cause floats never become exact
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


def format_x(x: float) -> str:
	"""
	Subject shows 6 decimals in examples.
	Also I want to avoid "-0.000000".
	"""
	if abs(x) < EPS:
		x = 0.0
	return f"{x:.6f}".rstrip("0").rstrip(".") #formats for 6 digits after the decimal point, then it removes trailing zeros, and lastly removes trailing '.'


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
		print(format_x(x))
		return

	# for the `ax^2 + bx + c = 0` scenarios, aka "a * X^2 + b * X^1 + c * X^0 = 0"
	if degree == 2:
		a = poly[2] # non-zero when degree == 2
		b = poly.get(1, 0.0)
		c = poly.get(0, 0.0)

		delta = b * b - 4.0 * a * c

		if delta > EPS:
			print("Discriminant is strictly positive, the two solutions are:")
			sqrt_d = sqrt_newton(delta)
			x1 = (-b + sqrt_d) / (2.0 * a)
			x2 = (-b - sqrt_d) / (2.0 * a)
			print(format_x(x1))
			print(format_x(x2))
			return

		if abs(delta) <= EPS: # meaning if it's zero ("anything extremely close to 0")
			print("Discriminant is zero, the solution is:")
			x = (-b) / (2.0 * a)
			print(x)
			return

		if delta < 0.0:
			print("Discriminant is strictly negative, the two complex solutions are:")
			sqrt_d_abs = sqrt_newton(-delta)
			real_part = (-b) / (2.0 * a)
			imag_part = sqrt_d_abs / (2.0 * a)

			# prints the two solutions: real_part ± imag_part*i
			print(f"{format_x(real_part)} + {format_x(abs(imag_part))} * i")
			print(f"{format_x(real_part)} - {format_x(abs(imag_part))} * i")

			#the non-formatted output:
			# print(f"{real_part} + {abs(imag_part)} * i")
			# print(f"{real_part} - {abs(imag_part)} * i")



