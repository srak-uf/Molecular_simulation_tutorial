# Run MD
- Type of gmx command
    - `gmx`: Serial version, Mixed Precision, OpenMP
    - `gmx_d`: Serial version, Double Precision, OpenMP
    - `gmx_mpi`: MPI version, Mixed Precision, MPI Parallelization + OpenMP
    - `gmx_mpi_d`: MPI version, Double Precision, MPI Parallelization + OpenMP

## Procedure
1. Run MD
    ```bash
    gmx grompp -c conf.gro -p topology.top -f md.mdp -o hoge.tpr

    ### Thread mpi for laptop, tMPI Process = 2 and OpenMP thread = 2
    # gmx mdrun -deffnm hoge -ntmpi 2 -ntomp 2 -v
    
    ### MPI Parallelization, MPI Process = 32 and OpenMP thread = 2
    # mpirun -np 32 gmx_mpi mdrun -deffnm hoge -ntomp 2 -v
    ```
2. Restart MD
    ```bash
    gmx mdrun -deffnm hoge -cpi hoge.cpt -ntmpi 2 -ntomp 2 -noappend -v
    ```

    ```{tip}
    Energy file of `.edr` can be merged by `gmx eneconv` command.  
    `gmx eneconv -f order1.edr order2.edr ... -o merge.edr`

    Trajectory file of `.trr` can be merged by `gmx trjcat` command.  
    `gmx trjcat -f order1.trr order2.trr ... -overwrite -o merge.trr`
    ```

## TSUBAME
under construction

