#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Usage: python remove_altloc.py protein.pdb")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + "_altlocA.pdb"

new_serial = 1

with open(input_file, "r") as fin, open(output_file, "w") as fout:

    for line in fin:

        if not line.startswith(("ATOM  ", "HETATM")):
            fout.write(line)
            continue

        altloc = line[16]

        # Keep atoms with no alternate location
        if altloc == " ":
            pass

        # Keep only conformer A
        elif altloc == "A":
            pass

        # Discard B, C, D, ...
        else:
            continue

        # Remove altloc identifier
        line = line[:16] + " " + line[17:]

        # Renumber atom serial
        line = f"{line[:6]}{new_serial:5d}{line[11:]}"
        new_serial += 1

        fout.write(line)

print(f"Output written to: {output_file}")