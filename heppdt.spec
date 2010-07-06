### RPM external heppdt 3.03.00
Source: http://lcgapp.cern.ch/project/simu/HepPDT/download/HepPDT-%{realversion}.tar.gz
Patch1: heppdt-2.03.00-nobanner
Patch2: heppdt-3.03.00-silence-debug-output 

%prep
%setup -q -n HepPDT-%{realversion}
%patch1 -p1
%patch2 -p1
./configure  --prefix=%{i} 

%build
make 

%install
make install
# SCRAM ToolBox toolfile
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/%n.xml
  <tool name="%n" version="%v">
    <lib name="HepPDT"/>
    <lib name="HepPID"/>
    <client>
      <environment name="HEPPDT_BASE" default="%i"/>
      <environment name="LIBDIR" default="$HEPPDT_BASE/lib"/>
      <environment name="INCLUDE" default="$HEPPDT_BASE/include"/>
    </client>
    <runtime name="HEPPDT_PARAM_PATH" value="$HEPPDT_BASE"/>
  </tool>
EOF_TOOLFILE

%post
%{relocateConfig}etc/scram.d/%n.xml
