### RPM external libpng 1.6.37
%define tag a40189cf881e9f0db80511c382292a5604c3c3d1
%define branch cms/v%{realversion}
%define github_user cms-externals
Source: git+https://github.com/%github_user/%{n}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz

BuildRequires: autotools
Requires: zlib

%prep
%setup -n %{n}-%{realversion}

%build
autoreconf -fiv

./configure \
  --prefix=%{i} \
  --disable-silent-rules \
  CPPFLAGS="-I${ZLIB_ROOT}/include" \
  LDFLAGS="-L${ZLIB_ROOT}/lib"

make %{makeprocesses}

%install
make install

# Strip libraries, we are not going to debug them.
%define strip_files %i/lib
%define drop_files %{i}/share

%post
%{relocateConfig}bin/libpng-config
%{relocateConfig}bin/libpng16-config
