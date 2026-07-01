# Installation
## TSUBAME
1. Choose your own install directory and set `INSTALL_PREFIX` accordingly.  
   For example, if you want to install GROMACS under `/hoge/fuga`, run:
   ```bash
   INSTALL_PREFIX=/hoge/fuga
   ```
   Replace `/hoge/fuga` with any directory where you have write permission
   (e.g. your home directory or a project-specific path).


2. Build GROMACS with the following commands:
    ```bash
    module purge
    module load  cmake/3.28.3 intel/2024.0.2  intel-mpi/2021.11

    wget ftp://ftp.gromacs.org/gromacs/gromacs-2024.1.tar.gz
    tar xvf gromacs-2024.1.tar.gz

    cd gromacs-2024.1
    
    mkdir build
    cd build
    
    cmake .. \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX} \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_C_COMPILER=mpicc \
    -DCMAKE_CXX_COMPILER=mpicxx \
    -DGMX_MPI=ON \
    -DGMX_GPU=OFF \
    -DGMX_DOUBLE=OFF \
    -DGMX_THREAD_MPI=OFF \
    -DBUILD_SHARED_LIBS=OFF \
    -DGMXAPI=OFF \
    -DGMX_INSTALL_NBLIB_API=OFF \
    -DGMX_BUILD_OWN_FFTW=ON \
    -DGMX_EXTERNAL_BLAS=ON \
    -DGMX_EXTERNAL_LAPACK=ON \
    -DREGRESSIONTEST_DOWNLOAD=ON

    # cmake .. \
    # -DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX} \
    # -DCMAKE_VERBOSE_MAKEFILE=ON \
    # -DCMAKE_C_COMPILER=mpiicx \
    # -DCMAKE_CXX_COMPILER=mpiicpx \
    # -DGMX_MPI=ON \
    # -DGMX_GPU=OFF \
    # -DGMX_DOUBLE=OFF \
    # -DGMX_THREAD_MPI=OFF \
    # -DBUILD_SHARED_LIBS=OFF \
    # -DGMXAPI=OFF \
    # -DGMX_INSTALL_NBLIB_API=OFF \
    # -DGMX_BUILD_OWN_FFTW=ON \
    # -DGMX_EXTERNAL_BLAS=ON \
    # -DGMX_EXTERNAL_LAPACK=ON \
    # -DREGRESSIONTEST_DOWNLOAD=ON
    
    make -j64
    make check
    make install
    ```
3. Set the PATH  
    Add the following line to your `.bashrc`:
   ```bash
   source ${INSTALL_PREFIX}/bin/GMXRC.bash
   ```
   Here `INSTALL_PREFIX` is the directory you chose in step 1.  
   For the example above, this becomes:
   ```bash
   source /hoge/fuga/bin/GMXRC.bash
   ```