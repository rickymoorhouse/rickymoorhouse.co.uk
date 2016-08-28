---
author: rickymoorhouse
comments: true
date: 2008-09-16 10:23:28+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2008/09/16/chop-and-chomp-in-perl/
slug: chop-and-chomp-in-perl
title: Chop and chomp in perl
wordpress_id: 1445
categories:
- Tech
---

Just a reminder, so I remember the difference! - chomp is a safer version of "chop" removes any trailing string that matches what perl thinks is a new line)


`
$string = "abcdef";  
chop($string) # $s is now f, $string is now abcde  
chomp($string) # $string is still now abcde  
  
$string = "abcdefn";  
chomp($string) # $string is now abcdef  
`
