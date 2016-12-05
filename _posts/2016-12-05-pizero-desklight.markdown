---
author: rickymoorhouse
comments: true
date: 2016-12-05 21:01:12+00:00
layout: post
slug: pizero-desklight
title: Pi Zero as a desklight
categories:
- Random
---

When we set up our office earlier in the year I decided on a standing desk which
I put together using the Ikea algot system.  In order to avoid using up desk
space with a light I originally planned on a clip on light but then saw my
Pi Zero and Unicorn pHat and thought they could make a good alternative.

## Hardware

The Raspberry Pi Zero is in a simple case, mounted onto the underside of the
shelf above my working space.  Attached is it's power cable, a PiHut wireless
adapter connected via USB and of course the Unicorn pHat.  The power cable is
routed down the side of the shelf to my PowerCube, which will eventually be
mounted under my work surface but it's sticky pad wasn't strong enough to hold
it on the underside of the desk!

## Software

As I've not yet added any switch for my light, it all has to be controllable
remotely, so I set up an API to set the colour of the light which I initially
controlled via a web browser with urls like:

    http://192.168.0.15:8009/colour/<red>/<green>/<blue>

As you can imagine that got a bit tedious - especially to turn off after I'd
shut down my laptop!  The next step was to add a simpler way to control the
light through my phone so I set up [iControl Web](https://github.com/sebbu/iControl-Web) with buttons to adjust the light settings.  Then when I saw the Home app on iOS 10, I researched ways to get my custom light controllable through that and came across [Homebridge](https://github.com/nfarina/homebridge) which I could point to my API via it's [Better HTTP RGB plugin](homebridge-better-http-rgb), a bit of config and a couple of changes to my API.

All the [code for my API](https://github.com/rickymoorhouse/light-api) is on github and is very much a work in progress!
