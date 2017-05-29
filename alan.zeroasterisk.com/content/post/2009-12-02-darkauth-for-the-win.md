---
title: DarkAuth for the win!
author: alan
type: post
date: 2009-12-02T16:37:33+00:00
url: /2009/12/02/darkauth-for-the-win/
categories:
  - cakephp

---
I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``

Here&#8217;s how to inject admin requirements based on the admin routing path (prefix):

```I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``

Here&#8217;s how to inject admin requirements based on the admin routing path (prefix):

```

And some other useful controller tricks:

````I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``

Here&#8217;s how to inject admin requirements based on the admin routing path (prefix):

```I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`I&#8217;ve been working with CakePHP for a few years now and am very happy with it.  I&#8217;ve been working with the 1.2 version for a few months (since it went stable) and playing with the [Auth][1] and [ACL][2] core components.

I&#8217;ve decided that ACL is too complicated for most setups, and Auth is fine, but not perfect.  So after some research, I switched to the [DarkAuth][3] component, which was much better suited to my needs.

The main reasons I prefer it are:

  * <span style="background-color: #ffffff; ">Role/Group based access out of the box, which is how I ususally provision security anyway</span>
  * <span style="background-color: #ffffff; ">Easy to customize/tweak to suit my needs (more below)</span>
  * <span style="background-color: #ffffff; ">Easy to setup permissions, easy to add to app_controller, without then having to explicitly allow public controllers/actions&#8230; instead I have to explicitly restrict controllers or actions.  Also it&#8217;s easy to check for prefixes and restrict based on that (more below)</span>
  * <span style="background-color: #ffffff; ">Fast</span>

So here are some of my customizations:

I like having some parameters set on the controller for easy access to &#8220;who is logged in&#8221;, so I put this in the bottom of the DarkAuth startup() function:

`

I like using the core security class for password hashing, which can easily be done like so:

``

Here&#8217;s how to inject admin requirements based on the admin routing path (prefix):

```

And some other useful controller tricks:

````


 [1]: http://book.cakephp.org/view/172/Authentication
 [2]: http://book.cakephp.org/view/171/Access-Control-Lists
 [3]: http://bakery.cakephp.org/articles/view/darkauth-v1-3-an-auth-component
