Name:             python-pymod2pkg
Version:          0.1
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
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc README.md
%license LICENSE
%{python_sitelib}/*


%changelog
* Fri Jul 17 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.1-1
- Initial version