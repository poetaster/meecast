# 
# Do not Edit! Generated by:
# spectacle version 0.18
# 
# >> macros
%define all_x86 i386 i586 i686 %{ix86}
%define all_arm %{arm}
# << macros

Name:       omweather
Summary:    Weather for Meego
Version:    0.3.11
Release:    1
Group:      Applications/Internet
License:    GPLv2.1
URL:        https://garage.maemo.org/projects/omweather/
Source0:    %{name}-%{version}.tar.bz2
Source100:  omweather.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libxml-2.0)
%ifarch %{all_x86} 
BuildRequires:  pkgconfig(meego-panel)
BuildRequires:  pkgconfig(mutter-plugins)
%endif
BuildRequires:  gettext
BuildRequires:  qt-qmake
BuildRequires:  libqt-devel
BuildRequires:  libmeegotouch-devel
BuildRequires:  desktop-file-utils


%description
Weather Forecast on Meego.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
#export PATH=/usr/lib/qt4/bin:$PATH
qmake PREFIX=%{_prefix} -r
make
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
make INSTALL_ROOT=%{buildroot} install
%ifarch %{all_x86}
ln -s /usr/share/omweather/icons  %{buildroot}/usr/share/meego-panel-omweather/theme/icons
%endif
rm %{buildroot}/usr/lib/libomweather-core.so
# << install post
desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop



%post
# >> post
/sbin/ldconfig
# << post

%postun
# >> postun
/sbin/ldconfig
# << postun


%files
%defattr(-,root,root,-)
/usr/bin/omweather-qml
/usr/bin/omweather-settings
%{_datadir}/applications/*.desktop
%{_libdir}
/usr/share/omweather
/usr/share/locale
/usr/share/pixmaps
/usr/lib/omweather/weathercom
/usr/share/omweather/copyright_icons/weather.com.png
/usr/share/omweather/db/weather.com.db
/usr/share/omweather/sources/weather.com.xml
# >> files
%ifarch %{all_x86}
%{_libexecdir}/meego-panel-omweather
/usr/share/meego-panel-omweather
/usr/share/mutter-meego/panels/meego-panel-omweather.desktop
/etc/xdg
/usr/share/dbus-1/services
%endif
%changelog
* Thu Mar 10 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.11
  * Began adding temeperature day
  * Added new source of weather forecast gismeteo.ru
  * Redesigned qml window
  * Began added MeegoTouch setting  
* Sat Mar 5 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.10
  * Fixed spelling mistake
  * Changed default icon to N/A in meego panel
* Sat Feb 26 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.9
  * Fixed problem with Temperature unit
  * Improvements in config and QML window
* Mon Feb 21 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.8
  * Fixed problem with time for forecast.
  * Fixed QML forms
  * Added Night box for detail window
* Fri Feb 19 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.7
  * Added transaltion for wind and forecast's description
* Fri Feb 19 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.6
  * Added Russian translate to omweather-settings
* Fri Feb 18 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.5
  * Added animation for meego panel
* Wed Feb 16 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.4
  * Added icon to desktop. Added translation to QML.
  * Added button 'close' to qml
* Tue Feb 15 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.3 
  * Updated QML version of Omweather
* Mon Feb 14 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.2
  * Updated QML version of Omweather
* Sun Feb 13 2010  Vlad Vasilyeu <vasvlad@gmail.com> 0.3.1
  * Added QML version of Omweather
* Wed Feb 9 2010 Vlad Vasilyeu <vasvlad@gmail.com> 0.3
  * Initial version
# << files


