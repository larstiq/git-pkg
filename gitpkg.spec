# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       gitpkg

# >> macros
# Magic
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
# << macros

Summary:    Helps manage packaging in git
Version:    0.0.3
Release:    2
Group:      Development
License:    GPLv2
BuildArch:  noarch
Source0:    gitpkg-0.0.1.tar.bz2
Source100:  gitpkg.yaml
Requires:   git
Requires:   pristine-tar
Requires:   python-yaml
BuildRequires:  python
BuildRequires:  python-distribute

%description
Allows the packaging to be maintained in a discrete git tree in the same git repo as the source

%package -n obs-service-gitpkg
Summary:    An OBS source service: Uses gitpkg to retrieve source
Group:      Development
Requires:   %{name} = %{version}-%{release}
Requires:   gitpkg

%description -n obs-service-gitpkg
Uses gitpkg to retrieve source


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_bindir}/gp_release
%{_bindir}/gp_setup
%{_bindir}/gp_mkpkg
%{_datadir}/gitpkg/gp_common
%{python_sitelib}/BlockDumper.py
%{python_sitelib}/BlockDumper.pyc
%{python_sitelib}/gitpkg-0.0.2-py2.7.egg-info
# >> files
# << files

%files -n obs-service-gitpkg
%defattr(-,root,root,-)
/usr/lib/obs/service/gitpkg
/usr/lib/obs/service/gitpkg.service
# >> files obs-service-gitpkg
# << files obs-service-gitpkg
