---
title: hamachi install error on ubuntu – fixed
author: alan
type: post
date: 2008-10-09T15:54:37+00:00
url: /2008/10/09/hamachi-install-error-on-ubuntu-fixed/
categories:
  - geek

---
I recently re-installed ubuntu (linux) on a server and ran into difficulties installing hamachi.&nbsp; As it turned out I tried to setup hamachi without installing the tun module first.&nbsp; I then installed the tun module, but hamachi wouldn&#8217;t work.&nbsp; I eventually figured out that the tuncfg had to be cleaned/make&#8217;ed again, after the tun was re-created.

This is the error I was getting:

> <font face="Courier New">bash: /sbin/tuncfg: No such file or directory</font>

And this fixed it:

> <font face="Courier New">./hamachi-0.9.9.9-20-lnx# cd tuncfg<br />./hamachi-0.9.9.9-20-lnx/tuncfg# sudo make clean<br />rm -f tuncfg<br />./hamachi-0.9.9.9-20-lnx/tuncfg# sudo make<br />cc&nbsp;&nbsp;&nbsp;&nbsp; tuncfg.c&nbsp;&nbsp; -o tuncfg<br />./hamachi-0.9.9.9-20-lnx/tuncfg# cd ..<br />./hamachi-0.9.9.9-20-lnx# sudo make install</p> 
> 
> <p>
>   Copying hamachi into /usr/bin ..<br />Creating hamachi-init symlink ..<br />Compiling tuncfg ..<br />Copying tuncfg into /sbin ..
> </p>
> 
> <p>
>   Hamachi is installed. See README for what to do next.<br />./hamachi-0.9.9.9-20-lnx# sudo tuncfg<br /></font>
> </p></blockquote> 
> 
> <div class="twttr_button">
>   <a href="http://twitter.com/share?url=https://zeroasterisk.com/2008/10/09/hamachi-install-error-on-ubuntu-fixed/&text=hamachi+install+error+on+ubuntu+-+fixed" target="_blank" title="Click here if you like this article."> <img src="http://zeroasterisk.com/wp-content/plugins/twitter-plugin/images/twitt.gif" alt="Twitt" /> </a>
> </div>