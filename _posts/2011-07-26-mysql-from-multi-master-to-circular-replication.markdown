---
author: rickymoorhouse
comments: true
date: 2011-07-26 12:32:52+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2011/07/26/mysql-from-multi-master-to-circular-replication/
slug: mysql-from-multi-master-to-circular-replication
title: 'MySQL: From multi-master to circular replication'
wordpress_id: 7280
categories:
- MySQL
---


	
  * Disable anything that will write to the database

	
  * Update the my.cnf files for all servers to support circular replication, by adding log-slave-updates and ensuring you have unique server ids and the auto increment values are suitable. Then restart mysql to pick up the config changes.

	
  * Ensure your existing replication is up-to-date using:
`SHOW SLAVE STATUS`

	
  * Stop replication on both existing servers using
`STOP SLAVE`

	
  * Create a backup of the database from the server that will be just before your new server in the circle using:
`mysqldump --master-data=1 -a -c -Q {db} >  {filename} `

	
  * Add the userids for replication to your new server.

	
  * Transfer the backup to your new server and import it.  

	
  * Change the master config on the new server to point to the server before it in the circle, using the values from the database backup (head -30 {filename} should get you them) and start the slave using:
`STOP SLAVE;
CHANGE MASTER TO MASTER_LOG_FILE='mysql-bin.00001', MASTER_LOG_POS=764,MASTER_HOST='{hostname}';
START SLAVE;`

	
  * Update the master config on the next server in the circle to point to your new server using the command above, taking the values for the log file and position from your new server using:
`SHOW MASTER STATUS`


