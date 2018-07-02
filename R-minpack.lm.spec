#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-minpack.lm
Version  : 1.2.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/minpack.lm_1.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/minpack.lm_1.2-1.tar.gz
Summary  : R Interface to the Levenberg-Marquardt Nonlinear Least-Squares
Group    : Development/Tools
License  : BSD-3-Clause-Attribution GPL-3.0
Requires: R-minpack.lm-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-minpack.lm package.
Group: Libraries

%description lib
lib components for the R-minpack.lm package.


%prep
%setup -q -c -n minpack.lm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523318826

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523318826
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library minpack.lm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library minpack.lm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library minpack.lm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library minpack.lm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/minpack.lm/DESCRIPTION
/usr/lib64/R/library/minpack.lm/INDEX
/usr/lib64/R/library/minpack.lm/Meta/Rd.rds
/usr/lib64/R/library/minpack.lm/Meta/features.rds
/usr/lib64/R/library/minpack.lm/Meta/hsearch.rds
/usr/lib64/R/library/minpack.lm/Meta/links.rds
/usr/lib64/R/library/minpack.lm/Meta/nsInfo.rds
/usr/lib64/R/library/minpack.lm/Meta/package.rds
/usr/lib64/R/library/minpack.lm/NAMESPACE
/usr/lib64/R/library/minpack.lm/NEWS
/usr/lib64/R/library/minpack.lm/R/minpack.lm
/usr/lib64/R/library/minpack.lm/R/minpack.lm.rdb
/usr/lib64/R/library/minpack.lm/R/minpack.lm.rdx
/usr/lib64/R/library/minpack.lm/help/AnIndex
/usr/lib64/R/library/minpack.lm/help/aliases.rds
/usr/lib64/R/library/minpack.lm/help/minpack.lm.rdb
/usr/lib64/R/library/minpack.lm/help/minpack.lm.rdx
/usr/lib64/R/library/minpack.lm/help/paths.rds
/usr/lib64/R/library/minpack.lm/html/00Index.html
/usr/lib64/R/library/minpack.lm/html/R.css
/usr/lib64/R/library/minpack.lm/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so.avx2
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so.avx512
