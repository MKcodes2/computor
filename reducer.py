def reduce_polynomial(left: dict[int, float],
					right: dict[int, float]) -> dict[int, float]:
	
	reduced = {}

	# each side is already reduced, so i fill first the dictionary with the reduced left side:
	reduced = left.copy()

	# and then subtract right side
	for power, coef in right.items():
		reduced[power] = reduced.get(power, 0.0) - coef

	return reduced


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