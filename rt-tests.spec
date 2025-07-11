#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v27
# autospec commit: 65cf152
#
Name     : rt-tests
Version  : 2.9
Release  : 37
URL      : https://mirrors.kernel.org/pub/linux/utils/rt-tests/rt-tests-2.9.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/utils/rt-tests/rt-tests-2.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: rt-tests-bin = %{version}-%{release}
Requires: rt-tests-license = %{version}-%{release}
Requires: rt-tests-man = %{version}-%{release}
Requires: rt-tests-python = %{version}-%{release}
Requires: rt-tests-python3 = %{version}-%{release}
BuildRequires : numactl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-prefix.diff

%description
cyclictest does not catch all cases where packet forwarding
latency can exceed a given threshold.

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
%setup -q -n rt-tests-2.9
cd %{_builddir}/rt-tests-2.9
%patch -P 1 -p1
pushd ..
cp -a rt-tests-2.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1751414702
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1751414702
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rt-tests
cp %{_builddir}/rt-tests-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rt-tests/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/rt-tests-%{version}/src/pi_tests/COPYING %{buildroot}/usr/share/package-licenses/rt-tests/17e3b0eea99abffe6ac71e65627413236e0b117a || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## install_append content
rm -rf %{buildroot}/usr/src
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cyclicdeadline
/V3/usr/bin/cyclictest
/V3/usr/bin/deadline_test
/V3/usr/bin/hackbench
/V3/usr/bin/oslat
/V3/usr/bin/pi_stress
/V3/usr/bin/pip_stress
/V3/usr/bin/pmqtest
/V3/usr/bin/ptsematest
/V3/usr/bin/queuelat
/V3/usr/bin/rt-migrate-test
/V3/usr/bin/signaltest
/V3/usr/bin/sigwaittest
/V3/usr/bin/ssdd
/V3/usr/bin/svsematest
/usr/bin/cyclicdeadline
/usr/bin/cyclictest
/usr/bin/deadline_test
/usr/bin/determine_maximum_mpps.sh
/usr/bin/get_cyclictest_snapshot
/usr/bin/hackbench
/usr/bin/hwlatdetect
/usr/bin/oslat
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
/usr/share/man/man8/cyclicdeadline.8
/usr/share/man/man8/cyclictest.8
/usr/share/man/man8/deadline_test.8
/usr/share/man/man8/determine_maximum_mpps.8
/usr/share/man/man8/get_cyclictest_snapshot.8
/usr/share/man/man8/hackbench.8
/usr/share/man/man8/hwlatdetect.8
/usr/share/man/man8/oslat.8
/usr/share/man/man8/pi_stress.8
/usr/share/man/man8/pip_stress.8
/usr/share/man/man8/pmqtest.8
/usr/share/man/man8/ptsematest.8
/usr/share/man/man8/queuelat.8
/usr/share/man/man8/rt-migrate-test.8
/usr/share/man/man8/signaltest.8
/usr/share/man/man8/sigwaittest.8
/usr/share/man/man8/ssdd.8
/usr/share/man/man8/svsematest.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
