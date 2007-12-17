%define name    jpilot-Mail
%define version 0.1.7
%define release %mkrel 3
%define url http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/index.html 

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Mail plugin for jpilot
Source:    %{name}-%{version}.tar.bz2
Patch0:    jpilot-Mail-0.1.7-gcc4.patch
URL:       %{url}
Group:     Communications
License: GPL
Requires:  jpilot >= 0.99.6
BuildRequires: gtk2-devel jpilot_plugin-devel pilot-link-devel >= 0.11.8
Buildrequires: autoconf2.5

%description
jpilot-Mail is a plugin for jpilot which enables you to deliver mail that was
written on your pilot and upload mail that you received to your pilot.

%prep
rm -rf %buildroot

%setup -q
%patch0 -p1
# To build on x86_64
sed -i "s|/usr/lib |%_libdir |g" configure

%build
%configure2_5x --enable-gtk2
%make

%install
mkdir -p %buildroot%{_libdir}/jpilot/plugins
make install libdir=%buildroot%{_libdir}/jpilot/plugins datadir=%buildroot%{_docdir}/%{name}-%{version}
rm -f %buildroot%{_libdir}/jpilot/plugins/*a

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%{_libdir}/jpilot/plugins/libmail.*
%doc doc/*.png doc/*.html
%doc COPYING ChangeLog INSTALL README TODO


