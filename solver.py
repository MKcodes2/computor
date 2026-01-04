from utils import *

def polynomial_degree(poly: dict[int, float]) -> int:

	degree = 0
	for power, coef in poly.items():
		if coef != 0.0:
			if power > degree:
				degree = power

	return degree


def solve_polynomial(poly: dict[int, float]):

	degree = polynomial_degree(poly)
	print(color(f"Polynomial degree: {degree}", MAGENTA))

	if degree > 2:
		print(color("🛑 The polynomial degree is strictly greater than 2, I can't solve.", RED))
		return

	# to handle input like "42*X^0 = 42*X^0", "21*X^2 = 21*X^2" or "42*X^0 = 43*X^0"
	if degree == 0:
		if poly.get(0, 0.0) == 0.0:
			print(color("❇️ All real number are solutions", GREEN))
		else:
			print(color("❌ No solution possible", RED))
		return
	
	# for the `bx + c = 0` scenarios, aka "b * X^1 + c * X^0 = 0"
	if degree == 1:
		b = poly[1]
		c = poly.get(0, 0.0)

		x = -c / b
		print(color("The solution is:", BLUE))
		print(color(f"{format_x(x)}", GREEN))
		return

	# for the `ax^2 + bx + c = 0` scenarios, aka "a * X^2 + b * X^1 + c * X^0 = 0"
	if degree == 2:
		a = poly[2] # non-zero when degree == 2
		b = poly.get(1, 0.0)
		c = poly.get(0, 0.0)

		delta = b * b - 4.0 * a * c

		if delta > EPS:
			print(
				f"{color('Discriminant is strictly', BLUE)} "
				f"{color('positive', BOLD + BLUE)} "
				f"{color('the two solutions are:', BLUE)}"
			)
			sqrt_d = sqrt_newton(delta)
			x1 = (-b + sqrt_d) / (2.0 * a)
			x2 = (-b - sqrt_d) / (2.0 * a)
			print(color(f"{format_x(x1)}", GREEN))
			print(color(f"{format_x(x2)}", GREEN))
			return

		if abs(delta) <= EPS: # meaning if it's zero ("anything extremely close to 0")
			print(
				f"{color('Discriminant is ', BLUE)}"
				f"{color('zero', BOLD + BLUE)}"
				f"{color(', the solution is:', BLUE)}"
			)
			x = (-b) / (2.0 * a)
			print(color(f"{format_x(x)}", GREEN))
			return

		if delta < 0.0:
			print(
				f"{color('Discriminant is strictly', BLUE)} "
				f"{color('negative', BOLD + BLUE)} "
				f"{color('the two complex solutions are:', BLUE)}"
			)
			sqrt_d_abs = sqrt_newton(-delta)
			real_part = (-b) / (2.0 * a)
			imag_part = sqrt_d_abs / (2.0 * a)

			# prints the two solutions: real_part ± imag_part*i
			print(color(f"{format_x(real_part)} + {format_x(abs(imag_part))} * i", CYAN))
			print(color(f"{format_x(real_part)} - {format_x(abs(imag_part))} * i", CYAN))

