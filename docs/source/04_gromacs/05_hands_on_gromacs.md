# Hands-on GROMACS
under construction

3. Analyze MD trajectory  
   GROMACS has many post analysis functions. Please check the [Command-line reference](https://manual.gromacs.org/2024.4/user-guide/cmdline.html).

   1. Index file (`.ndx`): This is used to specify the atoms, which is useful for MD analysis.  
        ```
        # Get N of nitrile and Li
        gmx make_ndx -f hoge.tpr -n Li_N.ndx
        ...
        ...
        0 System              :  4500 atoms
        1 Other               :  4500 atoms
        2 M1                  :  1350 atoms
        3 M2                  :  3000 atoms
        4 M3                  :   150 atoms

        nr : group      '!': not  'name' nr name   'splitch' nr    Enter: list groups
        'a': atom       '&': and  'del' nr         'splitres' nr   'l': list residues
        't': atom type  '|': or   'keep' nr        'splitat' nr    'h': help
        'r': residue              'res' nr         'chain' char
        "name": group             'case': case sensitive           'q': save and quit
        'ri': residue index
        ...
        ...
        > 3 & t N2
        > q
        ```
        - 3 & t N2
            - 3 = M2
            - t = atom type, N2 is the nitrile atom type as denoted in top file
   2. Radial distribution function
        ```
        # gmx rdf "-h" shows the help of the command
        gmx rdf -f nvt.trr -s nvt.tpr -n Li_N.ndx -o Li_N.xvg
        > 4
        > 5
        ctrl+d
        ```
        - `-b` command-line should be used to skip trajectories at the beginning that have not reached equilibrium.
        - `-cn` can evaluate the coordination number. 
   3. MSD  
        ```bash
        gmx msd -f nvt.trr -s nvt.tpr -o Li.xvg
        ...
        ...
        Reading file nvt.tpr, VERSION 2023.4-conda_forge (single precision)
        Reading file nvt.tpr, VERSION 2023.4-conda_forge (single precision)
        Available static index groups:
        Group  0 "System" (4500 atoms)
        Group  1 "Other" (4500 atoms)
        Group  2 "M1" (1350 atoms)
        Group  3 "M2" (3000 atoms)
        Group  4 "M3" (150 atoms)
        Specify any number of selections for option 'sel'
        (Selections to compute MSDs for from the reference):
        (one per line, <enter> for status/groups, 'help' for help, Ctrl-D to end)
        > 4
        ```
        `crtl` + `d` or `command` + `d` to finish the selection.
