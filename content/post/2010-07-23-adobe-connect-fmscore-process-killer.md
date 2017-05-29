---
title: 'Adobe Connect Issue and Fix: Lingering FMSCore.exe processes'
author: alan
type: post
date: 2010-07-23T17:54:50+00:00
url: /2010/07/23/adobe-connect-fmscore-process-killer/
categories:
  - Adobe Connect

---
We&#8217;ve setup Connect to expire the FMSCore processes after 2 hours, but if someone is still connected to a recording, it will keep the old zombie FMSCore process until that person disconnects.

It often happens that doesn&#8217;t work &#8211; and there&#8217;s seemingly no garbage collection in place to clean up old FMSCore.

So we created a simple AutoIt script which can be compiled to an EXE which works, but it has some dependancies&#8230;

The following dependencies / commands must all be in place:

  * c:\Windows\system32\[pv.exe][1]
  * c:\Windows\system32\[pslist.exe][2]
  * c:\Windows\system32\[pskill.exe][3]

How it works

  * the script uses pv.exe to find all FMS Core processes which have a command line argument that includes &#8220;flvplayerapp&#8221; (which is only for recorded courses)
  * for each of the returned process ids
  * it uses pslist to list details which include the age of the process
  * it uses a regex match find the &#8220;hours it&#8217;s been running&#8221;
  * if longer than 5 hours (a configurable parameter) it uses pskill to kill the process.

So we set this up on an hourly scheduled task and it handles garbage collection for us.

Source:  [fmscore-killer-source.au3][4]

<div class="twttr_button">
  <a href="http://twitter.com/share?url=https://zeroasterisk.com/2010/07/23/adobe-connect-fmscore-process-killer/&text=Adobe+Connect+Issue+and+Fix%3A+Lingering+FMSCore.exe+processes" target="_blank" title="Click here if you like this article."> <img src="http://zeroasterisk.com/wp-content/plugins/twitter-plugin/images/twitt.gif" alt="Twitt" /> </a>
</div>

 [1]: http://www.teamcti.com/pview/prcview.htm
 [2]: http://technet.microsoft.com/en-us/sysinternals/bb896682.aspx
 [3]: http://technet.microsoft.com/en-us/sysinternals/bb896683.aspx
 [4]: https://zeroasterisk.com/wp-content/uploads/2010/07/fmscore-killer-source.au3_.txt