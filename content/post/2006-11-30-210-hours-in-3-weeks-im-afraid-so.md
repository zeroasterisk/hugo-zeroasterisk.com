---
title: 210 hours in 3 weeks…. i’m afraid so.
author: alan
type: post
date: 2006-11-30T20:00:42+00:00
url: /2006/11/30/210-hours-in-3-weeks-im-afraid-so/
categories:
  - alan

---
My past 3 weeks&#8230; I&#8217;ve worked ~210 hours&#8230; that averages to 70 hours per week&#8230; but really I worked almost 100 hours in one 7 day period.&nbsp;&nbsp; One day, i worked from 6am &#8211; 2am, and one day I worked from 9am &#8211; 2am.&nbsp; Always getting up and working the next day by 9am at the latest and working more than a full day&#8230; every day.

Why would I do such horrendous work?

Well, we did an upgrade from Livelink 9.2 to Livelink 9.5 and included was a change from proprietary Livelink authentication to AD authentication.&nbsp; This didn&#8217;t work well for us because we have many other companies w/ access to our systems.&nbsp; Domain trusts were established ahead of times, but their AD usernames were formatted differently than our Livelink username format.&nbsp; We have been renaming accounts like mad (in fact, I setup a cool authentication failure logger and some tools to easily change the usernames directly in the KUAF table)&#8230; but it&#8217;s still a bear.&nbsp;&nbsp; On top of this, we use Livelink authentication as the basis for a few downstream systems and those are slow to update (and I can&#8217;t change or control them).&nbsp; And in addition, we have flaky windows servers which are complaining about the increased load (more users, more use, more work-per-page in LL9.5).

All in all &#8211; it&#8217;s an improvement, but the company should have listened to me when I warned it would be aweful.&nbsp; Too bad that&#8217;s the type of thing I know better than to say on a conference call&#8230; true as it may be.&nbsp; If we had known what to rename all users to and did it ahead of time&#8230; we could have been in much better shape.&nbsp; Also I suspect we would have been in better shape if we rebuilt our web servers from scratch instead of doing an upgrade of Livelink on Win 2000.

Bleh!

(yep, you should feel sorry for me.)

I&#8217;m only getting to write this, because the VPN connection to work is down&#8230;&nbsp; aside from that, I avoid this computer as much as possible.

<div class="twttr_button">
  <a href="http://twitter.com/share?url=https://zeroasterisk.com/2006/11/30/210-hours-in-3-weeks-im-afraid-so/&text=210+hours+in+3+weeks....+i%27m+afraid+so." target="_blank" title="Click here if you like this article."> <img src="http://zeroasterisk.com/wp-content/plugins/twitter-plugin/images/twitt.gif" alt="Twitt" /> </a>
</div>