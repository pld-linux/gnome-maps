# TODO: switch to gtk4-update-icon-cache
Summary:	Map application for GNOME
Summary(pl.UTF-8):	Mapa dla GNOME
Name:		gnome-maps
Version:	45.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-maps/45/%{name}-%{version}.tar.xz
# Source0-md5:	d6d096d2819ab94ea8d15f06894cd6ef
URL:		https://wiki.gnome.org/Apps/Maps
BuildRequires:	geoclue2-devel >= 0.12.99
BuildRequires:	geocode-glib2-devel >= 3.26
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel >= 1.69.2
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk4-devel >= 4
BuildRequires:	libadwaita-devel >= 1.4
# soup3 based
BuildRequires:	libgweather4-devel >= 4.0
BuildRequires:	libportal-devel
# soup3 based
BuildRequires:	libshumate-devel >= 1.1
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.61.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rest1-devel >= 0.9
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.66.0
Requires(post,postun):	gtk-update-icon-cache
# see src/main.js for GI dependencies
Requires:	cairo >= 1.0
Requires:	gdk-pixbuf2 >= 2.0
Requires:	geoclue2 >= 0.12.99
Requires:	geocode-glib2 >= 3.26
Requires:	gjs >= 1.69.2
Requires:	glib2 >= 1:2.66.0
Requires:	gnome-online-accounts >= 1.0
Requires:	gtk4 >= 4.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.4
Requires:	libgweather4 >= 4.0
Requires:	libshumate >= 1.1
Requires:	libsoup3 >= 3
Requires:	rest1 >= 0.9
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
