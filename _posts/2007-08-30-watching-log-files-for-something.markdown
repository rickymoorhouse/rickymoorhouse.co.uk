---
author: rickymoorhouse
comments: true
date: 2007-08-30 23:00:00+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2007/08/31/watching-log-files-for-something/
slug: watching-log-files-for-something
title: Watching log files for something
wordpress_id: 1483
categories:
- Linux
---


Found from: [techblog](http://blog.nominet.org.uk/tech/2005/05/26/tail-f-with-highlighting/):



`
tail -f /var/log/apache2/access_log | sed "s/rss/Ctrl+vCtrl+[[41;1mrssCtrl+vCtrl+[[0m/g"
`


This example is looking for people accessing the rss feed so I can see how frequently it gets hit (whilst still seeing what else is going on).  With this I spotted that one of the Firefox extensions I was using([piclens](http://piclens.com)) was automatically downloading the detected rss feed with every page access. It's a nice extension and I can see why it does that, but I don't want to be accessing rss feeds automatically and potentially multiple times as I use sites.
