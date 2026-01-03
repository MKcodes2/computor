def parse_term(term: str) -> tuple[float, int]:
	"""
	Parses a single term to check for the form: <coef>*X^<power> (a * X^p)
	"Every term respect the form a * X^P" subjects says
	Example: "-9.3*X^2"
	Returns the tuple: (coef: float, power: int)
	"""
	# 0) initial check for empty term or missing characters
	if term == "" or len(term) < 5:
		raise ValueError(f"Invalid term (doesn't follow the patern \"a * X^P\"):  {term}")
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

	# 4) Power must be integer
	if power_part == "":
		raise ValueError(f"Missing exponent in term: {term}")
	try:
		power = int(power_part)
	except ValueError:
		raise ValueError(f"Invalid exponent in term: {term}")
	if power < 0:
		raise ValueError(f"Negative exponent not allowed: {term}")
	# if power > 2 and not float(coef_part):
	# 	print("The polynomial degree is strictly greater than 2, I can't solve.")
	# 	sys.exit(1)

	return coef, power


def parse_side(side: str) -> dict[int, float]:
	# 1) we trim all the spaces:
	side = side.replace(" ", "")
	# 2) we convert the format "a - b + c - d" to "a + -b + c + -d"
	side = side.replace("-", "+-")
	# 2b) fix the edge case of the beginning with "+" so that i don't get the empty terms
	if side.startswith("+-") or side.startswith("+"):
		side = side[1:]
	# 3) split the side terms by the +:
	side_terms = side.split("+")
	for term in side_terms:
		parse_term(term)


	poly_dict: dict[int, float] = {}
	return poly_dict


def parse_equation(equation: str):
	# print("Received equation:", equation)

	equation = equation.strip() #trims unnecessary whitespaces

	sides = equation.split('=')
	if len(sides) != 2:
		raise ValueError("Equation must contain exactly one '='.")
	
	# my main polyonym dictionary to fill:
	poly_dict: dict[int, float] = {} # equivalent to the `std::map<int, double> poly;` i knew

	for side in sides:
		side = side.strip()
		print("side:", side, "$")
		if side is None or side == "":
			raise ValueError("One side is missing from the equation")
		if "^-" in side:
			raise ValueError("Only positive integer exponents expected")
		poly_dict = parse_side(side)
	
