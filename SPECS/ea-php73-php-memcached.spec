%global scl_version ea-php73
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcached
Version: 3.1.3
Summary: php-memcached extension for %{scl_version}
%define release_prefix 8
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcached
Source: https://github.com/php-memcached-dev/php-memcached/archive/v3.1.3.tar.gz
Source1: memcached.ini

# should be no requires for building this package
#Requires: memcached
Requires: ea-libmemcached
BuildRequires: cyrus-sasl-devel
BuildRequires: ea-libmemcached ea-libmemcached-devel
Requires: %{scl_version}-php-common
Requires: %{scl_version}-php-cli
BuildRequires: %{scl_version}

%description
This is the PECL memcached extension, using the libmemcached library to connect
to memcached servers.


%prep
%setup -n php-memcached-%{version}

%build
scl enable %{scl_version} phpize
scl enable %{scl_version} './configure --with-libmemcached-dir=/opt/cpanel/libmemcached --with-libdir=lib64'
make

%install
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcached.so
%config /%{ext_prefix}/%{conf_dir}/memcached.ini

%changelog
* Mon Oct 28 2024 Julian Brown <julian.brown@cpanel.net> - 3.1.3-8
- ZC-12246: Correct conffiles for Ubuntu

* Thu Sep 21 2023 Dan Muey <dan@cpanel.net> - 3.1.3-7
- ZC-11194: Remove unnecessary `BuildRequires` of php-cli

* Fri Apr 07 2023 Julian Brown <julian.brown@cpanel.net> - 3.1.3-6
- ZC-10320: Do not build on Ubuntu 22.

* Mon Apr 20 2020 Daniel Muey <dan@cpanel.net> - 3.1.3-5
- ZC-6608: Fix Requires for PHP

* Mon Apr 13 2020 Tim Mullin <tim@cpanel.net> - 3.1.3-4
- EA-8978: Add php as a dependency

* Wed Apr 08 2020 Daniel Muey <dan@cpanel.net> - 3.1.3-3
- ZC-6515: Promote from experimental

* Thu Jun 13 2019 Tim Mullin <tim@cpanel.net> - 3.1.3-2
- EA-8224: Built with our ea-libmemcached module

* Thu Apr 25 2019 Tim Mullin <tim@cpanel.net> - 3.1.3-1
- EA-8302 - Update to 3.1.3 to support PHP 7.3

* Wed Mar  5 2017 Jack Hayhurst <jack@deleteos.com> - 2.2.7
- RPM actually building, fixed naming scheme to fit in with EA4

* Wed Mar  1 2017 Jack Hayhurst <jack@deleteos.com> - 2.2.7
- Initial spec file creation.
