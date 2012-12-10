%define oname openastromenace

Name:		astromenace
Version:	1.3.0
Release:	1
Summary:	Hardcore 3D space shooter with spaceship upgrade possibilities
Group:		Games/Arcade
License:	GPLv3
URL:		http://www.viewizard.com/
Source0:	http://sourceforge.net/projects/openastromenace/files/%{version}/%{oname}-src-%{version}.tar.bz2
Source1:	astromenace.desktop
Patch0:		astromenace-system-glext.patch
Patch1:		astromenace-1.3.0-config.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(freealut)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	jpeg-devel
BuildRequires:	desktop-file-utils
Provides:	%{oname} = %{version}-%{release}
Requires:	astromenace-data = %{version}

%description
Space is a vast area, an unbounded territory where it seems there is a 
room for everybody, but reversal of fortune put things differently. The 
hordes of hostile creatures crawled out from the dark corners of the
universe, craving to conquer your homeland. Their force is compelling,
their legions are interminable. However, humans didn't give up without
a final showdown and put their best pilot to fight back. These malicious
invaders chose the wrong galaxy to conquer and you are to prove it! 
Go ahead and make alien aggressors regret their insolence.

%package data
Summary:	Game data for AstroMenace game
Requires:	%{name} = %{version}
Obsoletes:	astromenace-data < 1.3.0
Obsoletes:	astromenace-data-ru < 1.3.0
Obsoletes:	astromenace-data-de < 1.3.0

%description data
This package provides game data for AstroMenace.

%prep
%setup -qn AstroMenace
sed -i 's/\r//' License.txt
sed -i 's/\r//' gpl-3.0.txt
chmod -x License.txt
chmod -x ReadMe.txt
chmod -x gpl-3.0.txt
%patch0 -p1
%patch1 -p1

%build
%cmake
%make
./AstroMenace --pack --rawdata=../RAW_VFS_DATA --dir=.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 build/AstroMenace %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 build/gamedata.vfs %{buildroot}%{_datadir}/%{name}/gamedata.vfs

desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{name}_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 %{name}_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files
%doc ReadMe.txt License.txt gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/astromenace.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files data
%{_datadir}/%{name}

%changelog
* Mon Sep 26 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2-1
+ Revision: 701334
- imported package astromenace


* Mon Sep 26 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.2-1mdv2010.2
- Spec clean up

* Sat Nov 21 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 1.2-1mib2009.1
- Added Patch3
- First build for MIB users
