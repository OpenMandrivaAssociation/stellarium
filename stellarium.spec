%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%define title	Stellarium

Name:		stellarium
Version:	26.2
Release:	1
Summary:	Desktop planetarium
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		https://www.stellarium.org
Source0:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildSystem:	cmake
BuildOption:	-DCPM_USE_LOCAL_PACKAGES:BOOL=ON -DCPM_LOCAL_PACKAGES_ONLY:BOOL=ON
BuildRequires:	ninja
BuildRequires:	gettext
BuildRequires:	perl-podlators
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiPrivate)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6SerialPort)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(ShowMySky-Qt6)
BuildRequires:	cmake(QXlsxQt6)
BuildRequires:	cmake(NLopt)
BuildRequires:	cmake(md4c)
BuildRequires:	pkgconfig(md4c-html)
BuildRequires:	pkgconfig(libindi)
# libindi/libastro.h includes libnova headers; indi-devel does not require them.
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libgps)
BuildRequires:	pkgconfig(xcb-xkb)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(zlib)

# Loaded with QLibrary, so the ELF dependency generator does not see it.
Requires:	%{_lib}CalcMySky

%patchlist
stellarium-26.2-qt6.10-guiprivate.patch

%description
Stellarium renders 3D photo-realistic skies in real time.
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.

%files
%doc README.md COPYING CREDITS.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*.1.*
%{_datadir}/applications/org.stellarium.Stellarium.desktop
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
