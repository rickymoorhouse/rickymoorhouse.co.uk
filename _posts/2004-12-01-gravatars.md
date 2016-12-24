---
author: rickymoorhouse
comments: true
date: 2004-12-01 21:04:19+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2004/12/01/gravatars/
slug: gravatars
title: Gravatars
wordpress_id: 1595
---

I've now implemented [Gravatars](http://www.gravatars.com) for the comments on this site.  

It was a bit tricky as this is coded using ASP (VBScript) - but I've managed to get it working using the code from [http://www.frez.co.uk/freecode.htm#md5](http://www.frez.co.uk/freecode.htm#md5) - although interestingly the VBScript version wouldn't work, so I have used the javascript version - a bit of a strange way to do it, but it seems to work. I didn't realise before that you could mix languages in ASP, but it turns out you can by including one in the page using the <script runat="server"... tag, and then it can be called from within the other code on the page even if it's in a different programming language!
