---
author: rickymoorhouse
comments: true
date: 2010-09-06 14:17:12+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/09/06/recover-from-failed-to-open-the-relay-log/
slug: recover-from-failed-to-open-the-relay-log
title: Recover from "Failed to open the relay log"
wordpress_id: 5531
categories:
- MySQL
---

If you find that after rebooting your MySQL slave it stops replicating with the master and you see the "Failed to open the relay log" error in the logs it is probably caused by MySQL putting it's relay logs in /var/run by default, which gets cleared out on boot.




To fix this, you need to change the location MySQL uses for the logging by adding the following line to the [mysqld] section of /etc/my.cnf




`relay-log = /var/lib/mysql/relay-bin`




Then edit /var/lib/mysql/relay-log.info to point to the first new relay log (leaving the master information the same.





`/var/lib/mysql/relay-bin.000001  
1  
mysql-bin.12345  
123456789`





Then from the mysql prompt start the slave:




`mysql> START SLAVE;`




(Source: [Arjen's Journal](http://arjen-lentz.livejournal.com/115899.html))



