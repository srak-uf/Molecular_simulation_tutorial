# Input Files
## Overview
```{note}
This note includes only knowhow to perfom molecular dynamics by GROMACS. You should read the [GROMACS manual](https://manual.gromacs.org/) carefully and understand the mean of parameters.  
```

There are three key input files needed to run a GROMACS calculation:  
1. `.mdp`: Molecular Dynamics Parameter  (ex. timestep, temperature, and so on) 
   - [Official manual](https://manual.gromacs.org/current/user-guide/mdp-options.html)
2. `.top`: System topology (force field assignment)
   - [Official manual](https://manual.gromacs.org/current/reference-manual/topologies/topology-file-formats.html)
3. `.gro`: Structure file
   - [Official manual](https://manual.gromacs.org/current/reference-manual/file-formats.html#gro)

Generate the binary file `.tpr` to run a MD by converting the above files.   
`.tpr` has infomation about system topology, parameters, coordinates and velocities

### Energy minimization
- <details>
    <summary>mdp example</summary>

    ###
    ```
    integrator              = steep  ; steep | md | md-vv
    nsteps                  = 4096
    emtol                   = 100.0  ; steep option kJ mol-1 nm-1, converged when the maximum force is smaller
    emstep                  = 0.01   ; steep option nm, initial step-size
    pbc                     = xyz
    coulombtype             = PME    ; Cut-off | PME | P3M-AD
    coulomb-modifier        = None
    rcoulomb                = 1.2
    vdwtype                 = Cut-off   ; Cut-off | PME | P3M-AD
    vdw-modifier            = None
    rvdw                    = 1.2
    constraints             = all-bonds           ; all-bonds | h-bonds
    constraint-algorithm    = LINCS
    nstxout                 = 10
    nstvout                 = 10
    nstenergy               = 10
    nstxout-compressed      = 0
    compressed-x-grps       = 
    nstlist                 = 10
    ns-type                 = grid
    cutoff-scheme           = Verlet
    verlet-buffer-tolerance = -1
    rlist                   = 1.4
    fourierspacing          = 0.12
    pme-order               = 6
    ewald-rtol              = 1e-8
    DispCorr                = EnerPres
    lincs-order             = 8
    lincs-iter              = 2
    continuation            = no
    define                  = 
    print-nose-hoover-chain-variables = yes

    nstcalcenergy           = 10
    ```
</details>

### NVT ensemble
- Nose-Hoover thermostat is used to control temperature
- If the system is unstable or fails the NVT calculation, the below procedures will be helpful. 
    - Decrease temperature
    - Use Berendsen thermostat
    - Decrease dt  
- <details>
    <summary>mdp example</summary>

    ###
    ```
    gen-vel                 = yes
    gen-seed                = 12345
    gen-temp                = 300
    comm-mode               = Linear
    nstcomm                 = 50
    integrator              = md     ; steep | md | md-vv
    dt                      = 0.002  ; ps
    nsteps                  = 500000
    pbc                     = xyz
    coulombtype             = PME    ; Cut-off | PME | P3M-AD
    coulomb-modifier        = None
    rcoulomb                = 1.2
    vdwtype                 = Cut-off   ; Cut-off | PME | P3M-AD
    vdw-modifier            = None
    rvdw                    = 1.2
    tcoupl                  = nose-hoover   ;  berendsen | nose-hoover | v-rescale
    tc-grps                 = System
    tau-t                   = 1.0
    ref-t                   = 300
    nsttcouple              = 10 
    nh-chain-length         =  3
    pcoupl                  = no  ; no | Berendsen | Parrinello-Rahman
    pcoupltype              = isotropic           ; isotropic | semiisotropic (x/y vs z) | anisotropic
    tau-p                   = 1.0
    compressibility         = 4.5e-5
    ref-p                   = 5.0                 ; [bar]
    nstpcouple              = -1
    refcoord-scaling        = no
    constraints             = all-bonds           ; all-bonds | h-bonds
    constraint-algorithm    = LINCS
    nstxout                 = 1000
    nstvout                 = 1000
    nstenergy               = 1000
    nstxout-compressed      = 0
    compressed-x-grps       = 
    nstlist                 = 10
    ns-type                 = grid
    cutoff-scheme           = Verlet
    verlet-buffer-tolerance = -1
    rlist                   = 1.4
    fourierspacing          = 0.12
    pme-order               = 6
    ewald-rtol              = 1e-8
    DispCorr                = EnerPres
    lincs-order             = 6
    lincs-iter              = 2
    continuation            = no
    define                  = 
    print-nose-hoover-chain-variables = yes

    nstcalcenergy           = 10
    nstlog                  = 1000
    ```
</details>


### NpT ensemble
#### Liquid system
- *NpT* of amorphous system are usually perfomred by **isotropic** *NpT*.
- If the system is unstable or fails the *NpT* calculation, the below procedures will be helpful. 
    - Decrease temperature
    - Use Berendsen thermostat and barostat
    - Decrease dt  
- *NpT* calculations are mainly used to get the equilibrium density (volume) for following *NVT* production run.
    ```{tip}
    You can get the equilibrium cell length by gmx energy command.  
    The final structure should be scaled to make the cell lenggth the equilibrated one. 
    gmx editconf with -scale option and ASE are useful. 
    ```
- <details>
    <summary>mdp example</summary>

    ```
    gen-vel                 = no
    gen-seed                = -1
    gen-temp                = 300
    comm-mode               = Linear
    nstcomm                 = 50
    integrator              = md  ; steep | md | md-vv
    dt                      = 0.002
    nsteps                  = 100000000
    pbc                     = xyz
    coulombtype             = PME ; Cut-off | PME | P3M-AD
    coulomb-modifier        = None
    rcoulomb                = 1.2
    vdwtype                 = Cut-off   ; Cut-off | PME | P3M-AD
    vdw-modifier            = None
    rvdw                    = 1.2
    tcoupl                  = nose-hoover   ;  berendsen | nose-hoover | v-rescale
    tc-grps                 = System
    tau-t                   = 1.0
    ref-t                   = 300
    nsttcouple              = 10
    nh-chain-length         = 10
    pcoupl                  = Parrinello-Rahman  ; no | Berendsen | Parrinello-Rahman
    pcoupltype              = isotropic          ; isotropic | semiisotropic (x/y vs z) | anisotropic
    tau-p                   = 5.0
    compressibility         = 4.5e-5 4.5e-5 4.5e-5 0 0 0
    ref-p                   = 1.0  ; [bar]
    nstpcouple              = 10
    refcoord-scaling        = no
    constraints             = all-bonds           ; all-bonds | h-bonds
    constraint-algorithm    = LINCS
    nstxout                 = 1000
    nstvout                 = 1000
    nstenergy               = 1000
    nstxout-compressed      = 0
    compressed-x-grps       = 
    nstlist                 = 10
    ns-type                 = grid
    cutoff-scheme           = Verlet
    verlet-buffer-tolerance = -1
    rlist                   = 1.4
    fourierspacing          = 0.12
    pme-order               = 6
    ewald-rtol              = 1e-8
    DispCorr                = EnerPres
    lincs-order             = 6
    lincs-iter              = 2
    continuation            = no
    define                  = 
    print-nose-hoover-chain-variables = yes

    nstcalcenergy           = 10
    nstlog                  = 1000
    ```
</details>

#### Crystal system
- Anisotropic (Box changes along x, y, z direction independently) or triclinic (Box changes along x, y, z, xy, yz, zx direction independently) *NpT* are used for crystal system.
- <details>
    <summary>mdp example for anisotropic NpT</summary>

    ```
    gen-vel                 = no
    gen-seed                = -1
    gen-temp                = 300
    comm-mode               = Linear
    nstcomm                 = 50
    integrator              = md  ; steep | md | md-vv
    dt                      = 0.002
    nsteps                  = 100000000
    pbc                     = xyz
    coulombtype             = PME ; Cut-off | PME | P3M-AD
    coulomb-modifier        = None
    rcoulomb                = 1.2
    vdwtype                 = Cut-off   ; Cut-off | PME | P3M-AD
    vdw-modifier            = None
    rvdw                    = 1.2
    tcoupl                  = nose-hoover   ;  berendsen | nose-hoover | v-rescale
    tc-grps                 = System
    tau-t                   = 1.0
    ref-t                   = 300
    nsttcouple              = 10
    nh-chain-length         = 10
    pcoupl                  = Parrinello-Rahman  ; no | Berendsen | Parrinello-Rahman
    pcoupltype              = anisotropic           ; isotropic | semiisotropic (x/y vs z) | anisotropic
    tau-p                   = 5.0
    compressibility         = 4.5e-5 4.5e-5 4.5e-5 0.0 0.0 0.0
    ref-p                   = 1.0 1.0 1.0 0.0 0.0 0.0                ; [bar]
    nstpcouple              = 10
    refcoord-scaling        = no
    constraints             = all-bonds           ; all-bonds | h-bonds
    constraint-algorithm    = LINCS
    nstxout                 = 1000
    nstvout                 = 1000
    nstenergy               = 1000
    nstxout-compressed      = 0
    compressed-x-grps       = 
    nstlist                 = 10
    ns-type                 = grid
    cutoff-scheme           = Verlet
    verlet-buffer-tolerance = -1
    rlist                   = 1.4
    fourierspacing          = 0.12
    pme-order               = 6
    ewald-rtol              = 1e-8
    DispCorr                = EnerPres
    lincs-order             = 6
    lincs-iter              = 2
    continuation            = no
    define                  = 
    print-nose-hoover-chain-variables = yes

    nstcalcenergy           = 10
    nstlog                  = 1000
    ```
</details>

- <details>
    <summary>mdp example for triclinic NpT</summary>

    ```
    gen-vel                 = no
    gen-seed                = -1
    gen-temp                = 300
    comm-mode               = Linear
    nstcomm                 = 50
    integrator              = md  ; steep | md | md-vv
    dt                      = 0.002
    nsteps                  = 100000000
    pbc                     = xyz
    coulombtype             = PME ; Cut-off | PME | P3M-AD
    coulomb-modifier        = None
    rcoulomb                = 1.2
    vdwtype                 = Cut-off   ; Cut-off | PME | P3M-AD
    vdw-modifier            = None
    rvdw                    = 1.2
    tcoupl                  = nose-hoover   ;  berendsen | nose-hoover | v-rescale
    tc-grps                 = System
    tau-t                   = 1.0
    ref-t                   = 300
    nsttcouple              = 5
    nh-chain-length         = 10
    pcoupl                  = Parrinello-Rahman  ; no | Berendsen | Parrinello-Rahman
    pcoupltype              = anisotropic           ; isotropic | semiisotropic (x/y vs z) | anisotropic
    tau-p                   = 5.0
    compressibility         = 4.5e-5 4.5e-5 4.5e-5 4.5e-5 4.5e-5 4.5e-5
    ref-p                   = 1.0 1.0 1.0 0.0 0.0 0.0                ; [bar]
    nstpcouple              = 5
    refcoord-scaling        = no
    constraints             = all-bonds           ; all-bonds | h-bonds
    constraint-algorithm    = LINCS
    nstxout                 = 1000
    nstvout                 = 1000
    nstenergy               = 1000
    nstxout-compressed      = 0
    compressed-x-grps       = 
    nstlist                 = 5
    ns-type                 = grid
    cutoff-scheme           = Verlet
    verlet-buffer-tolerance = -1
    rlist                   = 1.4
    fourierspacing          = 0.12
    pme-order               = 6
    ewald-rtol              = 1e-8
    DispCorr                = EnerPres
    lincs-order             = 6
    lincs-iter              = 2
    continuation            = no
    define                  = 
    print-nose-hoover-chain-variables = yes

    nstcalcenergy           = 5
    nstlog                  = 1000
    ```
</details>