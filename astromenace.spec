%define oname openastromenace

Summary:	Hardcore 3D space shooter with spaceship upgrade possibilities
Name:		astromenace
Version:	1.3.2
Release:	2
License:	GPLv3+
Group:		Games/Arcade
Url:		http://www.viewizard.com/
Source0:	http://sourceforge.net/projects/openastromenace/files/%{version}/%{name}-src-%{version}.tar.bz2
Source1:	astromenace.desktop
BuildRequires:	cmake
BuildRequires:	pkgconfig(freealut)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	jpeg-devel
BuildRequires:	desktop-file-utils
Provides:	%{oname} = %{version}-%{release}
Requires:	%{name}-data = %{version}

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
Obsoletes:	astromenace-data < 1.3.1
Obsoletes:	astromenace-data-ru < 1.3.1
Obsoletes:	astromenace-data-de < 1.3.1

%description data
This package provides game data for AstroMenace.

%prep
%setup -qn AstroMenace
sed -i 's/\r//' License.txt
sed -i 's/\r//' gpl-3.0.txt
sed -i 's/\r//' ReadMe.txt

chmod -x License.txt
chmod -x ReadMe.txt
chmod -x gpl-3.0.txt

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DDATADIR=/usr/share/astromenace
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
%doc ReadMe.txt License.txt 
%{_bindir}/%{name}
%{_datadir}/applications/astromenace.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files data
%doc gpl-3.0.txt
%{_datadir}/%{name}


