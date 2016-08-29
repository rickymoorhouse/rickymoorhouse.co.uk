---
author: rickymoorhouse
comments: true
date: 2009-09-15 12:14:20+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2009/09/15/google-calendar-to-twitter/
slug: google-calendar-to-twitter
title: Google Calendar to Twitter
wordpress_id: 1419
categories:
- Tech
---

![](http://samespirit.net/ricky/images/2009/gcal2twitter.png)




For our [Momentum men's events](http://samespirit.net/momentum/) we have a [Google Calendar](http://calendar.google.com) that we use to manage the upcoming events, and this gets pulled into our website using the Wordpress plugin ICSCalendar. Recently I set up a [twitter account ](http://twitter.com/momentummen) as well, and decided that it would be useful to provide reminders of events on there, which people could then follow and receive SMS updates for.




Initially I had a look around to see what I could find, and came across [Calendar Tweet](http://calendartweet.com), but that didn't do quite what I was looking for. Then I remembered [smtp2web.com](http://smtp2web.com), which you can send e-mails to and it will post them to your website over http. So I set up our gmail account to forward the event reminders to my smtp2web e-mail address and built a PHP script to receive the content, parse it and send a nicely formatted message to twitter.




So I can now set up e-mail reminders for the events in Google Calendar:
![](http://samespirit.net/ricky/images/2009/gcal-reminder.png)  

and they will automatically get posted on twitter at the right time:  

![](http://samespirit.net/ricky/images/2009/gcal-twitter.png)





**Update:** The PHP Code used is available at [http://gist.github.com/280986/](http://gist.github.com/280986/)
