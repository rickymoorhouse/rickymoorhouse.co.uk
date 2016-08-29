---
author: rickymoorhouse
comments: true
date: 2009-03-03 20:19:01+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2009/03/03/sharing-a-printer-from-xp-to-vista/
slug: sharing-a-printer-from-xp-to-vista
title: Sharing a printer from XP to Vista
wordpress_id: 1437
categories:
- Tech
---

After quite a while of not being able to print from our laptop to the shared printer on our XP desktop, I finally got it working last night thanks to my Dad. 




Here's the instructions:




#### Make sure you can see the XP computer from Vista. 

If you can't:






  * make sure the workgroup is the same (as the defaults are different)  

    In Vista, go to Computer, System Properties


  * make sure file and print sharing is allowed through the firewall - in our case we had to reset the firewall rules on our XP machine and re-add the ones we wanted for this to work:

    * Go into Control Panel, Network and Internet Connections, Windows Firewall


    * On the Advanced tab, click Restore Defaults


    * On the Exceptions tab, make sure that File and Print Sharing is ticked






#### Adding the printer:






  * Go to Control Panel, Printers


  * Select "Add a printer" from the bar at the top


  * Select "Local Printer" (yes I know it's strange)
  
![](/ricky/images/blog/printer1.jpg)


  * Select "Add a new port" and choose "Local port" from the list
  
![](/ricky/images/blog/printer2.jpg)


  * Enter path to printer e.g. \computerprinter  
![](/ricky/images/blog/printer3.jpg)  

(you can find the printer name from Printers in Windows XP - right click on the printer and choose sharing)  


<!--


[![](/ricky/images/blog/printer1.png)](/ricky/images/blog/printer1.jpg)[![](/ricky/images/blog/printer2.png)](/ricky/images/blog/printer2.jpg)[![](/ricky/images/blog/printer3.png)](/ricky/images/blog/printer3.jpg)


-->
