---
author: rickymoorhouse
comments: true
date: 2011-10-05 12:02:31+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2011/10/05/firewall-rules-for-synergy-in-iptables/
slug: firewall-rules-for-synergy-in-iptables
title: Firewall rules for Synergy in iptables
wordpress_id: 7318
categories:
- Tech
---

For a while I've been turning off iptables to let my secondary machine connect as [synergy](http://synergy2.sourceforge.net) client to let me use one keyboard and mouse across both machines.  Finally today I decided to set up the rules properly to do it, so here's how:

Create a new rule file in the iptables chain directory for incoming rules:


    
    sudo vi /etc/iptables.d/filter/INPUT/53-custom-synergys.rule







with the following lines in it:


    
    # Allows incoming flows for Synergy.
    -A INPUT -p tcp -m tcp --dport 24800 -j ACCEPT
    -A INPUT -p udp -m udp --dport 24800 -j ACCEPT



Restart iptables for the rules to take effect


    
    sudo /etc/init.d/iptables restart
