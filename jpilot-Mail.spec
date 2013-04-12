%define _disable_ld_no_undefined 1

Summary:	Mail plugin for JPilot
Name:		jpilot-Mail
Version:	0.1.7
Release:	12
License:	GPLv2 and GPLv2+
Group:		Communications
URL:		http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/index.html
Source0:	http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/%{name}-%{version}.tar.bz2
Patch0:		jpilot-Mail-0.1.7-gcc4.patch
Patch1:		jpilot-Mail-0.1.7-libdir_fix.diff
Requires:	jpilot >= 0.99.6
BuildRequires:	gtk2-devel 
BuildRequires:	jpilot-devel >= 0.99.6
BuildRequires:	pilot-link-devel >= 0.12.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
jpilot-Mail is a plugin for JPilot which enables you to deliver mail that was
written on your Palm and upload mail that you received to your Palm.

%prep

%setup -q
%patch0 -p1 -b .gcc4
%patch1 -p1 -b .libdir_fix

# To build on x86_64
sed -i "s|/usr/lib |%_libdir |g" configure*

%build
%configure2_5x --enable-gtk2
%make

%install
rm -rf %{buildroot}

%makeinstall libdir=%{buildroot}%{_libdir}/jpilot/plugins datadir=%{buildroot}%{_docdir}/%{name}

rm -f %{buildroot}%{_libdir}/jpilot/plugins/*a

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc doc/*.png doc/*.html
%doc ChangeLog README TODO
%{_libdir}/jpilot/plugins/libmail.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-10mdv2011.0
+ Revision: 665832
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-9mdv2011.0
+ Revision: 606108
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-8mdv2010.1
+ Revision: 523088
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.7-7mdv2010.0
+ Revision: 425467
- rebuild

* Mon Nov 10 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-6mdv2009.1
+ Revision: 301749
- fix libdir
- fix deps

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.7-5mdv2009.0
+ Revision: 221748
- rebuild
- fix no-buildroot-tag

* Fri Dec 21 2007 Adam Williamson <awilliamson@mandriva.org> 0.1.7-4mdv2008.1
+ Revision: 136127
- unversion doc dir
- rebuild for new era
- new license policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Pascal Terjan <pterjan@mandriva.org> 0.1.7-3mdv2007.1
+ Revision: 134781
- fix build on x86_64
- use autoconf2.5
- Import jpilot-Mail

* Wed Sep 06 2006 Frederic Crozat <fcrozat@mandriva.com> 0.1.7-2mdv2007.0
- Rebuild with new pilot-link

* Mon May 29 2006 Stefan van der Eijk <stefan@eijk.nu> 0.1.7-1
- update from Cris B <cris@beebgames.com>
   - update URL
   - gcc4 patch
   - switch to gtk2

* Mon May 29 2006 Stefan van der Eijk <stefan@eijk.nu> 0.0.6-10mdk
- %%mkrel
- remove redundant BuildRequires

* Mon Jan 16 2006 Frederic Crozat <fcrozat@mandriva.com> 0.0.6-9mdk
- Rebuild

