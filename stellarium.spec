
%define title	Stellarium

Name:		stellarium 
Version:	1.2
Release:	1
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		http://www.stellarium.org
Source0:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:  gettext
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Help)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(VulkanHeaders)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.

%prep 
%setup -q

%build 
#export CC=gcc
#export CXX=g++
%cmake -DENABLE_SHOWMYSKY=no
%make_build

%install
%make_install -C build

%files
%doc README.md COPYING CREDITS.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*.1.*
%{_datadir}/applications/org.stellarium.Stellarium.desktop
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*

