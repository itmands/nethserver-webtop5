==================
nethserver-webtop5
==================

WebTop 5 is a full-featured groupware written in Java.

It's composed by three parts:

* Java web application running on Tomcat 7
* PHP implementation of Active Sync protocol
* PostgreSQL database

Access to web application is forced in SSL mode.

Database
========

Configuration is saved in ``webtop`` key inside ``configuration`` database.

Available properties:

* ``PublicUrl``: public URL used to publish resources for the cloud. If not set, default is ``http://<FQDN>/webtop``
* ``ActiveSync``: if set to ``enabled``, it enables /Microsoft-Server-ActiveSync url.  Default is ``enabled``
* ``MinMemory`` and ``MaxMemory``: minimun and maximum memory of Tomcat instance. Values are expressed in MB.

Example: ::

  webtop=configuration
      ActiveSync=enabled
      MaxMemory=1024
      MinMemory=512
      PublicUrl=


Configuration can be applied using the ``nethserver-webtop5-update`` event.

Troubleshooting
===============

In case of errors, see following logs:

* Tomcat: ``journalctl -u tomcat@webtop``
* Active Sync: :file:`/var/log/z-push/z-push-error.log`

To inspect z-push status use: ::

    php /usr/share/webtop/z-push/z-push-admin.php

Tomcat instance
===============

WebTop uses its own Tomcat instance running on port 58080.

The instance is launched with some special Java options,
see content of ``/etc/sysconfig/tomcat/tomcat@webtop``.

