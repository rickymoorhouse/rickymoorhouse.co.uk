---
author: rickymoorhouse
comments: true
date: 2009-04-27 12:50:43+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2009/04/27/linux-what-is-using-up-disk-space/
slug: linux-what-is-using-up-disk-space
title: 'Linux: What is using up disk space?'
wordpress_id: 1435
categories:
- Linux
---


`du -m | sort -nr | head`






du -m

    summarises disk usage from current path recursively (in megabytes)

sort -nr
    sorts the output numerically in reverse

head
    restricts output to the top 10 lines




adapted from [Linux Reviews](http://linuxreviews.org/quicktips/chkdirsizes/)

