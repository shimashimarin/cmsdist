### RPM external hepmc3 3.2.7
## INCLUDE cpp-standard
Source: https://gitlab.cern.ch/hepmc/HepMC3/-/archive/%{realversion}/HepMC3-%{realversion}.tar.gz
Requires: root
BuildRequires: cmake

%prep
%setup -q -n HepMC3-%{realversion}

%build
rm -rf build && mkdir build
cmake -S . -B build \
  -DHEPMC3_ENABLE_ROOTIO:BOOL=ON -DROOT_DIR=$ROOT_ROOT \
  -DHEPMC3_ENABLE_TEST:BOOL=OFF -DHEPMC3_INSTALL_INTERFACES:BOOL=ON -DHEPMC3_ENABLE_PYTHON:BOOL=OFF \
  -DHEPMC3_BUILD_STATIC_LIBS:BOOL=OFF -DHEPMC3_BUILD_DOCS:BOOL=OFF \
  -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} -DHEPMC3_CXX_STANDARD=%{cms_cxx_standard} \
  -DCMAKE_INSTALL_PREFIX:PATH="%i"

cmake --build build %{makeprocesses}

%install
cmake --install build

