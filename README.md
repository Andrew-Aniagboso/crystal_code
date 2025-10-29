<p align="center">
  <img src="images/crystal_code_banner.png" width="800" alt="crystal_code banner">
</p>

# 🧱 crystal_code

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="License: MIT"> (LICENSE)
  <img src="https://img.shields.io/badge/platform-macOS%20|%20Linux%20|%20Windows-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions">
  <img src="https://img.shields.io/github/last-commit/Andrew-Aniagboso/crystal_code?color=blue&label=Last%20Commit" alt="Last Commit">
</p>

---

A Python project for representing and visualizing crystal structures using the notation  
**M = (X, A, L)** → atomic coordinates, atom types, and lattice.

---

## 📘 Overview

`crystal_code` helps students and researchers understand how crystals are built from three fundamental components:

- **X:** Fractional coordinates of atoms within the unit cell  
- **A:** Atom types (chemical species)  
- **L:** 3×3 lattice vectors defining the crystal shape

Together, these components define any crystalline material.

---

## 🧪 Example: NaCl Crystal

```bash
from crystal_code.crystal import Crystal

# Define atomic positions (fractional coordinates)
X = [[0, 0, 0], [0.5, 0.5, 0.5]]

# Define atom types
A = ["Na", "Cl"]

# Define cubic lattice vectors (in Å)
L = [
    [5.64, 0.0, 0.0],
    [0.0, 5.64, 0.0],
    [0.0, 0.0, 5.64]
]


# Create the crystal structure object
M = Crystal(X, A, L)

# Save the structure to a CIF file
M.save_cif("NaCl.cif")
```
This code generates a simple NaCl (rock-salt) crystal structure that can be viewed using ASE or VESTA.

## Installation
```bash
git clone https://github.com/Andrew-Aniagboso/crystal_code.git
cd crystal_code
pip install -r requirements.txt
```

## Usage
case1: Creating and saving a crystal structure to a CIF file
Import the `Crystal` class and create crystal structures by providing atomic coordinates, atom types, and
lattice vectors. Use the `save_cif` method to export the structure to a CIF file.   
Refer to the example above for guidance.

case2: Running the example notebook
Run the example code to generate a CIF file for the NaCl crystal structure.Once installed, open the example notebook:

how to run:

```bash
jupyter notebook notebooks/demo.ipynb
```
Or run directly in PyCharm using the integrated Jupyter support.


## visualization
case1: Visualizing CIF files
You can visualize the generated CIF files using tools like ASE or VESTA. Simply open the CIF file in your preferred visualization software to explore the crystal structure.

case2: Using ASE for visualization
You can also use ASE to visualize the crystal structure directly in Python:
```bash
ase gui notebooks/NaCl.cif
```
You can rotate, zoom, and inspect the 3D atomic arrangement interactively.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

####  License
This project is released under the **MIT License**.
