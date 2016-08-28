---
author: rickymoorhouse
comments: true
date: 2010-10-11 11:25:40+00:00
layout: page
link: http://blog.rickymoorhouse.co.uk/vimrc/
slug: vimrc
title: .vimrc
wordpress_id: 6355
---

[code]
" Turn on syntax highlighting
syntax enable

"Set the colour scheme to mustang http://hcalves.deviantart.com/art/Mustang-Vim-Colorscheme-98974484
set t_Co=256
colorscheme mustang

if has("gui_running")   " If I'm using gVim (very rare these days) 
  " Turn off toolbar
  set guioptions-=T
  " Set font
  set gfn=Inconsolata 10 " really should change this to be different on Linux 
endif



"enable filetype detection
filetype on

" Be case insensitive...
set ignorecase

" ...unless I include caps in my search
set smartcase

" Always display X lines above and below the cursor
set scrolloff=7

"set expandtab
set tabstop=2
set shiftwidth=2

" Only do this part when compiled with support for autocommands.
if has("autocmd")
" Set the title to include the hostname and filename
autocmd BufEnter * let &amp;titlestring = hostname() . " - " . expand("%:t") . ""

" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid or when inside an event handler
" (happens when dropping a file on gvim).
autocmd BufReadPost *
 if line("'"") &gt; 0 &amp;&amp; line("'"") &lt;= line("$") |
   exe "normal g`"" |
 endif

endif " has("autocmd")

" tab navigation like firefox
:nmap &lt;C-S-tab&gt; :tabprevious&lt;cr&gt;
:nmap &lt;C-tab&gt; :tabnext&lt;cr&gt;
:map &lt;C-S-tab&gt; :tabprevious&lt;cr&gt;
:map &lt;C-tab&gt; :tabnext&lt;cr&gt;
:imap &lt;C-S-tab&gt; &lt;ESC&gt;:tabprevious&lt;cr&gt;i
:imap &lt;C-tab&gt; &lt;ESC&gt;:tabnext&lt;cr&gt;i
[/code]
