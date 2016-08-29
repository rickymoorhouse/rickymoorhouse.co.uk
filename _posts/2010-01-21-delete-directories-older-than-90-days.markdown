---
author: rickymoorhouse
comments: true
date: 2010-01-21 10:25:16+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/01/21/delete-directories-older-than-90-days/
slug: delete-directories-older-than-90-days
title: Delete directories older than 90 days
wordpress_id: 1394
categories:
- Linux
---

`
find /var/log/hostdb/* -type d -mtime +90 -exec rm -rf {} ;
`



-type d
    only look at directories, f would be files
-mtime +90
    modified time greater than 90 days ago
