Summary:	Map application for GNOME
Name:		gnome-maps
Version:	3.10.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-maps/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	3845857151bbee5c828d4a40e61d6d9c
URL:		http://wiki.gnome.org/Maps
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.10
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter
Requires:	clutter-gtk
Requires:	cogl
Requires:	geocode-glib
Requires:	gjs
Requires:	glib2
Requires:	gtk+3
Requires:	hicolor-icon-theme
Requires:	libchamplain
Requires:	libsoup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Maps is a simple map application for the GNOME desktop.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/appdata/gnome-maps.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.maps.gschema.xml
%{_datadir}/gnome-maps
%{_desktopdir}/gnome-maps.desktop
%{_iconsdir}/hicolor/*/*/gnome-maps.png

