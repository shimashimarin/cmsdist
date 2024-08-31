### RPM external collier 1.2.8
# Source: http://www.hepforge.org/archive/collier/%{n}-%{realversion}.tar.gz
Source: https://cmsrep.cern.ch/cmssw/download/collier/%{realversion}/%{n}-%{realversion}.tar.gz
BuildRequires: gmake cmake

%define keep_archives true

%prep
%setup -q -n COLLIER-%{realversion}
sed -i 's;add_definitions(-Dcollierdd -DSING);add_definitions(-Dcollierdd -DSING -fPIC);g' ./CMakeLists.txt

%build
rm -rf build && mkdir build
cmake -S . -B build \
  -DCMAKE_INSTALL_PREFIX=%{i} \
  -DCMAKE_BUILD_TYPE=Release \
  -Dstatic=ON \
  -DCMAKE_Fortran_FLAGS=-fPIC
cmake --build build %{makeprocesses}

%install
cmake --install build
sed -i 's;^.*set(COLLIER_LIBRARY_DIR.*$;get_filename_component(COLLIER_LIBRARY_DIR "${CMAKE_CURRENT_LIST_DIR}/../../lib" ABSOLUTE);' %{i}/lib/cmake/collierConfig.cmake
sed -i 's;^.*set(COLLIER_INCLUDE_DIR.*$;get_filename_component(COLLIER_INCLUDE_DIR "${CMAKE_CURRENT_LIST_DIR}/../../include" ABSOLUTE);' %{i}/lib/cmake/collierConfig.cmake
