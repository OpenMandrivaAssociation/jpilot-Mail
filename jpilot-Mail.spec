Name:		jpilot-Mail
Version:	0.1.7
Release:	%mkrel 4
Summary:	Mail plugin for JPilot
Source0:	http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/%{name}-%{version}.tar.bz2
Patch0:		jpilot-Mail-0.1.7-gcc4.patch
URL:		http://ludovic.rousseau.free.fr/softwares/jpilot-Mail/index.html
Group:		Communications
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2 and GPLv2+
Requires:	jpilot >= 0.99.6
BuildRequires:	gtk2-devel 
BuildRequires:	jpilot_plugin-devel
BuildRequires:	pilot-link-devel >= 0.12.0

%description
jpilot-Mail is a plugin for JPilot which enables you to deliver mail that was
written on your Palm and upload mail that you received to your Palm.

%prep
rm -rf %{buildroot}
%setup -q
%patch0 -p1 -b .gcc4
# To build on x86_64
sed -i "s|/usr/lib |%_libdir |g" configure

%build
%configure2_5x --enable-gtk2
%make

%install
mkdir -p %{buildroot}%{_libdir}/jpilot/plugins
make install libdir=%{buildroot}%{_libdir}/jpilot/plugins datadir=%{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_libdir}/jpilot/plugins/*a

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_libdir}/jpilot/plugins/libmail.*
%doc doc/*.png doc/*.html
%doc ChangeLog INSTALL README TODO

