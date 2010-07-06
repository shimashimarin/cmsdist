### RPM external thepeg 1.6.1
## BUILDIF case $(uname):$(uname -m) in Linux:i*86 ) true ;; Linux:x86_64 ) true ;;  Linux:ppc64 ) false ;; Darwin:* ) false ;; * ) false ;; esac

#Source: http://www.thep.lu.se/~leif/ThePEG/ThePEG-%{realversion}.tgz
#Source: http://projects.hepforge.org/herwig/files/ThePEG-%{realversion}.tar.gz
Source: http://service-spi.web.cern.ch/service-spi/external/MCGenerators/distribution/thepeg-%{realversion}-src.tgz
Patch0: thepeg-1.6.1-break-termcap-dependence
Patch1: thepeg-1.6.1-units
Requires: lhapdf
Requires: gsl

%prep
%setup -q -n %{n}/%{realversion}
%patch0 -p2
%patch1 -p2

%build
./configure --with-LHAPDF=$LHAPDF_ROOT/lib --without-javagui --prefix=%i --with-gsl=$GSL_ROOT
make

%install

make install
rm %i/share/ThePEG/Doc/fixinterfaces.pl

# SCRAM ToolBox toolfile
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/%n.xml
  <tool name="%n" version="%v">
    <lib name="ThePEG"/>
    <client>
      <environment name="THEPEG_BASE" default="%i"/>
      <environment name="LIBDIR" default="$THEPEG_BASE/lib/ThePEG"/>
      <environment name="INCLUDE" default="$THEPEG_BASE/include"/>
    </client>
    <use name="lhapdf"/>
    <use name="gsl"/>
  </tool>
EOF_TOOLFILE

%post
%{relocateConfig}etc/scram.d/%n.xml
%{relocateConfig}lib/ThePEG/ACDCSampler.la
%{relocateConfig}lib/ThePEG/BreitWignerMass.la
%{relocateConfig}lib/ThePEG/ColourPairDecayer.la
%{relocateConfig}lib/ThePEG/DalitzDecayer.la
%{relocateConfig}lib/ThePEG/FixedCMSLuminosity.la
%{relocateConfig}lib/ThePEG/GaussianPtGenerator.la
%{relocateConfig}lib/ThePEG/GRV94L.la
%{relocateConfig}lib/ThePEG/GRV94M.la
%{relocateConfig}lib/ThePEG/GRVBase.la
%{relocateConfig}lib/ThePEG/KTClus.la
%{relocateConfig}lib/ThePEG/LeptonLeptonPDF.la
%{relocateConfig}lib/ThePEG/LeptonLeptonRemnant.la
%{relocateConfig}lib/ThePEG/LesHouches.la
%{relocateConfig}lib/ThePEG/libThePEG.la
%{relocateConfig}lib/ThePEG/LWHFactory.la
%{relocateConfig}lib/ThePEG/MadGraphReader.la
%{relocateConfig}lib/ThePEG/MEee2gZ2qq.la
%{relocateConfig}lib/ThePEG/MENCDIS.la
%{relocateConfig}lib/ThePEG/MEQCD.la
%{relocateConfig}lib/ThePEG/MultiEventGenerator.la
%{relocateConfig}lib/ThePEG/O1AlphaS.la
%{relocateConfig}lib/ThePEG/OmegaPhi3PiDecayer.la
%{relocateConfig}lib/ThePEG/Onium3GDecayer.la
%{relocateConfig}lib/ThePEG/QuarksToHadronsDecayer.la
%{relocateConfig}lib/ThePEG/ReweightConstant.la
%{relocateConfig}lib/ThePEG/ReweightMinPT.la
%{relocateConfig}lib/ThePEG/SimpleAlphaEM.la
%{relocateConfig}lib/ThePEG/SimpleDISCut.la
%{relocateConfig}lib/ThePEG/SimpleFlavour.la
%{relocateConfig}lib/ThePEG/SimpleKTCut.la
%{relocateConfig}lib/ThePEG/SimpleZGenerator.la
%{relocateConfig}lib/ThePEG/StandardCKM.la
%{relocateConfig}lib/ThePEG/Tau2HadronsDecayer.la
%{relocateConfig}lib/ThePEG/TestLHAPDF.la
%{relocateConfig}lib/ThePEG/ThePEGStrategy.la
%{relocateConfig}lib/ThePEG/V2LeptonsCut.la
%{relocateConfig}lib/ThePEG/V2PPDecayer.la
%{relocateConfig}lib/ThePEG/WeakToHadronsDecayer.la
%{relocateConfig}lib/ThePEG/XSecCheck.la

