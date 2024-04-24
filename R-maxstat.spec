#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-maxstat
Version  : 0.7.25
Release  : 2
URL      : https://cran.r-project.org/src/contrib/maxstat_0.7-25.tar.gz
Source0  : https://cran.r-project.org/src/contrib/maxstat_0.7-25.tar.gz
Summary  : Maximally Selected Rank Statistics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-maxstat-lib = %{version}-%{release}
Requires: R-exactRankTests
Requires: R-mvtnorm
BuildRequires : R-exactRankTests
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
several p-value approximations.

%package lib
Summary: lib components for the R-maxstat package.
Group: Libraries

%description lib
lib components for the R-maxstat package.


%prep
%setup -q -n maxstat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713980613

%install
export SOURCE_DATE_EPOCH=1713980613
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/maxstat/DESCRIPTION
/usr/lib64/R/library/maxstat/INDEX
/usr/lib64/R/library/maxstat/Meta/Rd.rds
/usr/lib64/R/library/maxstat/Meta/data.rds
/usr/lib64/R/library/maxstat/Meta/features.rds
/usr/lib64/R/library/maxstat/Meta/hsearch.rds
/usr/lib64/R/library/maxstat/Meta/links.rds
/usr/lib64/R/library/maxstat/Meta/nsInfo.rds
/usr/lib64/R/library/maxstat/Meta/package.rds
/usr/lib64/R/library/maxstat/Meta/vignette.rds
/usr/lib64/R/library/maxstat/NAMESPACE
/usr/lib64/R/library/maxstat/NEWS
/usr/lib64/R/library/maxstat/R/maxstat
/usr/lib64/R/library/maxstat/R/maxstat.rdb
/usr/lib64/R/library/maxstat/R/maxstat.rdx
/usr/lib64/R/library/maxstat/data/Rdata.rdb
/usr/lib64/R/library/maxstat/data/Rdata.rds
/usr/lib64/R/library/maxstat/data/Rdata.rdx
/usr/lib64/R/library/maxstat/doc/index.html
/usr/lib64/R/library/maxstat/doc/maxstat.R
/usr/lib64/R/library/maxstat/doc/maxstat.Rnw
/usr/lib64/R/library/maxstat/doc/maxstat.pdf
/usr/lib64/R/library/maxstat/help/AnIndex
/usr/lib64/R/library/maxstat/help/aliases.rds
/usr/lib64/R/library/maxstat/help/maxstat.rdb
/usr/lib64/R/library/maxstat/help/maxstat.rdx
/usr/lib64/R/library/maxstat/help/paths.rds
/usr/lib64/R/library/maxstat/html/00Index.html
/usr/lib64/R/library/maxstat/html/R.css
/usr/lib64/R/library/maxstat/results/LausenTab2.rda
/usr/lib64/R/library/maxstat/tests/Examples/maxstat-Ex.Rout.save
/usr/lib64/R/library/maxstat/tests/maxstat-bugs.R
/usr/lib64/R/library/maxstat/tests/maxstat-bugs.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/maxstat/libs/maxstat.so
