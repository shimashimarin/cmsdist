### RPM external libzip 1.10.1
Source: https://github.com/nih-at/libzip/releases/download/v%{realversion}/libzip-%{realversion}.tar.gz
Requires: zlib zstd
BuildRequires: cmake

%prep
%setup -n %{n}-%{realversion}

%build
rm -rf build && mkdir build
cmake -S . -B build \
  -DCMAKE_INSTALL_PREFIX=%{i}
cmake --build build %{makeprocesses}

%install
cmake --install build
