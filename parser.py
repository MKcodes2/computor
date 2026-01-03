def parse_term(term: str) -> tuple[float, int]:
	"""
	Parses a single term to check for the form: <coef>*X^<power> (a * X^p)
	"Every term respect the form a * X^P" subjects says
	Example: "-9.3*X^2"
	Returns the tuple: (coef: float, power: int)
	"""
	# 0) initial check for empty term or missing characters
	if term == "" or len(term) < 5:
		raise ValueError(f"Invalid input.")
	# 1) Exactly one '*'
	if term.count("*") != 1:
		raise ValueError(f"Invalid term (expected one '*'): {term}")

	coef_part, var_part = term.split("*")
	# 2) Parse coefficient
	try:
		coef = float(coef_part)
	except ValueError:
		raise ValueError(f"Invalid coefficient in term: {term}")
	# 3) Variable must be X^<power>
	if not var_part.startswith("X^"):
		raise ValueError(f"Invalid variable format in term: {term}")

	power_part = var_part[2:]  # everything after the "X^"

	# 4) Power must be a positive integer
	if power_part == "":
		raise ValueError(f"Missing exponent in term: {term}")
	try:
		power = int(power_part)
	except ValueError:
		raise ValueError(f"Invalid exponent in term: {term}")
	if power < 0:
		raise ValueError(f"Negative exponent not allowed: {term}")

	return coef, power


def parse_side(side: str) -> dict[int, float]:
	# 1) we trim all the spaces:
	# side = side.replace(" ", "")
	side = "".join(side.split()) # to remove ALL whitespaces actually
	# 2) we convert the format "a - b + c - d" to "a + -b + c + -d"
	side = side.replace("-", "+-")
	# 2b) fix the edge case of the beginning with "+" so that i don't get the empty terms
	if side.startswith("+-") or side.startswith("+"):
		side = side[1:]
	# 3) split the side terms by the +:
	side_terms = side.split("+")
	side_poly: dict[int, float] = {}
	for term in side_terms:
		if term == "":
			# for something like "++" or trailing "+"
			raise ValueError("Invalid syntax: empty term (consecutive '+' or trailing '+').")

		coef, power = parse_term(term)  # <-- tuple unpacking

		# 4) accumulate by power (the user might give multiple entries for same X^P)
		side_poly[power] = side_poly.get(power, 0.0) + coef

	return side_poly


def parse_equation(equation: str) -> tuple[dict[int, float], dict[int, float]]:
	# print("Received equation:", equation)

	equation = equation.strip() #trims unnecessary whitespaces

	sides = equation.split('=')
	if len(sides) != 2:
		raise ValueError("Equation must contain exactly one '='.")
	
	side_dicts: list[dict[int, float]] = [] # one list to save the left side dictionary and right side dictionary

	for side in sides:
		side = side.strip()
		# print("side:", side, "$")
		if side == "":
			raise ValueError("One side is missing from the equation")
		if "^-" in side:
			raise ValueError("Only positive integer exponents expected")
		side_dicts.append(parse_side(side))

	# unpacks explicitly the two dictionaries 
	left_dict, right_dict = side_dicts

	return left_dict, right_dict
