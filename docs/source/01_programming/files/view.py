#!/usr/bin/env python 
from ase.io import read
from ase.visualize import view
import argparse as arg


parser = arg.ArgumentParser()
parser.add_argument('-pos',    help='xyz, pdb, cif, POSCAR, OUTCAR ...',nargs=1)


args = parser.parse_args()

a = read(args.pos[0],index=":")
view(a)

