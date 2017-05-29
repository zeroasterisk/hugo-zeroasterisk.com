---
title: recreating the RAID array
author: alan
type: post
date: 2007-03-11T05:52:33+00:00
url: /2007/03/11/recreating-the-raid-array/
categories:
  - alan
  - geek

---
So, due to a degraded HDD in my RAID5 array, I decided to build a new array.

I bought 4 320G Seagate drives&#8230; those drives have many benifits, not least of which, a 5 year warranty.

I already have a 3ware escalade RAID controller (7506-4LP), one of the best options for a hardware RAID controller.

Instead of building another RAID5, I chose to build 2, RAID1 arrays. I chose this because it&#8217;s much easier to buy 2 hard drives (upgrading one mirrored pair) than to buy 4 hard drives (to upgrade a 4 disk array). Also the second parity drive is good for data security&#8230; though, of course, if I lost 2 drives on the same array the data would still be lost.

Anyway, so I built 2 RAID1 arrays, and ended up with 2 320G paritions.

I had done some research on filesystems and wanted to move away from ext3 (due to some of the overhead and to take advantage of other filesystems benifits). I had pretty much decided on XFS, have had a previous (mildly) bad experience with ReiserFS&#8230; but while playing with my mkfs options, I noticed the overhead of the various filesystems are quite different&#8230; check out the following comparison, different empty filesystems created on the same disk and mounted:

<pre>/dev/sda1             294G  129M  279G   1% /ext3</pre>

<pre>/dev/sda1             298G  272K  298G   1% /xfs</pre>

<pre>/dev/sda1             299G   33M  299G   1% /reiserfs</pre>

Notice how little of the drive I get from ext3? It&#8217;s slower and I get less of the disk&#8230; yes, it&#8217;s compatible with ext2, but that&#8217;s not enough for me. So, I chose XFS&#8230;. I ended up just using the default mkfs.xfs options as it figured out the proper block size, etc&#8230; I was going to specify a larger log-file size, but the one it calculated was larger than the one I would have specified. I mounted the partitions with the following parameters &#8220;<tt>noatime,nodiratime,logbufs=8</tt>&#8220;.

Transferring the data back&#8230; and all seems good. I love it when things work.

&#8212; researched:

<http://en.wikipedia.org/wiki/XFS>

<http://everything2.com/index.pl?node_id=1479435>

<http://terapix.iap.fr/cplt/oldSite/hard/cluster/raid_config.html>

