---
title: 'A CakePHP gotcha for migrating from 1.1 to 1.2+ on Model->create()'
author: alan
type: post
date: 2009-11-30T16:15:28+00:00
excerpt: |
  I noticed that the data for my saves were not populating with the current date/time as they should, when calling the model->create() function, without a parameter, and then the model->save() function.
  
  $this->ModelName->create();
  $data = $this->ModelName->save($dataWithoutCreatedModifiedUpdated);
  $data['ModelName']['created']=="0000-00-00 00:00:00"
url: /2009/11/30/a-cakephp-gotcha-for-migrating-from-1-1-to-1-2-on-model-create/
categories:
  - cakephp

---
I reported this as a [ticket][1], but as it turns out, it&#8217;s a design choice.. but it&#8217;s enough of a gotcha that I thought I should report it.

#### What happened

The $this->ModelName->create() set the defaults for the next save, which is what I would expect. But on my database there&#8217;s a default value set for the &#8216;created&#8217; field (the standard for datetime columns in PHPmyAdmin) as well as the &#8216;modified&#8217; and &#8216;updated&#8217; fields.

So when the $this->ModelName->create() function ran, it populated the &#8216;created&#8217; and &#8216;updated&#8217; and &#8216;modified&#8217; fields based on their default values in MySQL; which is &#8220;0000-00-00 00:00:00&#8243;.

Subsequently, when I ran $this->ModelName->save($dataWithoutCreated); the &#8216;created&#8217; and &#8216;updated&#8217; and &#8216;modified&#8217; fields were not defaulting to the current timestamp when they were not set by the $data passed into save&#8230; since they already had a &#8220;valid&#8221; value.

#### The Solution

Of course you can modify your model with a beforeSave() code to strip those off, but the &#8220;real&#8221; solution recommended by Mark Story is to change the default value of those fields in the database to NULL. This is something that sounded foreign to me, since PHPMyAdmin defaults to &#8220;0000-00-00&#8243; for date/time fields, but it seems to work fine and I usually will defer to recommendations of the CakePHP core devs (and usually am happy I&#8217;ve done so).


 [1]: http://code.cakephp.org/tickets/view/143
