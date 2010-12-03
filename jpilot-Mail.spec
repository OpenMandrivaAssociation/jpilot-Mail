Summary:	Mail plugin for JPilot
Name:		jpilot-Mail
Version:	0.1.7
Release:	%mkrel 9
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
