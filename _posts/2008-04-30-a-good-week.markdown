---
author: rickymoorhouse
comments: true
date: 2008-04-30 11:31:04+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2008/04/30/a-good-week/
slug: a-good-week
title: A good week
wordpress_id: 1459
categories:
- Family
- Tech
---

Had a really good week last week, work has been really interesting and challenging recently and last week got the integration between the new security scanning tool and our existing tooling working nicely. The scan results are another thing, but we're still working through those! It's been nice to have a short fairly self contained problem to solve.





My solution consists of a fairly simple REST web service that takes a request formatted with JSON to add the queue to be scanned.  The queue was used as the scans seem to run quicker in batches rather than individually (1 hour for 1 host, or 1 hour 15mins for 4). The web service takes in either an ip address or hostname for the system to be scanned and either an e-mail address and/or a URL to send the output to. Then a set of scheduled tasks look at the queue and submit scans or collect the results and send them on. 





We had a really good time over the weekend too - on Friday night we had dinner with some friends from church .Then on Saturday we went to QE park with Abi (photos below) which was great fun and she loved it, running about between the trees, trying out the trim trail - particularly walking along the wooden beams. 




[  ![](/ricky/images/blog/qepark1.png)  ](/ricky/images/blog/qepark1.jpg)  [  ![](/ricky/images/blog/qepark2.png)  ](/ricky/images/blog/qepark2.jpg)  [  ![](/ricky/images/blog/qepark3.png)  ](/ricky/images/blog/qepark3.jpg)  [  ![](/ricky/images/blog/qepark4.png)  ](/ricky/images/blog/qepark4.jpg)  [  ![](/ricky/images/blog/qepark5.png)  ](/ricky/images/blog/qepark5.jpg)
