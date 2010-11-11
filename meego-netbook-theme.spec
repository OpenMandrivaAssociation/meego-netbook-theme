Name: meego-netbook-theme
Summary: MeeGo Netbook Theme
Version: 0.1
Release: %mkrel 1
Group: System/Desktop
License: LGPL v2.1
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Requires: gnome-settings-daemon
BuildRequires: libgtk+2-devel
Obsoletes: moblin-gtk-engine <= 1.0.2

%description
Theme for MeeGo Netbooks

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm %{buildroot}%{_libdir}/gtk-2.0/2.10.0/engines/libmeego-netbook.la

%files
%defattr(-,root,root,-)
%doc README COPYING.LIB AUTHORS
%{_libdir}/gtk-2.0/2.10.0/engines/libmeego-netbook.so
%dir %{_datadir}/themes/Netbook/gtk-2.0/Assets
%{_datadir}/themes/Netbook/gtk-2.0/Assets/*.png
%{_datadir}/themes/Netbook/gtk-2.0/gtkrc
%{_datadir}/themes/Netbook/index.theme
%dir %{_datadir}/themes/Netbook/metacity-1
%{_datadir}/themes/Netbook/metacity-1/*.png
%{_datadir}/themes/Netbook/metacity-1/metacity-theme-1.xml
