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

Example: ::

  webtop=configuration
      ActiveSync=enabled
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

See content of ``/etc/e-smith/templates/etc/sysconfig/tomcat/90webtop``.

Known problems
==============

When PostgreSQL is restarted, WebTop can loss the database connection.
If a blank page is displayed, restart Tomcat with the following command: ::

    systemctl restart tomcat
