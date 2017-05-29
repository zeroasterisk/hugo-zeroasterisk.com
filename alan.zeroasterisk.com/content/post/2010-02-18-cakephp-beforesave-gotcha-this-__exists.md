---
title: 'CakePHP beforeSave() gotcha: need to set $this->__exists to true if setting a primary key'
author: alan
type: post
date: 2010-02-19T02:59:45+00:00
excerpt: |
  if you add a primary key which would turn an "insert" into an "update" within beforeSave() you'll need to set $this->__exists = true;... the call to $this->exists(); happens in model.php before the callback to beforeSave().
url: /2010/02/18/cakephp-beforesave-gotcha-this-__exists/
categories:
  - cakephp
  - development
  - php
tags:
  - beforeSave
  - cake
  - cakephp
  - php

---
I added an update to [CakePHP Book: beforeSave()][1]

> Also, if you add a primary key which would turn an &#8220;insert&#8221; into an &#8220;update&#8221; within beforeSave() you&#8217;ll need to set `$this->__exists = true;`&#8230; the call to [$this->exists();][2] happens in model.php before the callback to [beforeSave()][3].
> 
> <pre>function beforeSave() {
	if (!isset($this-&gt;data[$this-&gt;name]['id']) && isset($this-&gt;data[$this-&gt;name]['unique_field'])) {
		$found = $this-&gt;find("first",array(
				"recursive" =&gt; -1,
				"fields" =&gt; array("id"),
				"conditions" =&gt; array("unique_field" =&gt; $this-&gt;data[$this-&gt;name]['unique_field'])));
		if (!empty($found) && isset($found[$this-&gt;name]['id'])) {
			$this-&gt;id = $this-&gt;data[$this-&gt;name]['id'] = $found[$this-&gt;name]['id'];
			<strong>$this-&gt;__exists = true;</strong>
		}
	}
	return parent::beforeSave();
}</pre>

That&#8217;s been confusing me a bit recently &#8211; setting the ID of a row within beforesave() should change the save to an update, but it was trying to insert with a specified ID and thus, failing&#8230; glad to have a simple solution that makes sense&#8230; hope that helps someone else&#8230;

<div class="twttr_button">
  <a href="http://twitter.com/share?url=https://zeroasterisk.com/2010/02/18/cakephp-beforesave-gotcha-this-__exists/&text=CakePHP+beforeSave%28%29+gotcha%3A+need+to+set+%24this-%3E__exists+to+true+if+setting+a+primary+key" target="_blank" title="Click here if you like this article."> <img src="http://zeroasterisk.com/wp-content/plugins/twitter-plugin/images/twitt.gif" alt="Twitt" /> </a>
</div>

 [1]: http://book.cakephp.org/view/76/Callback-Methods
 [2]: http://api12.cakephp.org/view_source/model/#line-1159
 [3]: http://api12.cakephp.org/view_source/model/#line-1191