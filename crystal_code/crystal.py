import numpy as np
from ase import Atoms

class Crystal:
    """
    Represents a crystal defined by (X, A, L)
    - X: fractional coordinates (3×n)
    - A: atom types list of length n
    - L: lattice matrix (3×3)
    """

    def __init__(self, X, A, L):
        self.X = np.array(X, dtype=float)
        self.A = list(A)
        self.L = np.array(L, dtype=float)
        self.n = len(A)

    def cartesian_positions(self):
        """Return Cartesian coordinates (Å)."""
        return self.L @ self.X

    def volume(self):
        """Return the unit cell volume."""
        return abs(np.linalg.det(self.L))

    def to_ase(self):
        """Convert to an ASE Atoms object."""
        return Atoms(symbols=self.A, scaled_positions=self.X.T, cell=self.L, pbc=True)

    def save_cif(self, filename="crystal.cif"):
        """Export the structure to a CIF file."""
        atoms = (self.

                 to_ase())
        atoms.write(filename)
        print(f"✅ CIF saved as {filename}")

    def __repr__(self):
        return f"<Crystal n={self.n}, volume={self.volume():.3f} Å³>"
