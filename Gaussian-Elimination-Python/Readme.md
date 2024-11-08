# Gaussian Elimination with Reduced Row Echelon Form Solver

This Python script uses Gaussian elimination to solve systems of linear equations. It converts a user-input matrix into its **Row Echelon Form (REF)** and then its **Reduced Row Echelon Form (RREF)**, allowing it to identify solutions, free variables, or inconsistencies in the system.

## Features

- **User-Input Matrix**: Accepts a matrix from the user by specifying rows, columns, and individual entries.
- **Gaussian Elimination**: Transforms the matrix into Row Echelon Form (REF) to simplify solving.
- **Reduced Row Echelon Form (RREF)**: Further reduces the matrix to identify free variables and unique solutions.
- **Solution Identification**: 
  - Recognizes if the system is **consistent** or **inconsistent**.
  - Lists **unique solutions** or **free variables** if they exist.
  - Identifies **inconsistent rows** and reports that the system has no solutions if encountered.

## Getting Started

### Prerequisites

- **Python 3.x**
- **NumPy library**

Install NumPy with:
```bash
pip install numpy
```
## Running the Code
- Clone this repository or copy the code into a Python file (e.g., gaussian_elimination.py).
- Open a terminal, navigate to the file location, and run:
  ```bash
  python gaussian_elimination.py
  ```
## Input Instructions
- Enter the number of rows in the matrix when prompted.
- Enter the number of columns in the matrix.
- Enter each element of the matrix in sequence, row by row.
```diff
Please enter the rows of your matrix:
3
Please enter the columns of your matrix:
4
Enter each entry in one line:
1
2
-1
8
2
-3
4
-2
3
1
-4
3

```
## Sample Output
```lua
Echelon Form:
[[ 1.  2. -1.  8.]
 [ 0.  1.  0.  1.]
 [ 0.  0.  1.  3.]]

Reduced Echelon Form:
[[ 1.  0.  0.  2.]
 [ 0.  1.  0.  1.]
 [ 0.  0.  1.  3.]]

Answers of Matrix:
x 1 is 2.0
x 2 is 1.0
x 3 is 3.0
```
For an inconsistent system:
```csharp
system is inconsistent because
[0. 0. 0. 1.]
```
## License
This project is open-source and available for use under the [MIT License](https://opensource.org/licenses/MIT).

