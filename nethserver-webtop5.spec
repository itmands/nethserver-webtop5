Summary: NethServer webtop5 configuration
Name: nethserver-webtop5
Version: 1.2.3
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source4: ListTimeZones.java
BuildArch: noarch

Requires: nethserver-mail-server, nethserver-postgresql, nethserver-httpd
Requires: php-process, php-pgsql, php-imap, php-ldap, php-mbstring, php-mcrypt
Requires: perl-libintl, perl-DBD-Pg
Requires: webtop5 >= 1.2.4, webtop5-zpush, webtop5-webdav
Requires: tomcat, java-1.8.0-openjdk
Requires: nethserver-rh-php56-php-fpm

BuildRequires: perl, java-1.8.0-openjdk-devel
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

for source in %{SOURCE4}
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
  --file /etc/sudoers.d/webtop 'attr(0440, root, root)' \
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
* Thu May 17 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.3-1
- WebTop 5.1.9 - NethServer/dev#5487

* Thu Apr 26 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.2-1
- WebTop 5.1.8 - NethServer/dev#5463

* Wed Feb 21 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 1.2.1-1
- WebTop 5.1.7 - NethServer/dev#5423

* Tue Jan 30 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- WebTop 5.1.5 - NethServer/dev#5414

* Tue Jan 09 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.7-1
- WebTop 5: installation fails on ext4 - NethServer/dev#5405

* Wed Nov 29 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.6-1
- WebTop 5.1.4 - NethServer/dev#5376

* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.5-1
- db: handle multiline encrypted password - NS 7.4

* Fri Sep 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.4-1
- WebTop 5.0.13 - NethServer/dev#5338
- Disable iCal4j timezone update
- Avoid automatic deploy for future releases

* Mon Sep 04 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- WebTop 5.0.13 - NethServer/dev#5338

* Thu Jul 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- WebTop5: Outlook PST import - NethServer/dev#5244

* Thu Jun 22 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- WebTop 5.0.7 - NethServer/dev#5312
- Implement log rotation with logrotate
- Clear Tomcat cache dir on service restart

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- WebTop 5: enable folder sorting - NethServer/dev#5275
- Build RPM from source

* Mon Mar 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- WebTop 5: upgrade to RC6 - NethServer/dev#5250
- WebTop5: extended time format not set - Bug NethServer/dev#5254

* Tue Mar 14 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- WebTop5: can't access with master user NethServer/dev#5239

* Thu Mar 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- WebTop 5: contacts don't work at all - Bug NethServer/dev#5237

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- WebTop 5 - NethServer/dev#5225

