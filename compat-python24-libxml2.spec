%define compat_python %{_bindir}/python2.4

%{!?python_sitearch: %define python_sitearch %(%{compat_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_sitelib: %define python_sitelib %(%{compat_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Python2.4 bindings for the libxml2 library
Name: compat-python24-libxml2
Version: 2.7.3
Release: 3%{?dist}
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: compat-python24-devel libxml2-devel
Requires: libxml2 = %{version}, python(abi) = 2.4
URL: http://xmlsoft.org/
Patch0: multilib.patch

Provides: libxml2-python24 = %{version}-%{release}
Obsoletes: libxml2-python24 < 2.7.1-2

%description
The libxml2-python24 package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%setup -q -n libxml2-%{version}
%patch0 -p1

%build
pushd python
CFLAGS="$RPM_OPT_FLAGS" %{compat_python} setup.py build
popd
gzip -9 ChangeLog

%install
rm -rf $RPM_BUILD_ROOT

pushd python
CFLAGS="$RPM_OPT_FLAGS" %{compat_python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README Copyright
%{python_sitearch}/libxml2.py*
%{python_sitearch}/drv_libxml2.py*
%{python_sitearch}/libxml2mod*
%doc python/TODO
%doc python/tests/*.py
%doc doc/*.py
%doc doc/python.html

%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.7.3-3
- rebuild for new F11 features

* Mon Feb 02 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.7.3-1
- update to 2.7.3

* Wed Oct 15 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.7.2-2
- update to 2.7.2

* Fri Oct 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.7.1-2
- update to 2.7.1 on request from Jonathan

* Sat Aug 09 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.6.32-2
- rebuild for RPM Fusion
- add provides and obsoletes for libxml2-python24 from livna

* Sun Apr 27 2008 Jonathan Steffan <jon a fedoraunity.org> 2.6.32-1
- Update to 2.6.32

* Wed Jan 16 2008 Jonathan Steffan <jon a fedoraunity.org> 2.6.31-1
- Update to 2.6.31

* Tue Jan 15 2008 Jonathan Steffan <jon a fedoraunity.org> 2.6.30-2
- Bump release for rebuild
- Update upstream URL

* Sat Dec 1 2007 Jonathan Steffan <jon a fedoraunity.org> 2.6.30-1
- Update for f8's 2.6.30 libxml2

* Mon Sep 3 2007 Jonathan Steffan <jon a fedoraunity.org> 2.6.29-1
- Only package the python bindings built for python 2.4
