Summary:	E_dbus bindings for Python
Name:		python-e_dbus
Version:	1.7.0
Release:	2
License:	GPLv2
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	python-cython
%py_requires -d

%description
Python support files for E_dbus.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	pkgconfig(dbus-python)

%description devel
Development files for the Python wrapper for the E_dbus libraries.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{py_platsitedir}/e_dbus.*

%files devel
%{_libdir}/pkgconfig/*.pc



%changelog
* Fri Jun 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.3-0.71914.1
+ Revision: 807489
- revision update 71914

* Tue Jan 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.3-0.65723.1
+ Revision: 759581
- fixed BR
- imported package python-e_dbus

