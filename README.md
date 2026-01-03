# 🧮 ComputorV1 — A Polynomial Equation Solver

A command-line program that parses and solves polynomial equations of **degree ≤ 2**, written in **Python** without using _any_ math libraries.

This project is an implementation of the *ComputorV1* subject, focusing on:
- strict input parsing
- polynomial reduction
- numerical methods
- real and complex solutions

---

## ✨ Features

- Parses polynomial equations written in the form:  
  `a * X^p + b * X^q = c * X^r`
- Supports **floating-point coefficients**
- Reduces equations to canonical form
- Detects the **polynomial degree**
- Solves equations of:
  - degree **0**
  - degree **1**
  - degree **2**
- Handles:
  - two real solutions
  - one real solution
  - **two complex solutions**
- Uses a **custom square root implementation** (Newton’s method)
- Does **not** use the `math` module

---

## 🎯 Purpose

This project demonstrates:
- robust string parsing
- numerical stability with floating-point values
- correct handling of edge cases
- understanding of polynomial mathematics
- implementation of algorithms instead of relying on libraries

It intentionally avoids shortcuts such as `math.sqrt()` to reinforce algorithmic reasoning.

---

## 📥 Input Format

The program expects **one argument**: a polynomial equation as a string.

Each term **must** respect the format:
```
<coefficient> * X^<power>
```
Whitespace is allowed.

### ✔ Valid examples
```bash
"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
```

### ❌ Invalid examples
```bash
"5 + X^2 = 0"
"X^2 + 3X = 1"
```

## ▶️ How to Run

### 1️⃣ Make the program executable
```bash
chmod +x computor
```
### 2️⃣ Run from the terminal
```bash
./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```

#### 🖨 Example Output

##### Degree 2 — two real solutions
```bash
$ ./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
```

##### Degree 1 — one solution
```bash
$ ./computor "5 * X^0 + 4 * X^1 = 4 * X^0"

Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25
```

##### Degree 2 — two complex solutions
```bash
$ ./computor "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0"

Reduced form: 4 * X^0 + 3 * X^1 + 3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-0.5 + 1.040833 * i
-0.5 - 1.040833 * i
```

## 📁 Project Structure
```bash
computor/
├── computor          # Executable entry point
├── parser.py         # Equation parsing and validation
├── reducer.py        # Polynomial reduction and formatting
├── solver.py         # Degree detection and equation solving
├── README.md
```

## 🧠 Implementation Details

- Parsing
	- Splits equation into left/right sides
	- Parses each term as (`coefficient`, `power`)
	- Accumulates coefficients by power
- Reduction
	- Moves all terms to the left side
	- Normalizes floating-point noise using epsilon tolerance
- Solving
	- Degree 0: no solution or infinite solutions
	- Degree 1: linear equation
	- Degree 2: quadratic equation
		- real or complex roots depending on discriminant

- Square Root
	- Implemented using **Newton–Raphson method**
	- Stops when successive guesses converge within epsilon

## ⚠️ Constraints
- No usage of `math`, `cmath`, or numerical libraries
- Only basic arithmetic operations are used
- Floating-point precision handled manually
- Input must strictly follow the specified format

## 🧪 Tested Edge Cases
- Zero polynomial (`0 = 0`)
- Floating-point cancellation (`0.1 - 0.3 + 0.2`)
- Missing terms (`0 * X^n`)
- Complex discriminants
- High-degree detection (`degree > 2`)

## 📌 Notes
- The program prints zero coefficients in the reduced form to match the subject’s expected output.
- Polynomial degree is determined by the highest non-zero coefficient.