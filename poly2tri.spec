Name:           poly2tri
Version:        0.0
Release:        20
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD
URL:            https://github.com/greenm01/poly2tri
Source0:        https://github.com/greenm01/poly2tri/archive/88de49021b6d9bef6faa1bc94ceb3fbd85c3c204/poly2tri.tar.gz
Source1:        Makefile
BuildRequires:  gcc-c++ mesa-libGL-devel

%description
This package provides a library for constrained Delaunay triangulation.

%package        devel
Summary:        Development files for poly2tri
Requires:       poly2tri = %{version}-%{release}

%description    devel
This package contains development files for poly2tri.

%prep
%autosetup -n   %{name}-88de49021b6d9bef6faa1bc94ceb3fbd85c3c204 -p1
cp %{SOURCE1} poly2tri/Makefile

%build
cd poly2tri
%make_build CXX=%toolchain CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
install -Dp -m 0755 poly2tri/libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so.1.0
ln -s libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so.1
ln -s libpoly2tri.so.1.0 %{buildroot}%{_libdir}/libpoly2tri.so
mkdir -p %{buildroot}%{_includedir}/poly2tri/common
mkdir -p %{buildroot}%{_includedir}/poly2tri/sweep
cp -p poly2tri/common/*.h  %{buildroot}%{_includedir}/poly2tri/common
cp -p poly2tri/sweep/*.h   %{buildroot}%{_includedir}/poly2tri/sweep
cp -p poly2tri/*.h  %{buildroot}%{_includedir}/poly2tri

%files
%doc AUTHORS LICENSE README
%{_libdir}/libpoly2tri.so.*

%files devel
%{_libdir}/libpoly2tri.so
%{_includedir}/poly2tri

%changelog
* Thu May 25 2023 Xiaoya Huang <huangxiaoya@iscas.ac.cn> - 0.0-20
- Make CXX compiler depend on toolchain

* Wed Feb 19 2020 Jiangping Hu <hujp1985@foxmail.com> - 0.0-19
- Package init
