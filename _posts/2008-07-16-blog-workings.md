---
author: rickymoorhouse
comments: true
date: 2008-07-16 12:55:44+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2008/07/16/blog-workings/
slug: blog-workings
title: Blog workings
wordpress_id: 1449
---

This blog has been through various different iterations mostly based on custom written code- I tried Wordpress for a while, but didn't get on with it - it was too complicated for what I wanted, and I got too much comment spam (mostly filtered out, but still a lot to check it wasn't filtering valid comments).

![How this blog fits together](/ricky/images/blog/blog_workings.png)

A while ago I decided that I wanted to include content that I'd created elsewhere into my blog, so initially attempted this with the timeline approach - however this took the content too far away from the front page. In this latest iteration, all content is included in the main flow of the blog with different rendering styles for different types of content.

The content currently comes from twitter, flickr and from my own post form. These get updated using an ajax call once the front page of the site is loaded to ensure the content is up to date. At the backend, this is written in PHP and stored in a MySQL database, with each type of content having a PHP Class which controls how it is displayed.

**Update:  And I'm back to Wordpress again!**
