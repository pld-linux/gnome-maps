Summary:	Map application for GNOME
Summary(pl.UTF-8):	Mapa dla GNOME
Name:		gnome-maps
Version:	42.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-maps/42/%{name}-%{version}.tar.xz
# Source0-md5:	76270662fcff139a2577da8a57df7399
URL:		https://wiki.gnome.org/Apps/Maps
BuildRequires:	folks-devel >= 0.10.0
BuildRequires:	geoclue2-devel >= 0.12.99
BuildRequires:	geocode-glib-devel >= 3.15.2
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.66.0
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libchamplain-devel >= 0.12.14
BuildRequires:	libgee-devel >= 0.16.0
# only soup2 based is supported
BuildRequires:	libgweather4-devel >= 4.0
BuildRequires:	libhandy1-devel >= 1.5.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rest-devel >= 0.7.90
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.66.0
Requires(post,postun):	gtk-update-icon-cache
# see src/main.js for GI dependencies
Requires:	cairo >= 1.0
Requires:	clutter >= 1.0
Requires:	clutter-gtk >= 1.0
Requires:	cogl >= 1.0
Requires:	folks >= 0.10.0
Requires:	gdk-pixbuf2 >= 2.0
Requires:	geoclue2 >= 0.12.99
Requires:	geocode-glib >= 3.15.2
Requires:	gfbgraph >= 0.2
Requires:	gjs >= 1.66.0
Requires:	glib2 >= 1:2.66.0
Requires:	gnome-online-accounts >= 1.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	libchamplain >= 0.12.14
Requires:	libgee >= 0.16.0
Requires:	libgweather4 >= 4.0
Requires:	libhandy1 >= 1.5.0
Requires:	libsoup >= 2.4
Requires:	rest >= 0.7.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Maps is a simple map application for the GNOME desktop.

%description -l pl.UTF-8
GNOME Maps to prosta aplikacja dla środowiska GNOME służąca do obsługi
map.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-maps
%dir %{_libdir}/gnome-maps
%attr(755,root,root) %{_libdir}/gnome-maps/libgnome-maps.so*
%dir %{_libdir}/gnome-maps/girepository-1.0
%{_libdir}/gnome-maps/girepository-1.0/GnomeMaps-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/glib-2.0/schemas/org.gnome.Maps.gschema.xml
%dir %{_datadir}/gnome-maps
%dir %{_datadir}/gnome-maps/gir-1.0
%{_datadir}/gnome-maps/gir-1.0/GnomeMaps-1.0.gir
%attr(755,root,root) %{_datadir}/gnome-maps/org.gnome.Maps
%{_datadir}/gnome-maps/org.gnome.Maps.*.gresource
%{_datadir}/gnome-maps/icons
%{_datadir}/gnome-maps/maps-service.json
%{_datadir}/metainfo/org.gnome.Maps.appdata.xml
%{_desktopdir}/org.gnome.Maps.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Maps.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Maps-symbolic.svg
