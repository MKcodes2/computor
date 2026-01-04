from utils import *

def normalize_poly(poly: dict[int, float]) -> dict[int, float]:
	"""
	I use the EPS to handle extreme cases like: "0.1 * X^2 = 0.3 * X^2 - 0.2 * X^2"
	where without the comparsion to EPS it makes the coefficient 2.77556e-17 instead of 0 
	and gives wrong degrees. 
	"""
	out = poly.copy()
	for power, coef in out.items():
		if abs(coef) < EPS:
			out[power] = 0.0

	return out

def reduce_polynomial(left: dict[int, float],
					right: dict[int, float]) -> dict[int, float]:
	
	# each side is already reduced, so i fill first the dictionary with the reduced left side:
	reduced = left.copy()

	# and then subtract right side
	for power, coef in right.items():
		reduced[power] = reduced.get(power, 0.0) - coef

	return normalize_poly(reduced)


def format_reduced_form(poly: dict[int, float]) -> str:
	# Sorts by power ascending: X^0, X^1, X^2... (what the subject wants)
	items = sorted(poly.items(), key=lambda kv: kv[0]) # which is like saying “For each (power, coefficient) tuple, sort by power."
	# items = sorted(poly.items(), key=lambda kv: kv[0], reverse=True) # that would make more sense actually, but the pdf doesn't agree i guess

	#will never be met currently, but just in case i change anything in the future:
	if not items:
		return "0 = 0"
	
	result = ""

	for i, (power, coef) in enumerate(items):
		# I would normally do this too for the reduced form, but pdf doesn't want it -_-
		# if coef == 0.0:
		# 	continue

		# First term prints sign only if negative
		if i == 0:
			result += f"{coef:g} * X^{power}"# :g is the format specifier for the 5.000 to be written simply as 5 for example
		else:
			sign = "+" if coef >= 0 else "-"
			result += f" {sign} {abs(coef):g} * X^{power}"

	return result + " = 0"