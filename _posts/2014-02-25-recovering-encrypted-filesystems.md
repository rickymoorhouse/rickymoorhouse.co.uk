---
author: rickymoorhouse
comments: false
date: 2014-02-25 10:25:55+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2014/02/25/recovering-encrypted-filesystems/
slug: recovering-encrypted-filesystems
title: Recovering encrypted filesystems
wordpress_id: 8164
---


	
  1. Boot from Live CD / USB

	
  2. Decrypt the filesystem

    
    <code class="markdown">cryptsetup luksOpen /dev/sda5 <span class="emphasis">*hostname*</span>
    </code>




	
  3. Mount filesystems

    
    <code class="sql">mount /dev/dm-2 /mnt
    mount /dev/dm-3 /mnt/home
    mount /dev/sda1 /mnt/boot
    mount <span class="comment">--bind /dev /mnt/dev</span>
    mount <span class="comment">--bind /sys /mnt/sys</span>
    mount <span class="comment">--bind /proc /mnt/proc</span>
    </code>




	
  4. Enter chroot
chroot /mnt


`/etc/crypttab` should have: sda5_crypt UUID=*sda5_uuid*
