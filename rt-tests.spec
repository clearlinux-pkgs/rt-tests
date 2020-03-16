#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rt-tests
Version  : 1.8
Release  : 9
URL      : https://mirrors.edge.kernel.org/pub/linux/utils/rt-tests/rt-tests-1.8.tar.xz
Source0  : https://mirrors.edge.kernel.org/pub/linux/utils/rt-tests/rt-tests-1.8.tar.xz
Summary  : Programs used to test Priority Inheritance Mutexes
Group    : Development/Tools
License  : GPL-2.0
Requires: rt-tests-bin = %{version}-%{release}
Requires: rt-tests-license = %{version}-%{release}
Requires: rt-tests-man = %{version}-%{release}
Requires: rt-tests-python = %{version}-%{release}
Requires: rt-tests-python3 = %{version}-%{release}
BuildRequires : numactl-dev
Patch1: 0001-prefix.diff

%description
The pi_tests package contains programs used to test the functionality of 
the priority inheritance attribute of POSIX mutexes on the Linux kernel

%package bin
Summary: bin components for the rt-tests package.
Group: Binaries
Requires: rt-tests-license = %{version}-%{release}

%description bin
bin components for the rt-tests package.


%package license
Summary: license components for the rt-tests package.
Group: Default

%description license
license components for the rt-tests package.


%package man
Summary: man components for the rt-tests package.
Group: Default

%description man
man components for the rt-tests package.


%package python
Summary: python components for the rt-tests package.
Group: Default
Requires: rt-tests-python3 = %{version}-%{release}

%description python
python components for the rt-tests package.


%package python3
Summary: python3 components for the rt-tests package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rt-tests package.


%prep
%setup -q -n rt-tests-1.8
cd %{_builddir}/rt-tests-1.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584378279
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1584378279
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rt-tests
cp %{_builddir}/rt-tests-1.8/COPYING %{buildroot}/usr/share/package-licenses/rt-tests/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/rt-tests-1.8/src/pi_tests/COPYING %{buildroot}/usr/share/package-licenses/rt-tests/17e3b0eea99abffe6ac71e65627413236e0b117a
%make_install
## install_append content
rm -rf %{buildroot}/usr/src
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cyclicdeadline
/usr/bin/cyclictest
/usr/bin/deadline_test
/usr/bin/determine_maximum_mpps.sh
/usr/bin/get_cpuinfo_mhz.sh
/usr/bin/get_cyclictest_snapshot
/usr/bin/hackbench
/usr/bin/hwlatdetect
/usr/bin/pi_stress
/usr/bin/pip_stress
/usr/bin/pmqtest
/usr/bin/ptsematest
/usr/bin/queuelat
/usr/bin/rt-migrate-test
/usr/bin/signaltest
/usr/bin/sigwaittest
/usr/bin/ssdd
/usr/bin/svsematest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rt-tests/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/rt-tests/17e3b0eea99abffe6ac71e65627413236e0b117a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/cyclicdeadline.8.gz
/usr/share/man/man8/cyclictest.8.gz
/usr/share/man/man8/deadline_test.8.gz
/usr/share/man/man8/hackbench.8.gz
/usr/share/man/man8/hwlatdetect.8.gz
/usr/share/man/man8/pi_stress.8.gz
/usr/share/man/man8/pip_stress.8.gz
/usr/share/man/man8/pmqtest.8.gz
/usr/share/man/man8/ptsematest.8.gz
/usr/share/man/man8/queuelat.8.gz
/usr/share/man/man8/rt-migrate-test.8.gz
/usr/share/man/man8/signaltest.8.gz
/usr/share/man/man8/sigwaittest.8.gz
/usr/share/man/man8/ssdd.8.gz
/usr/share/man/man8/svsematest.8.gz

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
