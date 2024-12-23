%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%define title	Stellarium

Name:		stellarium 
Version:	24.4
Release:	1
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		https://www.stellarium.org
Source0:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:	ninja
BuildRequires:  gettext
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	qt6-qtbase-theme-gtk3

Requires:  	%{_lib}nlopt

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.

%prep 
%setup -q
%cmake -G Ninja

%build 
%ninja_build -C build

%install
%ninja_install -C build
# Missing install rules in the CMake files...
cp -a build/_deps/qxlsxqt6-build/libQXlsxQt6.so* %{buildroot}%{_libdir}/

%files
%doc README.md COPYING CREDITS.md
%{_bindir}/%{name}
%{_libdir}/libShowMySky-Qt6.so*
%{_libdir}/libQXlsxQt6.so*
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*.1.*
%{_datadir}/applications/org.stellarium.Stellarium.desktop
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*

