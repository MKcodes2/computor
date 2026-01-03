# computor
A second-degree polynomials' solver in Python

Architecture of the files:
```
computor/
  computor          # executable entrypoint (no extension)
  computor.py       # main CLI (arg parsing + printing)
  parser.py         # parse equation -> polynomial dict
  reducer.py        # move right to left, combine, format reduced form
  solver.py         # degree detection + solve (0/1/2)
  math_utils.py     # your own sqrt + float helpers (no math module)
```

More analytically:
- computor
Tiny executable wrapper (or a shebang Python script). Goal: evaluator runs ./computor "...".

- computor.py
The “main.cpp” equivalent:
	- reads sys.argv[1]
	- calls parse_equation(...)
	- calls reduce(...)
	- prints reduced form + degree
	- calls solver + prints solutions

- parser.py
Only parsing concerns:
	- splis by =
	- parses a side like "5 * X^0 + 4 * X^1 - 9.3 * X^2"
	- returns dictionary: {power: coeff}

- reducer.py
	- subtracts right-side dict from left-side dict
	- cleans near-zero coefficients
	- computes degree
	- builds the exact output string: Reduced form: ... = 0

- solver.py
`solve(poly_dict)` returns a structured result:
	- degree
	- discriminant (if degree 2)
	- list of solutions (real or complex as strings or tuples)

- math_utils.py
	- sqrt_newton(x) (my own cause we can not call math module)
	- is_zero(x, eps=1e-12)
	- maybe format_number(x) to avoid ugly -0.0
