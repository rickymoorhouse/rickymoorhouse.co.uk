---
author: rickymoorhouse
comments: true
date: 2004-04-20 00:00:00+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2004/04/20/more-firefox-search-plugins/
slug: more-firefox-search-plugins
title: More Firefox Search Plugins
wordpress_id: 1623
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



I've wrote a couple more search plugins for Mozilla Firefox - install them using the link below, If you have any problems, [contact me](/ricky/contact/).  
  





  * ![](/ricky/search/a9.gif)[A9 search](addEngine('a9','gif','General')) ([ http://www.a9.com/](http://www.a9.com/))


  * ![](/ricky/search/bibleverse-niv-eng.png)[Lookup verse in the Bible](addEngine('bibleverse-niv-eng','png','Bible'))


