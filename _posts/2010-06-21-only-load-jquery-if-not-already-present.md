---
author: rickymoorhouse
comments: true
date: 2010-06-21 14:01:59+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/06/21/only-load-jquery-if-not-already-present/
slug: only-load-jquery-if-not-already-present
title: Only load jQuery if not already present
wordpress_id: 2262
categories:
- Javascript
---

Very useful method of ensuring jQuery is loaded before running the code that needs it - from [How to build a web widget (using jQuery) - Alex Marandon](http://alexmarandon.com/articles/web_widget_jquery/)


[js]
/******** Load jQuery if not present *********/
if (typeof jQuery === "undefined" || jQuery.fn.jquery !== '1.4.2') {
    var script_tag = document.createElement('script');
    script_tag.setAttribute("type","text/javascript");
    script_tag.setAttribute("src",
      "http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js")
    script_tag.onload = main; // Run main() once jQuery has loaded
    script_tag.onreadystatechange = function () { // Same thing but for IE
      if (this.readyState == 'complete' || this.readyState == 'loaded') main();
    }
    document.getElementsByTagName("head")[0].appendChild(script_tag);
} else {
    main();
}
[/js]
