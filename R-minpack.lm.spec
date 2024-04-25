#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-minpack.lm
Version  : 1.2.4
Release  : 53
URL      : https://cran.r-project.org/src/contrib/minpack.lm_1.2-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/minpack.lm_1.2-4.tar.gz
Summary  : R Interface to the Levenberg-Marquardt Nonlinear Least-Squares
Group    : Development/Tools
License  : BSD-3-Clause-Attribution GPL-3.0
Requires: R-minpack.lm-lib = %{version}-%{release}
Requires: R-minpack.lm-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-minpack.lm package.
Group: Libraries
Requires: R-minpack.lm-license = %{version}-%{release}

%description lib
lib components for the R-minpack.lm package.


%package license
Summary: license components for the R-minpack.lm package.
Group: Default

%description license
license components for the R-minpack.lm package.


%prep
%setup -q -n minpack.lm
pushd ..
cp -a minpack.lm buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694449862

%install
export SOURCE_DATE_EPOCH=1694449862
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-minpack.lm
cp %{_builddir}/minpack.lm/LICENSE.note %{buildroot}/usr/share/package-licenses/R-minpack.lm/df73e10dcfd2d05667e6fe85cabe5dfe3c984727 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/minpack.lm/COPYRIGHTS
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so.avx2
/usr/lib64/R/library/minpack.lm/libs/minpack.lm.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-minpack.lm/df73e10dcfd2d05667e6fe85cabe5dfe3c984727
