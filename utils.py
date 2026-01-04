RESET  = "\033[0m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA = "\033[35m"
CYAN   = "\033[36m"
BOLD   = "\033[1m"

USE_COLOR = True

def color(text: str, c: str) -> str:
	if not USE_COLOR:
		return text
	return f"{c}{text}{RESET}"

def format_x(x: float) -> str:
	"""
	Subject shows 6 decimals in examples.
	Also I want to avoid "-0.000000".
	"""
	if abs(x) < EPS:
		x = 0.0
	return f"{x:.6f}".rstrip("0").rstrip(".") #formats for 6 digits after the decimal point, then it removes trailing zeros, and lastly removes trailing '.'


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




