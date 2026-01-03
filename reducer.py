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
	#will never be met currently, but just in case i change anything in the future:
	if not items:
		return "0 = 0"
	
	parts: list[str] = [] #empty list, but annotates that is intended to contain strings

	for i, (power, coef) in enumerate(items):
		# I would normally do this too, but pdf doesn't want it -_-
		# if coef == 0.0:
		# 	continue

		# First term prints sign only if negative
		if i == 0:
			parts.append(f"{coef:g} * X^{power}") # :g is the format specifier for the 5.000 to be written simply as 5 for example
		else:
			sign = "+" if coef >= 0 else "-"
			parts.append(f"{sign} {abs(coef):g} * X^{power}")

	return " ".join(parts) + " = 0"