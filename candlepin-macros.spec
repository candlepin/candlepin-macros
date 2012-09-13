%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio
%define __jar_repack %{nil}

Name: candlepin-macros
Summary: RPM build macros for Candlepin
Group: Internet/Applications
License: GPL
Version: 0.1.1
Release: 1%{?dist}
URL: https://github.com/candlepin/candlepin-macros
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: Red Hat, Inc
BuildArch: noarch

%description
RPM build macros to build Candlepin with candlepin-deps instead of regular
build requires when needed.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
install -m 644 macros.candlepin $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.candlepin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/rpm/macros.candlepin

%changelog
* Thu Sep 13 2012 jesus m. rodriguez <jesusr@redhat.com> 0.1.1-1
- add macros.candlepin to rpm macros
- new package built with tito

