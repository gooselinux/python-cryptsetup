%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-cryptsetup
Version:        0.0.11
Release:        1%{?dist}
Summary:        Python bindings for cryptsetup

Group:          Development/Libraries
License:        GPLv2+
Url:            http://git.fedorahosted.org/git/?p=python-cryptsetup.git;a=snapshot;h=%{name}-%{version};sf=tgz

# To generate source do
# git clone git://git.fedorahosted.org/python-cryptsetup.git
# make archive

Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cryptsetup-luks-devel
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

%description
A python module to ease the manipulation with LUKS devices.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# For noarch packages: sitelib
%{python_sitearch}/pycryptsetup
%{python_sitearch}/cryptsetup.so
%{python_sitearch}/*egg-info

%doc COPYING
%doc selftest.py

%changelog
* Fri Aug 13 2010 Martin Sivak <msivak at redhat dot com> - 0.0.11-1
- Different payload alignment
  Resolves: rhbz#623703

* Tue Dec 08 2009 Martin Sivak <msivak at redhat dot com> - 0.0.10-2
- add python-devel into build requires
- change the Url so it uses git repo

* Wed Aug 26 2009 Martin Sivak <msivak at redhat dot com> - 0.0.10-1
- fix the crash in dealloc routine

* Thu Aug 13 2009 Martin Sivak <msivak at redhat dot com> - 0.0.9-3
- spec file change, point to proper project url

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Martin Sivak <msivak at redhat dot com> - 0.0.9-1
- luksFormat accepts None values and then uses defaults

* Fri Mar 06 2009 Martin Sivak <msivak at redhat dot com> - 0.0.8-1
- Fix the params for add and remove key routines
- Workaround one SIGSEGV in cryptsetup and change the order of passwords in luksRemoveKey

* Thu Mar 05 2009 Martin Sivak <msivak at redhat dot com> - 0.0.7-1
- add default cipher mode and key to luksFormat

* Mon Mar 02 2009 Martin Sivak <msivak at redhat dot com> - 0.0.6-1
- fix the UUID extraction logic
- fix the key manipulation

* Mon Mar 02 2009 Martin Sivak <msivak at redhat dot com> - 0.0.5-1
- fix the luksUUID

* Mon Mar 02 2009 Martin Sivak <msivak at redhat dot com> - 0.0.4-1
- add prepare_passphrase_file method

* Mon Mar 02 2009 Martin Sivak <msivak at redhat dot com> - 0.0.3-1
- Improve documentation
- luksFormat now accepts keyfile argument

* Mon Feb 23 2009 Martin Sivak <msivak at redhat dot com> - 0.0.2-1
- Throw a runtime exception when buildvalue problem is encountered

* Thu Jan 22 2009 Martin Sivak <msivak at redhat dot com> - 0.0.1-1
- Inital release

