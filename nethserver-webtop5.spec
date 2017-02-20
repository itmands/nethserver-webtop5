Summary: NethServer webtop5 configuration
Name: nethserver-webtop5
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source3: WebtopPassEncode.java
BuildArch: noarch

Requires: nethserver-mail-server, nethserver-postgresql, nethserver-tomcat, nethserver-httpd
Requires: php-process, php-pgsql, php-imap, php-ldap, php-mbstring
Requires: perl-libintl, perl-DBD-Pg
Requires: webtop5-core, webtop5-zpush

BuildRequires: perl, java-1.7.0-openjdk-devel
BuildRequires: nethserver-devtools 

%description
NethServer webtop configuration

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/var/lib/nethserver/webtop/domains/NethServer
mkdir -p root/var/lib/nethserver/webtop/domains/NethServer/images
mkdir -p root/var/lib/nethserver/webtop/domains/NethServer/temp
mkdir -p root/var/lib/nethserver/webtop/domains/NethServer/models

mkdir -p root/var/log/webtop
mkdir -p root/var/lib/nethserver/webtop/backup

mkdir -p root/usr/share/webtop/bin/
mkdir -p root/usr/share/webtop/updates/pre
mkdir -p root/usr/share/webtop/updates/post/main

cp %{SOURCE3} root/usr/share/webtop
javac root/usr/share/webtop/WebtopPassEncode.java
rm -f root/usr/share/webtop/WebtopPassEncode.java

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} \
  --dir /var/lib/nethserver/webtop 'attr(755, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/backup 'attr(755, postgres, postgres)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/images 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/temp 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/models 'attr(-, tomcat, tomcat)' \
  --dir /var/log/webtop 'attr(-, tomcat, tomcat)' \
 > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%config %ghost %attr (0644,root,root) %{_sysconfdir}/httpd/conf.d/webtop.conf
%dir %{_nseventsdir}/%{name}-update
%dir /usr/share/webtop/updates/pre
%dir /usr/share/webtop/updates/post
%dir /usr/share/webtop/updates/post/main
%doc COPYING
%doc README.rst

%changelog
