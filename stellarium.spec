%define name	stellarium
%define version	0.9.1
%define release	%mkrel 1
%define title	Stellarium

Name:		%{name} 
Version:	%{version} 
Release:	%{release} 
Summary:	Stellarium is a desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2 
URL:		http://www.stellarium.org
Source:		http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
Patch0:		stellarium-0.8.2-manpage.diff
Buildrequires:	mesaglu-devel 
Buildrequires:	SDL-devel
Buildrequires:	SDL_mixer-devel
Buildrequires:	png-devel
Buildrequires:	jpeg-devel
Buildrequires:	freetype2-devel
Buildrequires:	qt4-devel
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
Buildrequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q
%patch0 -p1 -b .manpage 

%build 
export QTDIR=/usr/lib/qt4
export PATH=$QTDIR/bin:$PATH
%cmake
%make


%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -c -p"

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=Desktop planetarium
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Astronomy;
EOF
%find_lang %{name}

%clean 
rm -rf %{buildroot} 

%post
%{update_menus}

%postun
%{clean_menus}

%files -f build/%{name}.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
