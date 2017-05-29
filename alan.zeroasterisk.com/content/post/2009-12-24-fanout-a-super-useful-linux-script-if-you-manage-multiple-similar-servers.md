---
title: fanout, a super useful linux script if you manage multiple, similar servers
author: alan
type: post
date: 2009-12-24T04:54:29+00:00
url: /2009/12/24/fanout-a-super-useful-linux-script-if-you-manage-multiple-similar-servers/
categories:
  - geek
  - linux

---
I love this fanout script for running the same command on multiple servers, just in case you&#8217;re interested:

<http://www.stearns.org/fanout/fanout>

`[root@199564-6 scripts]# fanout "$SERVERS" "cp /root/.ssh/authorized_keys /home/user/.ssh/"<br />
Starting root@db1<br />
Starting root@db2<br />
Starting root@nas<br />
Starting root@www1<br />
Starting root@www2<br />
Starting root@www3<br />
Fanout executing "cp /root/.ssh/authorized_keys /home/user/.ssh/"<br />
Start time Wed Dec 23 23:45:35 EST 2009 , End time Wed Dec 23 23:45:47 EST 2009<br />
==== As root on db1 ====`

`==== As root on db2 ====</p>
<p>==== As root on nas ====</p>
<p>==== As root on www1 ====</p>
<p>==== As root on www2 ====</p>
<p>==== As root on www3 ====</p>
<p>Exiting fanout, cleaning up...done.</p>
<p>[root@199564-6 scripts]# fanout "$SERVERSWWW" "/etc/init.d/httpd restart"<br />
Starting root@www1<br />
Starting root@www2<br />
Starting root@www3<br />
Fanout executing "/etc/init.d/httpd restart"<br />
Start time Wed Dec 23 23:50:52 EST 2009 , End time Wed Dec 23 23:50:59 EST 2009<br />
==== As root on www1 ====<br />
Stopping httpd: [  OK  ]<br />
Starting httpd: [  OK  ]</p>
<p>==== As root on www2 ====<br />
Stopping httpd: [  OK  ]<br />
Starting httpd: [  OK  ]</p>
<p>==== As root on www3 ====<br />
Stopping httpd: [  OK  ]<br />
Starting httpd: [  OK  ]</p>
<p>Exiting fanout, cleaning up...done.</p>
<p>`

`[root@199564-6 scripts]# echo $SERVERS<br />
root@www1 root@www2 root@www3 root@db1 root@db2 root@nas<br />
[root@199564-6 scripts]# echo $SERVERSWWW<br />
root@www1 root@www2 root@www3`

A great way to execute the same commands on multiple servers&#8230; if you export the $SERVERS to a standard list, in your .bashrc or whatnot&#8230; it&#8217;s even easier. Of course, you&#8217;ll probably want to setup authorized_keys for your servers so that you don&#8217;t have to authenticate to each&#8230;

