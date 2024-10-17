%define oname openastromenace

Summary:	Hardcore 3D space shooter with spaceship upgrade possibilities
Name:		astromenace
Version:	1.4.2
Release:	1
License:	GPLv3+
Group:		Games/Arcade
Url:		https://www.viewizard.com/
Source0:	https://github.com/viewizard/astromenace/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	cmake ninja
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
Obsoletes:	%{name}-data < %{EVRD}
Obsoletes:	%{name}-data-ru < %{EVRD}
Obsoletes:	%{name}-data-de < %{EVRD}

%description
Space is a vast area, an unbounded territory where it seems there is a 
room for everybody, but reversal of fortune put things differently. The 
hordes of hostile creatures crawled out from the dark corners of the
universe, craving to conquer your homeland. Their force is compelling,
their legions are interminable. However, humans didn't give up without
a final showdown and put their best pilot to fight back. These malicious
invaders chose the wrong galaxy to conquer and you are to prove it! 
Go ahead and make alien aggressors regret their insolence.

%prep
%autosetup -p1
sed -i 's/\r//' LICENSE.md
sed -i 's/\r//' README.md

chmod -x LICENSE.md README.md share/*.png

%cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DDATADIR=/usr/share/astromenace \
	-G Ninja

%build
%ninja_build -C build

cd build
./astromenace --pack --rawdata=../gamedata --dir=.


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 build/astromenace %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 build/gamedata.vfs %{buildroot}%{_datadir}/%{name}/gamedata.vfs

desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  share/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 share/*.appdata.xml %{buildroot}%{_datadir}/metainfo/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 share/%{name}_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 share/%{name}_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/astromenace.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
