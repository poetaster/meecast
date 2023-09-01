# 
# Do not Edit! Generated by:
# spectacle version 0.18
# 
%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Name:       harbour-meecast
Summary:    Weather forecast application for SailfishOS
Version:    1.1.33
Release:    1 
Group:      Utility
License:    GPLv2.1
URL:        https://github.com/Meecast/meecast 
Source0:    %{name}-%{version}.tar.bz2
#Temporary
#Requires:       libmeegotouch-devel
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(sqlite3)
#BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libxml-2.0)
#BuildRequires:  libxml2-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig(dconf) 
BuildRequires:  libkeepalive-devel
#BuildRequires:  libqt-devel
BuildRequires: qt5-qtpositioning-devel
#Requires:      qt5-qtpositioning 
#Requires:      sailfishsilica-qt5
#Requires:      qt5-qtdeclarative-import-models2 
#Requires:      zlib 

%description
MeeCast - multiplatform highly customizable open source weather forecast client based on OMWeather code

%package daemon
Version: 1.8
Release: 1 
Summary: Daemon for Weather forecast application MeeCast on SailfishOS
Group:      Utility
License:    GPLv2.1
Requires:   harbour-meecast    
BuildRequires:  pkgconfig(contentaction5)
%description daemon
MeeCast daemon for multiplatform highly customizable open source weather forecast client based on OMWeather code

%package lockscreen
Version: 0.4
Summary: Lockscreen Widget for Weather forecast application MeeCast on SailfishOS
Group:      Utility
License:    GPLv2.1
Requires: harbour-meecast 
Requires: harbour-meecast-daemon => 0.3 
Requires: patchmanager
%description lockscreen
MeeCast Lockscreen widget for multiplatform highly customizable open source weather forecast client based on OMWeather code

%package event
Version: 1.0
Release: 4 
Summary: Event Widget for Weather forecast application MeeCast on SailfishOS
Group:      Utility
License:    GPLv2.1
Requires: harbour-meecast 
Requires: harbour-meecast-daemon => 0.9 
%description event
MeeCast event widget for multiplatform highly customizable open source weather forecast client based on OMWeather code


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
ls
echo "Test1"
/usr/lib/qt5/bin/qmake *.pro
echo "Test2"
make

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%qmake5_install
#make INSTALL_ROOT=%{buildroot} install
#rm %{buildroot}/opt/com.meecast.omweather/lib/libomweather-core.a
# << install post
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop


%pre lockscreen
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u sailfishos-lockscreen-meecast-patch || true
fi

%pre daemon

%preun daemon
if [ "$1" = "0" ]; then
    systemctl-user disable meecastd.service
    systemctl-user stop meecastd.service    
fi

%preun lockscreen
if [ -f /usr/sbin/patchmanager ]; then
    /usr/sbin/patchmanager -u sailfishos-lockscreen-meecast-patch || true
fi

%postun daemon
#systemctl-user disable meecastd.service
#systemctl-user stop meecastd.service    
#if ps -A | grep "meecastd" ; then killall meecastd ; fi
#systemctl-user daemon-reload

%post daemon
if ps -A | grep "meecastd" ; then killall meecastd ; fi
systemctl-user enable meecastd.service
systemctl-user start meecastd.service    

%post lockscreen 
if ps -A | grep "meecastd" ; then killall meecastd ; fi
systemctl-user enable meecastd.service
systemctl-user start meecastd.service    

%files
%defattr(-,root,root,-)
/usr/share/applications/harbour-meecast.desktop
/usr/bin/harbour-meecast
/usr/share/harbour-meecast
#/usr/share/iconsets
/usr/share/icons/hicolor
#/opt/com.meecast.omweather/share

%files daemon
%defattr(-,root,root,-)
/usr/bin/meecastd
/usr/bin/meecast_predaemon
/usr/lib/systemd/user/meecastd.service
%{_libdir}/qt5/qml/org/meecast/data

%files lockscreen 
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-lockscreen-meecast-patch

%files event 
%defattr(-,root,root,-)
#/usr/lib/qt5/qml/Sailfish/Weather
%{_libdir}/qt5/qml/Sailfish/Weather


# << files


