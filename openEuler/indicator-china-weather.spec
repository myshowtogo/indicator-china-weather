%define debug_package %{nil}
Name:           indicator-china-weather
Version:        3.0.4
Release:        1
Summary:        The weather data are from the heweather API s6 version.
License:        GPL-3+
URL:            https://github.com/UbuntuKylin/indicator-china-weather
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qtchooser
# BuildRequires:  qtbase5-dev-tools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconf
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  GeoIP-devel

# Requires: NetworkManager

%description
 Indicator that displays China weather information
 Kylin Weather displays detail weather information for one place,
 including weather forecast and observe weather, and you can
 change it.

%prep
%setup -q

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  indicator-china-weather.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/bin/
mkdir -p %{buildroot}/usr/share/doc/indicator-china-weather/
mkdir -p %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/indicator-china-weather/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/indicator-china-weather/changelog.gz
gzip -c man/indicator-china-weather.1	> %{buildroot}/usr/share/man/man1/indicator-china-weather.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/xdg/autostart/indicator-china-weather.desktop
%{_bindir}/indicator-china-weather
%{_datadir}/applications/indicator-china-weather.desktop
%{_datadir}/doc/indicator-china-weather/changelog.gz
%{_datadir}/doc/indicator-china-weather/copyright
%{_datadir}/glib-2.0/schemas/org.china-weather-data.gschema.xml
%{_datadir}/indicator-china-weather/translations/indicator-china-weather_bo.qm
%{_datadir}/indicator-china-weather/translations/indicator-china-weather_zh_CN.qm
%{_datadir}/man/man1/indicator-china-weather.1.gz

%changelog
* Wed Dec 30 2020 lvhan <lvhan@kylinos.cn> - 3.0.4-1
- update to upstream version 3.0.4