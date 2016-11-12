Summary:	Map application for GNOME
Summary(pl.UTF-8):	Mapa dla GNOME
Name:		gnome-maps
Version:	3.22.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-maps/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	7a1e0f10b00019024893368e3e80401f
Patch0:		%{name}-build.patch
URL:		https://wiki.gnome.org/Apps/Maps
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	folks-devel >= 0.10.0
BuildRequires:	geoclue2-devel >= 0.12.99
BuildRequires:	geocode-glib-devel >= 3.15.2
BuildRequires:	gjs-devel >= 1.44.0
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libchamplain-devel >= 0.12.14
BuildRequires:	libgee-devel >= 0.16.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rest-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	clutter
Requires:	clutter-gtk
Requires:	cogl
Requires:	folks >= 0.10.0
Requires:	geocode-glib >= 3.15.2
Requires:	gjs >= 1.44.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.16.0
Requires:	hicolor-icon-theme
Requires:	libchamplain >= 0.12.14
Requires:	libgee >= 0.16.0
Requires:	libsoup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Maps is a simple map application for the GNOME desktop.

%description -l pl.UTF-8
GNOME Maps to prosta aplikacja dla środowiska GNOME służąca do obsługi
map.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-maps/*.la

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
%{_datadir}/appdata/org.gnome.Maps.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/gir-1.0/GnomeMaps-1.0.gir
%{_datadir}/glib-2.0/schemas/org.gnome.Maps.gschema.xml
%dir %{_datadir}/gnome-maps
%attr(755,root,root) %{_datadir}/gnome-maps/org.gnome.Maps
%{_datadir}/gnome-maps/org.gnome.Maps.*.gresource
%{_datadir}/gnome-maps/icons
%{_datadir}/gnome-maps/maps-service.json
%{_desktopdir}/org.gnome.Maps.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Maps.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Maps-symbolic.svg
