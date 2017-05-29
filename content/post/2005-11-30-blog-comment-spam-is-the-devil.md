---
title: blog comment spam is the devil
author: alan
type: post
date: 2005-12-01T03:26:15+00:00
url: /2005/11/30/blog-comment-spam-is-the-devil/
categories:
  - geek

---
Anyone else getting a flood of blog comment spam recently?

WordPress is awesome enough to catch all of it as probably spam and put it into a moderation queue for me, but I still had 80+ comments to delete in the past week&#8230; and I have to be careful not to delete a non-spam comment&#8230; not a good situation.

So I looked into plug-ins for WordPress and found a few, but the one I liked the most is called [bad behavior][1]. It&#8217;s built as a very modular component, to be shared into many php applications (which is good for me). Also, I like that it looks at the HTTP headers and can block all bot access (which is really hot). 

I have just set it up and have yet to determine if it&#8217;s effective or if it&#8217;s killing too much access (false positives), but from what I can tell &#8211; it&#8217;s going to be great!

**Update:** I have found that a good deal of spam was getting past &#8220;bad behavior&#8221; &#8211; perhaps the bots are geting more advanced&#8230; but I have added the plugin [wp-gatekeeper][2] and it looks like it will work for me.

<div class="twttr_button">
  <a href="http://twitter.com/share?url=https://zeroasterisk.com/2005/11/30/blog-comment-spam-is-the-devil/&text=blog+comment+spam+is+the+devil" target="_blank" title="Click here if you like this article."> <img src="http://zeroasterisk.com/wp-content/plugins/twitter-plugin/images/twitt.gif" alt="Twitt" /> </a>
</div>

 [1]: http://www.ioerror.us/software/bad-behavior/
 [2]: http://www.meyerweb.com/eric/tools/wordpress/wp-gatekeeper.html "gate keeper"