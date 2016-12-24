---
author: rickymoorhouse
comments: true
date: 2009-03-12 13:08:14+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2009/03/12/customising-pocket-ubuntu-for-windows/
slug: customising-pocket-ubuntu-for-windows
title: Customising Pocket Ubuntu for Windows
wordpress_id: 1436
categories:
- Ubuntu
---

I've been playing about with [Portable Ubuntu for Windows](http://portableubuntu.sourceforge.net/), as a replacement for my secondary machine at work, and customised the system a bit for my liking. This is going to be a working post for me to add notes on what I've changed so that I can find it again! Initially I was planning to build my own image based on [Cooperative Linux](http://www.colinux.org/), but decided that as [Portable Ubuntu for Windows](http://portableubuntu.sourceforge.net/) had most things configured it made a better starting point.




#### Moving the notification popups




The default notification position is bottom right, which was appearing below the windows task bar - so I wanted to move them






  * Open up **gconf-editor**


  * Go to apps, notification-daemon


  * Edit popup_location to suit your setup - I'm currently trying top_right


