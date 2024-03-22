### RPM external tensorflow-xla-runtime 2.12.0
## INCLUDE cpp-standard
## INCLUDE compilation_flags

Source99: scram-tools.file/tools/eigen/env

Requires: eigen py3-tensorflow abseil-cpp
BuildRequires: cmake

%prep

cp -r ${PY3_TENSORFLOW_ROOT}/lib/python%{cms_python3_major_minor_version}/site-packages/tensorflow .

%build

source %{_sourcedir}/env
export CPATH="${CPATH}:${EIGEN_ROOT}/include/eigen3"

CXXFLAGS="-fPIC %{arch_build_flags} ${CMS_EIGEN_CXX_FLAGS}"
%ifarch x86_64
    CXXFLAGS="${CXXFLAGS} -msse3"
%endif

pushd tensorflow/xla_aot_runtime_src
  # the CMakelists.txt file is not intended to produce a shared library so create a static one first
  cmake . -DCMAKE_CXX_FLAGS="${CXXFLAGS}" -DCMAKE_CXX_STANDARD=%{cms_cxx_standard} -DBUILD_SHARED_LIBS=OFF
  make %{makeprocesses}

  # build the shared library, linking missing symbols from abseil
  gcc -shared -o libtf_xla_runtime.so -Wl,--whole-archive libtf_xla_runtime.a -Wl,--no-whole-archive \
    -L${ABSEIL_CPP_ROOT}/lib -labsl_strings -labsl_str_format_internal
popd

%install

mkdir -p %{i}/lib/archive
mv tensorflow/xla_aot_runtime_src/libtf_xla_runtime.a %{i}/lib/archive/libtf_xla_runtime-static.a
mv tensorflow/xla_aot_runtime_src/libtf_xla_runtime.so %{i}/lib/
