Name:             python-pymod2pkg
Version:          0.2.1
Release:          1%{?dist}
Summary:          python module name to package name map

Group:            Development/Languages
License:          ASL 2.0
URL:              https://github.com/redhat-openstack/pymod2pkg.git
Source0:          https://pypi.python.org/packages/source/p/pymod2pkg/pymod2pkg-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools
BuildRequires:    python2-devel


%description
pymod2pkg provides simple python function to translate python module names to
their corresponding distro package names.


%prep
%setup -q -n pymod2pkg-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc README.md
%license LICENSE
%{python2_sitelib}/pymod2pkg.py*
%{python2_sitelib}/pymod2pkg-%{version}-py?.?.egg-info


%changelog
* Tue Aug 11 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2.1-1
- Update to 0.2.1

* Wed Aug 05 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2-2
- Use python versioned macros
- List files instead of using wildcard

* Thu Jul 23 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.2-1
- Update to 0.2

* Fri Jul 17 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.1-1
- Initial version
