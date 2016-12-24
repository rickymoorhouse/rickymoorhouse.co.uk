---
author: rickymoorhouse
comments: true
date: 2014-10-18 06:11:17+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2014/10/18/disabling-sslv3/
slug: disabling-sslv3
title: Disabling SSLv3
wordpress_id: 8205
categories:
- Tech
---

With [POODLE](http://googleonlinesecurity.blogspot.co.uk/2014/10/this-poodle-bites-exploiting-ssl-30.html) the time has come to disable SSLv3 everywhere. There will be clients that break and need fixing but it needs doing. You can [read more details and background](https://www.imperialviolet.org/2014/10/14/poodle.html) on the [vulnerability](https://www.openssl.org/~bodo/ssl-poodle.pdf).

Here's a few useful snippets from my experience with it this week:



## Apache



Make sure the combination you have for the SSLProtocol line disables SSLv2 and v3 - something like:
`SSLProtocol All -SSLv2 -SSLv3`



## DataPower



Ensure your crypto profiles have SSLv2 and v3 disabled in the options line:

[code lang=text]
  switch <domain>
  co 
  crypto 
  profile <profile>
  option-string OpenSSL-default+Disable-SSLv2+Disable-SSLv3
  exit 
  exit 
  write mem 
[/code]



## Java



If you have problems with handshakes from Java client process force the protocols to use with 
`-Dhttps.protocols=TLSv1`



## nginx



Make sure the ssl_protocols line in your SSL configuration doesn't have SSLv3 in it.
`ssl_protocols TLSv1 TLSv1.1 TLSv1.2;`



## nodejs



Make sure you don't have secureProtocol:SSLv3_method anywhere in https options - use TLSv1_method instead if it's really needed.



## Websphere



See [Security bulletin](http://www-01.ibm.com/support/docview.wss?uid=swg21687173)
