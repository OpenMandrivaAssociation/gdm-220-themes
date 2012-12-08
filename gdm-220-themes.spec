%define pkgname gdm-themes
Summary:	Themes for Gnome Display Manager
Name:		gdm-220-themes
Version:	0.2
Release:	%mkrel 9
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-9mdv2011.0
+ Revision: 610822
- rebuild

* Mon May 03 2010 Frederic Crozat <fcrozat@mandriva.com> 0.2-8mdv2010.1
+ Revision: 541749
- Rename package to gdm-220-themes
- rename gdm-themes to gdm-220-themes

* Fri Apr 23 2010 Frederic Crozat <fcrozat@mandriva.com> 0.2-7mdv2010.1
+ Revision: 538301
- Requires old gdm

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdv2010.1
+ Revision: 522711
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2-5mdv2010.0
+ Revision: 424579
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.2-4mdv2009.1
+ Revision: 351195
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 221046
- rebuild

* Sun Mar 02 2008 Adam Williamson <awilliamson@mandriva.org> 0.2-2mdv2008.1
+ Revision: 177590
- update URL at john's request

* Fri Feb 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.2-1mdv2008.1
+ Revision: 176869
- new license policy
- new release 0.2: update images to use Mandriva instead of Mandrake (finally!)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2008.1
+ Revision: 150100
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2008.0
+ Revision: 70241
- use %%mkrel

