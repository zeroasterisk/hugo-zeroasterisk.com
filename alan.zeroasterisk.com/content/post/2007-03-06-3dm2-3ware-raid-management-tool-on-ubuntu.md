---
title: 3DM2 (3ware raid management tool) on Ubuntu
author: alan
type: post
date: 2007-03-06T17:35:40+00:00
url: /2007/03/06/3dm2-3ware-raid-management-tool-on-ubuntu/
categories:
  - geek

---
Ran into a problem installing the 3DM2 (3ware raid management tool) on Ubuntu today.

Got an &#8220;&#8221; error when trying to run the install script.

After a bit of debugging, I figured out that the failing variable was in the &#8220;check architecture&#8221; section of the script&#8230; In my case, I simply stripped out the logic and put in the following text to just set variables to my specific setup:

<pre class="code console">## Check release.
## Get architecture
set arch = `uname -m`
set arch = "x86"
set supported = "yes"
</pre>

After that it worked fine&#8230; but once installed, the service wouldn&#8217;t start&#8230; due to the following error &#8220;Failed to create SSL context&#8221;.

At this point, I went back to researching and found a .deb package installer for debain (the distro ubuntu is based on). { [pkg][1], [ref][2] }

I got that, installed it, went through the config script did a slight configuration change, and it actually worked this time. I think the problem was the &#8220;3dm2.pem&#8221; file (SSL cert).

<pre class="code console">wget http://ftp.debian-unofficial.org/debian/pool/restricted/3/3ware-3dm2-binary-i386/3ware-3dm2-binary_9.3.0.4-1duo1_i386.debdpkg -i 3ware-3dm2-binary_9.3.0.4-1duo1_i386.deb
</pre>

Note: the default password is &#8220;3ware&#8221;

Much thanks to the following page for getting me going at several stopping points:

[Random Garbage Generator :: Hardware RAID management from the web :: February :: 2007][3]

also here&#8217;s a link to all my [3ware driver files/sources/etc][4] in one place


 [1]: http://ftp.debian-unofficial.org/debian/pool/restricted/3/3ware-3dm2-binary-i386/
 [2]: http://www.debian-unofficial.org/packages.html
 [3]: http://dfhzn.blogsome.com/2007/02/08/hardware-raid-management-from-the-web/
 [4]: http://home.zeroasterisk.com/files/linux/3ware.tar.bz2
