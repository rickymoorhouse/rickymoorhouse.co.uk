---
author: rickymoorhouse
comments: true
date: 2010-10-20 12:19:35+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2010/10/20/recreating-twitter-for-iphones-swipe-to-reveal/
slug: recreating-twitter-for-iphones-swipe-to-reveal
title: Recreating swipe to reveal in HTML, CSS and JS
wordpress_id: 6388
categories:
- Javascript
---

One of the things I really like about the interface in Tweetie / Twitter for iPhone is being able to swipe a tweet to reveal actions beneath it.  This is my attempt to recreate it using HTML, CSS3 and Javascript.  The main swiping action seems to work nicely, but to complete it, I'd like to add a bit more bounciness, a sound effect on swipe (using ?) and have better handling of non-swipe actions.

[View the Demo](http://rickymoorhouse.co.uk/experiments/swipe.html) (only tested on iPhone)

The HTML used in the demo is very simple - just an unordered list. This currently uses jQuery because I already had it in the code I intend to use this with, but it's unnecessary for this part. The javascript adds the div containing the actions and event listeners for touch events. When your finger moves across the screen, if the vertical movement of the swipe is less than 10 pixels the default action is stopped to prevent the view-port moving sideways. If the horizontal movement is greater than 30 pixels, this indicates a swipe to the right, and the "swiped" class is added to the element. There may well be a better way to ensure normal scrolling and link clicking can take place, but this seems to work for now.


## Javascript



    
    <code class="language-javascript">
    var swipeToReveal = {
    init: function() {
    document.addEventListener('touchstart', swipeToReveal.ontouchstart, false);
    document.addEventListener('touchmove', swipeToReveal.ontouchmove, false);
    $(document.body).append('<div id="revealedActions">'+swipeToReveal.actions+'</div>');
    swipeToReveal.bgitems = $('#revealedActions');
    swipeToReveal.bgitems.hide();
    },
    actions: 'Get some actions here',
    startx: 0,
    starty: 0,
    target: null,
    ontouchmove: function(e) {
    var dx = e.touches[0].pageX - swipeToReveal.startx;
    var dy = e.touches[0].pageY - swipeToReveal.starty;
    if ((dy < 10) && (dy > -10)) {
    e.preventDefault();
    if (dx > 30) {
    $(swipeToReveal.target).addClass('swiped');
    }
    }
    },
    ontouchstart: function(e) {
    $('li').removeClass('swiped');
    var target = e.target;
    swipeToReveal.target = target;
    swipeToReveal.bgitems.css({top:target.offsetTop,height: target.offsetHeight});
    swipeToReveal.bgitems.show();
    swipeToReveal.startx = e.touches[0].pageX;
    swipeToReveal.starty = e.touches[0].pageY;
    }
    }
    
    $(document).ready(function() {swipeToReveal.init();});
    </code>



The main effect is produced in CSS using using -webkit-transform and -webkit-transition to slide the list item off the page when it has the class "swiped". Initially I did this by altering the left position of the element but the animation effect was very slow so I've moved to use a 3d translate to take advantage of the iPhone's hardware acceleration. To get the bounce effect I think I could replace the ease-in on the transition with a custom formula. The div that is added by the javascript is shifted into the background with a negative z-index.


## CSS



    
    <code class="language-css">
    li {
    /* positioning and colours removed */
    z-index: 20;
    -webkit-transform: translate3d(0,0,0) rotate(0deg);
    -webkit-transition: -webkit-transform 200ms ease-in;
    }
    li.swiped {
    -webkit-transform: translate3d(100%,0,0) rotate(0deg);
    -webkit-transition: -webkit-transform 200ms ease-in;
    }
    #revealedActions {
    background: #555;color: #fff;
    text-align: center;
    position: absolute;
    width: 100%;
    z-index: -10;
    }</code>



[View the Demo](http://rickymoorhouse.co.uk/experiments/swipe.html) (only tested on iPhone)
