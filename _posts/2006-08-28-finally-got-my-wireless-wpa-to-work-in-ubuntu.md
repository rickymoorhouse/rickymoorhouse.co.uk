---
author: rickymoorhouse
comments: true
date: 2006-08-28 18:27:43+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2006/08/28/finally-got-my-wireless-wpa-to-work-in-ubuntu/
slug: finally-got-my-wireless-wpa-to-work-in-ubuntu
title: Finally got my wireless (WPA) to work in Ubuntu
wordpress_id: 1561
---

Last weekend I finally got my laptop to talk to my wireless network in Ubuntu, I'd tried following some instructions before when I had Ubuntu 5.10 (Breezy) on the laptop, but never got anywhere with it. I know I could have changed my network to use WEP instead, but I didn't want to have to change too much just to get my laptop to work occasionaly when I booted into Linux.





With Ubuntu 6.06 (Dapper) it wasn't as straight forward as I'd have liked, but it was much simpler than the method I'd attempted initially. I found the instructions at [fredericiana](http://en.magenson.de/2006/06/11/ubuntu-dapper-drake-and-wpa-encrypted-wireless/).
It was simply a case of doing an 
    
    sudo apt-get update

to update the package library, followed by 
    
    sudo apt-get install gnome-network-manager

and finally commenting out the all but lo from /etc/network/interfaces and rebooting.





When the laptop rebooted I was supposed to be able to go to the new icon in the tray and select the wireless network, however as it was a little more complicated as we hide the SSID on our network and it seems that the SSID was treated as case-sensitive, which I don't think was the case on windows.
