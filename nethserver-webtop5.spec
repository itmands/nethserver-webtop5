Summary: NethServer webtop5 configuration
Name: nethserver-webtop5
Version: 1.0.2
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source3: WebtopPassEncode.java
Source4: ListTimeZones.java
BuildArch: noarch

Requires: nethserver-mail-server, nethserver-postgresql, nethserver-httpd
Requires: php-process, php-pgsql, php-imap, php-ldap, php-mbstring, php-mcrypt
Requires: perl-libintl, perl-DBD-Pg
Requires: webtop5-core >= 1.0.2, webtop5-zpush
Requires: tomcat, java-1.7.0-openjdk

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

mkdir -p root/var/lib/tomcats/webtop/{logs,temp,webapps,work}
mkdir -p root/var/log/webtop
mkdir -p root/var/lib/nethserver/webtop/backup

mkdir -p root/usr/share/webtop/bin/
mkdir -p root/usr/share/webtop/updates/pre
mkdir -p root/usr/share/webtop/updates/post/main

for source in %{SOURCE3} %{SOURCE4}
do
    cp $source root/usr/share/webtop
    source=`basename $source`
    javac root/usr/share/webtop/$source
    rm -f root/usr/share/webtop/$source
done

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} \
  --dir /var/lib/nethserver/webtop 'attr(755, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/backup 'attr(755, postgres, postgres)' \
  --dir /var/lib/nethserver/webtop/domains 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/images 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/temp 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/nethserver/webtop/domains/NethServer/models 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/tomcats/webtop/conf 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/tomcats/webtop/logs 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/tomcats/webtop/temp 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/tomcats/webtop/webapps 'attr(-, tomcat, tomcat)' \
  --dir /var/lib/tomcats/webtop/work 'attr(-, tomcat, tomcat)' \
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
* Tue Mar 14 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- WebTop5: can't access with master user NethServer/dev#5239

* Thu Mar 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- WebTop 5: contacts don't work at all - Bug NethServer/dev#5237

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- WebTop 5 - NethServer/dev#5225

