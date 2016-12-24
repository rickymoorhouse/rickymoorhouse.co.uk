---
author: rickymoorhouse
comments: false
date: 2013-01-11 20:54:54+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2013/01/11/measure-sunlight-with-raspberry-pi/
slug: measure-sunlight-with-raspberry-pi
title: Measure sunlight with Raspberry Pi
wordpress_id: 7517
categories:
- Raspberry Pi
---

For Christmas the girls gave me a Raspberry Pi, and for my first project I decided to try recording how bright the sunlight at our window is using an old Webcam.
[![raspberrypi](http://rickymoorhouse.files.wordpress.com/2013/01/raspberrypi.jpg?w=420&h=262)](http://rickymoorhouse.files.wordpress.com/2013/01/raspberrypi.jpg)
The basic idea is:



	
  1.  Capture a photo

	
  2. Analyse the brightness of the photo

	
  3. Log it (and eventually publish to cosm)


So first of all getting the webcam set up - My webcam is a Logitech Quickcam Express, which proved to work nicely with the Raspberry Pi, after plugging it in, it showed up straight away in the output to lsusb:
`
ricky@pi ~ $ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp.
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp.
Bus 001 Device 004: ID 046d:0840 Logitech, Inc. QuickCam Express
`

To get the photo from the webcam I used fswebcam which was simple to install (sudo apt-get install fswebcam) and use:
`
fswebcam --no-banner -d /dev/video0 webcam.jpg
`
The no-banner removes the default date and time at the bottom of the image, /dev/video0 is where the webcam appeared and webcam.jpg is the file to save the image to.

I found a python function to calculate the brightness of the image from [StackExchange](http://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python) so put it all together and here is the python script I'm using:

    
    <code class="language-python">
    #!/usr/bin/python
    import Image
    import ImageStat
    import math
    import os
    import datetime
    os.system("fswebcam --no-banner --scale 50x50 -d /dev/video0 webcam.jpg")
    im = Image.open("webcam.jpg")
    stat = ImageStat.Stat(im)
    r,g,b = stat.mean
    brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    dt = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    data = '%s,%sn' % (dt, brightness)
    open("brightness.csv", 'a').write(data)
    </code>


It could be tidied up quite a bit and I'm sure there's a way to capture the image within Python without having to write it to disk first as well. My first days readings taken every 10 minutes look something like this:
// 
