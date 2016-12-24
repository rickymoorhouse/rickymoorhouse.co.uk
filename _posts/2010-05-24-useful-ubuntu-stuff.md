---
author: rickymoorhouse
comments: true
date: 2010-05-24 13:50:13+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/05/24/useful-ubuntu-stuff/
slug: useful-ubuntu-stuff
title: Useful Ubuntu Stuff
wordpress_id: 1918
categories:
- Ubuntu
tags:
- apt-get
- screenshot
- sharing
---

This post is a dumping ground for useful Ubuntu bits and pieces that aren't worth a full post on their own.


### Useful Packages





	
  * [Lookit](https://launchpad.net/lookit) - captures screenshots and upload them to a specified server, then copies the URL to the clipboard - **ppa:lookit/ppa**

	
  * [Teatime](http://www.rojtberg.net/419/intruducing-teatime/) - simple timer, in a Unity launcher

	
  * [Giver](http://code.google.com/p/giver/) - simple file sharing within the same network - [install](giver)

	
  * [Docky](http://do.davebsd.com/wiki/Docky) - nice dock - [install](docky)
To get the file browser working nicely with the dock, you need to:

	
    1. Edit /usr/share/applications/nautilus-browser as root, changing:
Exec=nautilus to Exec=nautilus --no-desktop --browser .

	
    2. Drag "File Manager" from /usr/share/applications to the dock







### Useful Commands


`dpkg -r <_package>_ `remove a package

`dpkg --purge <_package> _`remove all traces of a package

more at [Linux.com: What to do when apt-get fails](http://www.linux.com/archive/feed/48910)


### Stop the screen from going off when the laptop is shut


Run gconf-editor

Go to  apps-->gnome-power-manager-->buttons ,  set lid_ac and/or lid_battery to "nothing"
