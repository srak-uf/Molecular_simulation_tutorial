#!/usr/bin/env python 
import ase.io
import argparse as arg
from ase import Atoms

parser = arg.ArgumentParser()
parser.add_argument('-pos',   help='xyz, pdb, cif, POSCAR, OUTCAR ...',nargs=1)
parser.add_argument('-cell',  help='File (xyz, inp,...) with cell information', default=None)
parser.add_argument('-dt',    help="time step of trajectory (fs)", default=None)
parser.add_argument('-o',     help='xyz, cif, OUTCAR, POSCAR, pdb, etc...', default="py_ext.xyz")
parser.add_argument('-skip',  help='Only read every nr-th frame', type=int,default=1)
parser.add_argument('-atoms', nargs="*")

args = parser.parse_args()


skip = args.skip
e_xxx = ase.io.read(args.pos[0],index="::"+str(skip))

if args.dt is not None:
    dt = float(args.dt) 
    for i in range(len(e_xxx)):
        e_xxx[i].info["time"] = i*dt

selec = args.atoms
if selec is not None  and len(selec) >0:
    sel_trj = []
    for i in range(len(e_xxx)):
        temp_atoms = Atoms()
        for j in range(len(e_xxx[i])):
            if e_xxx[i][j].symbol in selec:
                temp_atoms.append(e_xxx[i][j])
        temp_atoms.cell = e_xxx[i].cell
        temp_atoms.pbc = e_xxx[i].pbc
        sel_trj.append(temp_atoms)
    e_xxx = sel_trj

if args.cell is not None:
    cell = ase.io.read(args.cell).cell
    for e in e_xxx:
        e.cell = cell
    
ase.io.write(args.o, e_xxx )


