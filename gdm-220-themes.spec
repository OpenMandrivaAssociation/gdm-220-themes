%define pkgname gdm-themes
Summary:	Themes for Gnome Display Manager
Name:		gdm-220-themes
Version:	0.2
Release:	%mkrel 10
# Want a new version? Ask John Keller to make it. - AdamW 2008/02
Source0:	%{pkgname}-%{version}.tar.lzma
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/packages/cooker/gdm-themes
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	gdm-220

%description
This package contains themes for gdm, the Gnome Display Manager.
It provides three themes:
- Enterprise-spot
- Enterprise
- RadiantStar

%prep
%setup -q -n %{pkgname}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gdm/themes/
cp -a * %{buildroot}%{_datadir}/gdm/themes/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gdm/themes/*

