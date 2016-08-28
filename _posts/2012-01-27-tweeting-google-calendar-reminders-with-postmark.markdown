---
author: rickymoorhouse
comments: true
date: 2012-01-27 12:41:09+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2012/01/27/tweeting-google-calendar-reminders-with-postmark/
slug: tweeting-google-calendar-reminders-with-postmark
title: Tweeting Google Calendar reminders with Postmark
wordpress_id: 7374
categories:
- Tech
---

A while back I wrote my [original script](http://samespirit.net/ricky/2009/09/15/google-calendar-to-twitter/) to tweet event reminders from Google Calendar and it's been through a couple of iterations since and been broken for a while. Well finally I got round to update it to use OAuth to connect to twitter using the [twitteroauth library](https://github.com/abraham/twitteroauth) and switched to using [Postmark Inbound](http://blog.postmarkapp.com/post/15687406657/introducing-postmark-inbound-easily-parse-replies-other) for handling the incoming e-mail.

What you will need



	
  * Web hosting with php

	
  * A Google calendar attached to a Gmail account

	
  * A [Postmark ](https://postmarkapp.com/)account

	
  * A [Twitter ](http://twitter.com)account

	
  * [My script](https://gist.github.com/280986)




## Getting set up


Register a new twitter app from the [Twitter Developer Site](https://dev.twitter.com/apps/new) (making sure you sign in with the account you want the tweets to come from) - fill out all the necessary fields and click create. On the next page you should get the OAuth details (Consumer key and Consumer secret) and a section to generate your access token and access token secret, these all need putting into the section at the top of the script.

Install the [script](https://gist.github.com/280986) on your web hosting, along with the twitteroauth directory from  [twitteroauth at GitHub](https://github.com/abraham/twitteroauth). If you got to the script URL in a web browser you should see it post a , to your twitter account without any errors. (I need to add some testing code really!)

Set up a server in your [Postmark account](https://postmarkapp.com/servers) then go into the Settings page for that server and update the Inbound Hook to point to the full URL of the script on your server to point to your script for inbound emails. Make a note of the inbound e-mail address from the server tab of your settings as you will need this to forward the calendar reminders to.

Add your Inbound Email address as a forwarding address to your Gmail account. It will send a confirmation code to the address, which you can collect from the Inbound section of the Postmark interface

Create a filter in your gmail account to forward your calendar reminders to the Inbound Email address from your postmark account (Mine forwards anything from calendar.notifier@google.com).

Now everything should be in place to start sending reminders.  For each event in your calendar set up e-mail reminders for the number of days/hours before you want the reminder tweeted.  These should then appear something like this at twitter:


<blockquote><Description> this afternoon at <time>, <Location>

<Description> next Saturday at <time>, <Location></blockquote>
