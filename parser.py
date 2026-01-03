def parse_each_side(side: str) -> dict[int, float]:
	# 1) we trim all the spaces:
	side = side.replace(" ", "")
	# 2) we convert the format "a - b + c - d" to "a + -b + c + -d"
	side = side.replace("-", "+-")
	# 2b) fix the edge case of the beginning with "-"
	if side.startswith("+-"):
		side = side[1:]
	# 3) split the side parts by the +:
	side_parts = side.split("+")

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
	
	# converts the "a - b + c - d" to "a + -b + c + -d" to safely split then by "+"
