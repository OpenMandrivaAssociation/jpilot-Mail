%define _disable_ld_no_undefined 1
%define debug_package %{nil}

Summary:	Mail plugin for JPilot
Name:		jpilot-Mail
Version:	0.1.7
Release:	15
License:	GPLv2 and GPLv2+
Group:		Communications
Url:		http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/index.html
Source0:	http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/%{name}-%{version}.tar.bz2
Patch0:		jpilot-Mail-0.1.7-gcc4.patch
Patch1:		jpilot-Mail-0.1.7-libdir_fix.diff

BuildRequires:	jpilot-devel >= 0.99.6
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pilot-link)
Requires:	jpilot >= 0.99.6

%description
jpilot-Mail is a plugin for JPilot which enables you to deliver mail that was
written on your Palm and upload mail that you received to your Palm.

%prep

%setup -q
%apply_patches

# To build on x86_64
sed -i "s|/usr/lib |%_libdir |g" configure*

%build
%configure2_5x \
	--disable-static \
	--enable-gtk2
%make

%install
%makeinstall libdir=%{buildroot}%{_libdir}/jpilot/plugins datadir=%{buildroot}%{_docdir}/%{name}

%files
%doc doc/*.png doc/*.html
%doc ChangeLog README TODO
%{_libdir}/jpilot/plugins/libmail.so

