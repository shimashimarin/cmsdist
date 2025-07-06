### RPM external recola2_model_sm 2.2.3
Source: https://recola.hepforge.org/downloads/SM_%{realversion}.tar.gz
Requires: collier
BuildRequires: cmake

%define keep_archives true

%prep
%setup -q -n SM_%{realversion}

%build
rm -rf build && mkdir build
cmake -S . -B build \
  -DCMAKE_INSTALL_PREFIX=%{i} \
  -DCMAKE_BUILD_TYPE=Release \
  -Dstatic=ON \
  -Dcollier_path=${COLLIER_ROOT}
cmake --build build %{makeprocesses}


%install
cmake --install build
mv %{i}/lib/cmake %{i}/cmake
sed -i 's;^.*set(MODELFILE_LIBRARY_DIR.*$;get_filename_component(MODELFILE_LIBRARY_DIR "${CMAKE_CURRENT_LIST_DIR}/../lib" ABSOLUTE);' %{i}/cmake/modelfileConfig.cmake
sed -i 's;^.*set(MODELFILE_INCLUDE_DIR.*$;get_filename_component(MODELFILE_INCLUDE_DIR "${CMAKE_CURRENT_LIST_DIR}/../include" ABSOLUTE);' %{i}/cmake/modelfileConfig.cmake


