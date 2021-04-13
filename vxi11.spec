Summary: VXI11 Device Communication
Name: vxi11
Version: 2.0ud.1
Release: 1
URL: https://github.com/drepper/vxi11.git
Source: vxi11-2.0ud.1.tar.gz
License: GPLv2+

BuildRequires: gcc
BuildRequires: make
BuildRequires: libtirpc-devel
BuildRequires: rpcgen
BuildRequires: pkgconf-pkg-config
BuildRequires: sed

%define abi 1

%description
This library allows communication using the VXI11 RPC protocol with
Ethernet-enabled devices such as oscilloscopes, logic analyzers, 
function generators, power supplies, etc.  The specific commands vary
by device.

%package utils
Summary: Utilities to use VXI11 library to control devices
License: GPLv2+
Requires: vxi11 = %{version}-%{release}

%description utils
This package contains the utilities which use the VXI11 library to
control devices.  The vxi11_cmd utility provides a simple interactive
shell to send commands and queries to one device at a time.  The
vxi11_send utility allows to send a single command to a device.

%package devel
Summary: Files needed for using the VXI11 library
License: GPLv2+
Requires: vxi11 = %{version}-%{release}

%description devel
The vxi11-devel package contains the files needed to write code that
uses the libvxi11 library.

%package -n python3-vxi11
Summary: Python interface to VXI11 library
License: GPLv2+
Requires: vxi11 = %{version}-%{release}

%description -n python3-vxi11
This package contains a Python binding of the libvxi11 library to
control Ethernet-enabled devices.

%prep
%setup -q

%build
make OPTS="${RPM_OPT_FLAGS} -Wno-unused-variable" CC=gcc

cd python
%py3_build
cd ..

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}

%make_install prefix=%{_prefix} lib=%{_lib}

cd python
%py3_install
cd ..

%clean
rm -fr ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license GNU_General_Public_License.txt
%doc README.md CHANGELOG.txt
%{_libdir}/libvxi11.so.%{abi}

%files utils
%defattr(-,root,root)
%{_bindir}/vxi11_cmd
%{_bindir}/vxi11_send

%files devel
%defattr(-,root,root)
%{_libdir}/libvxi11.so
%{_includedir}/vxi11_user.h

%files -n python3-vxi11
%defattr(-,root,root)
%{python3_sitelib}/vxi11.py
%{python3_sitelib}/vxi11-*.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
* Tue Apr 13 2021 Ulrich Drepper <drepper@gmail.com> 2.0ud.1-1
- Build based on cloned git repository which contains the patches
* Mon Apr 12 2021 Ulrich Drepper <drepper@gmail.com> 2.0-1
- Create Fedora .spec file for the unchanged git repository
- fix a few bugs including potential buffer overruns
- add patch to distribute python code
