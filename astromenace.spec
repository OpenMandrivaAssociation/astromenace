Name:		astromenace
Version:	1.2
Release:	%mkrel 1
Summary:	Hardcore 3D space shooter with spaceship upgrade possibilities
Group:		Games/Arcade
License:	GPLv3
URL:		http://www.viewizard.com/
Source0:	http://www.viewizard.com/download/AstroMenaceSourceCode_080519.zip
Source1:	astromenace.desktop
Source2:	astromenace.png
Patch0:		astromenace-langvfs.patch
Patch1:		astromenace-640x480.patch
Patch2:		astromenace-programmdir.patch
Patch3:		astromenace-1.2-str-fmt.patch
Patch4:		astromenace-system-glext.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	openal-devel
BuildRequires:	freealut-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libjpeg-devel
BuildRequires:	desktop-file-utils
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

%prep
%setup -qn AstroMenaceSourceCode

sed -i 's/\r//' License.txt
sed -i 's/\r//' gpl-3.0.txt
chmod -x License.txt
chmod -x ReadMe.txt
chmod -x gpl-3.0.txt

%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
%cmake
%make

%install
cd ./build
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_bindir}
install -m 755 AstroMenace %{buildroot}%{_bindir}/astromenace

desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ReadMe.txt License.txt gpl-3.0.txt
%{_bindir}/astromenace
%{_datadir}/applications/astromenace.desktop
%{_datadir}/icons/hicolor/64x64/apps/astromenace.png

