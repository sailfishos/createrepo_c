Summary:        Creates a common metadata repository
Name:           createrepo_c
Version:        1.2.0
Release:        1
License:        GPLv2+
URL:            https://github.com/sailfishos/createrepo_c
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-Revert-createrepo_c-modifyrepo_c-switch-default-comp.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  file-devel
BuildRequires:  glib2-devel >= 2.22.0
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel >= 4.8.0-28
BuildRequires:  sqlite-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
Requires:       %{name}-libs =  %{version}-%{release}
Requires:       rpm >= 4.8.0-28
Obsoletes:      python2-%{name} <= 0.10.0+git1

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package libs
Summary:    Library for repodata manipulation

%description libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package devel
Summary:    Library for repodata manipulation
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package doc
Summary:   Readme for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/createrepo_c

%build
export CFLAGS="$CFLAGS -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="$CXXFLAGS -D_FILE_OFFSET_BITS=64"
export CPPFLAGS="$CPPFLAGS -D_FILE_OFFSET_BITS=64"
%cmake -DENABLE_PYTHON=OFF -DWITH_LIBMODULEMD=OFF -DWITH_ZCHUNK=OFF
%cmake_build

%install
%cmake_install

# Copy readme to document directory
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version}/ README.md

%post -n %{name}-libs -p /sbin/ldconfig

%postun -n %{name}-libs -p /sbin/ldconfig

%files
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_mandir}/man8/createrepo_c.8*
%{_mandir}/man8/mergerepo_c.8*
%{_mandir}/man8/modifyrepo_c.8*
%{_mandir}/man8/sqliterepo_c.8*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%files doc
%{_docdir}/%{name}-%{version}
