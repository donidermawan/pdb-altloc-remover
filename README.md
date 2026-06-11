# pdb-altloc-remover

A Python tool for detecting and removing alternate atomic conformations (AltLocs) in protein PDB files. Retains only the primary conformer (AltLoc A), removes alternative conformations (B, C, D, ...), and renumbers atom serial numbers for clean structure preparation and molecular modeling workflows.

## 1. Features

* Automatically detects alternate location identifiers (AltLocs)
* Retains only the primary conformer (AltLoc A)
* Removes alternative conformers (B, C, D, ...)
* Preserves atoms without alternate locations
* Removes AltLoc labels from retained atoms
* Renumbers atom serial numbers sequentially
* Maintains valid PDB formatting
* Produces cleaner structures for downstream applications

---

## 2. Requirements

* Python ≥ 3.8

No external Python packages are required.

---

## 3. Installation

### Clone the Repository

```bash
git clone https://github.com/donidermawan/pdb-altloc-remover.git
cd pdb-altloc-remover
```

### Or Download Directly

Download `remove_altloc.py` and place it in your working directory.

No installation is necessary.

---

## 4. Usage

Run the script by providing a protein PDB file as input:

```bash
python remove_altloc.py protein.pdb
```

### Output

The script generates a new PDB file:

```text
protein_altlocA.pdb
```

### Output Characteristics

* Only one conformer retained
* AltLoc identifiers removed
* Continuous atom serial numbering
* Original coordinates preserved
* Compatible with molecular docking and simulation software

---

## 5. Example

### Input

```text
ATOM    112  CA AVAL A1018 ...
ATOM    113  CA BVAL A1018 ...
ATOM    116  CB AVAL A1018 ...
ATOM    117  CB BVAL A1018 ...
```

### Command

```bash
python remove_altloc.py protein.pdb
```

### Output

```text
ATOM    112  CA  VAL A1018 ...
ATOM    113  CB  VAL A1018 ...
```

### Console Output

```text
Output written to: protein_altlocA.pdb
```

---

## 6. Important Notes

* Atoms with no alternate location identifier are preserved
* Only AltLoc A is retained when multiple conformations exist
* AltLoc labels are removed from retained atoms
* Coordinates and residue numbering remain unchanged
* Alternative conformations (B, C, D, etc.) are discarded
* Atom serial numbers are renumbered sequentially
* Intended for technical preprocessing rather than structural modification

---

## 7. Use Cases

* Preparing protein structures for molecular docking
* Cleaning crystal structures before molecular dynamics simulations
* Standardizing structures from the Protein Data Bank (PDB)
* Removing alternate side-chain conformations
* Simplifying structures for structure-based drug design
* Improving compatibility with HADDOCK, AutoDock, AutoDock Vina, Glide, GROMACS, AMBER, CHARMM, and related software

---

## Author

**Doni Dermawan**

GitHub: https://github.com/donidermawan

---
