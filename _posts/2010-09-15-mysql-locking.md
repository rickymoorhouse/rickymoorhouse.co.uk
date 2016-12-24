---
author: rickymoorhouse
comments: true
date: 2010-09-15 15:17:56+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/09/15/mysql-locking/
slug: mysql-locking
title: MySQL Locking
wordpress_id: 5992
categories:
- MySQL
---

After experimenting a bit with MySQL locking today, I thought I'd make a note of what I'd discovered:

To create a lock, you need to use:

    
    <code>LOCK TABLES table1 [READ |WRITE], table2 [READ |WRITE]</code>


` `

READ is used to stop other people changing the table while you read from it.
WRITE is used to stop other people reading the table while you write to it.

Once you have issued a `LOCK TABLES` statement, you will not have access to any tables you didn't include.

When you have finished, you can issue the `UNLOCK TABLES` command.

The lock remains until you issue the `UNLOCK TABLES` command, your session ends, you start a transaction or your client is disconnected.

The MySQL locking mechanism is no use if you need to lock something between PHP requests, unless you have a separate process running persistently to maintain the connection to the database.
