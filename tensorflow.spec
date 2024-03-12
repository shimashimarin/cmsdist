### RPM external tensorflow 2.12.0
%if "%{?vectorized_package:set}" != "set"
%define source_package tensorflow-sources
%else
%define source_package tensorflow-sources_%{vectorized_package}
%endif
## INCLUDE tensorflow-requires
BuildRequires: %{source_package}
%define tf_root %(echo %{source_package}_ROOT | tr '[a-z-]' '[A-Z_]')
%define tf_version %(echo %{source_package}_VERSION | tr '[a-z-]' '[A-Z_]')
Provides: libtensorflow_cc.so(tensorflow)(64bit)
Source: none

%prep
case ${%{tf_version}} in
  %{realversion}|%{realversion}-*) ;;
  * ) echo "ERROR: Mismatch %{n} (%{realversion}) and %{source_package} (${%{tf_version}}) versions."
      echo "Please update %{n}.spec to use ${%{tf_version}} verison."
      exit 1
      ;;
esac

%build

%install

tar xfz ${%{tf_root}}/libtensorflow_cc.tar.gz -C %{i}
%if %{enable_gpu}
mkdir -p %{i}/etc/scram.d
cat << \EOF_TOOLFILE >%{i}/etc/scram.d/tf_cuda_support.xml
  <tool name="tf_cuda_support" version="1.0">
  <tool>
EOF_TOOLFILE
%endif

%post
%{relocateConfig}lib/lib*.params
