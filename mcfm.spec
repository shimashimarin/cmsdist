### RPM external mcfm 10.3

Source: https://mcfm.fnal.gov/downloads/MCFM-%{realversion}.tar.gz
Requires: lhapdf openmpi
BuildRequires: gmake cmake
Patch0: mcfm-10.3-add-install-path-option

%define keep_archives true

%prep
%setup -q -n MCFM-%{realversion}
%patch0 -p1

%build
rm -rf build && mkdir build
export OMP_STACKSIZE=16000
cmake -S . -B build \
  -DCMAKE_INSTALL_PREFIX=%{i} \
  -Dwith_vvamp=ON \
  -Dwith_library=ON \
  -Duse_internal_lhapdf=OFF \
  -DCMAKE_PREFIX_PATH=$LHAPDF_ROOT \
  -Dlhapdf_include_path=$LHAPDF_ROOT/include \
  -Duse_mpi=ON \
  -DCMAKE_C_COMPILER=mpicc \
  -DCMAKE_CXX_COMPILER=mpic++ \
  -DCMAKE_Fortran_COMPILER=mpifort

cmake --build build %{makeprocesses}

%install
cmake --install build