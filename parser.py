def parse_equation(equation: str):
	# print("Received equation:", equation)

	equation = equation.strip() #trims unnecessary whitespaces

	sides = equation.split('=')
	if len(sides) != 2:
		raise ValueError("Equation must contain exactly one '='.")

	for side in sides:
		print(side)
