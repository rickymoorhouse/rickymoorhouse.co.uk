---
author: rickymoorhouse
comments: true
date: 2004-03-14 00:00:00+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2004/03/14/mozwho-search-plugin/
slug: mozwho-search-plugin
title: MozWho Search Plugin
wordpress_id: 1639
---


function addEngine(name,ext,cat)

  if ((typeof window.sidebar == "object") && (typeof
  window.sidebar.addSearchEngine == "function"))

    //cat="Web";
    //cat=prompt("In what category should this engine be installed?","Web")
    window.sidebar.addSearchEngine(
      "http://www.samespirit.net/ricky/search/"+name+".src",
      "http://www.samespirit.net/ricky/search/"+name+"."+ext,
      name,
      cat );

  else

    errorMsg(name,ext,cat);



I've wrote a quick search plugin to search your Mozilla Firefox bookmarks through [mozWho](http://mozwho.mozdev.org/), install it using the link below, If you have any problems, [contact me](/ricky/contact/).  
  


![](/ricky/search/mozwho.png)[Mozwho search](addEngine('mozwho','png','Bookmarks'))
