---
title: Meteor Core Cordova Support – Alpha Release is out
author: alan
type: post
date: 2014-08-25T20:02:49+00:00
url: /2014/08/25/meteor-core-cordova-support-alpha-release-is-out/
categories:
  - development
  - meteorjs

---
We&#8217;ve been watching this for a while, but now the first Alpha release is out for Meteor + Cordova built into the core.

**SWEET!**

Watch the DevShop Presentation on it here: <https://www.youtube.com/watch?v=zzNoXbv1DX4&feature=youtu.be&t=24m>

&nbsp;

And here are instructions to get it going and play with it: <https://meteor.hackpad.com/Getting-Started-With-Cordova-Z5n6zkVB1xq>

&nbsp;

Also, just an [update][1], [MeteorRider][2] is still a strong and simple option for getting Meteor into Cordova (DOM hijacking), but I&#8217;m also checking out another great looking option is [Cordova Loader][3] (builds all Cordova assets into the public folder of Meteor).  Of course there&#8217;s also [Packmeteor][4], which is an early version of what the core Cordova implementation seems to be.

&nbsp;

I&#8217;m the most excited about:

  * Core API is clean (Meteor.isCordova is simple but brilliant) and Cordova.depends() sounds great too
  * Vastly improved local development early on, tying a cordova emulator to the localhost development is very well done
  * Meteor packages which can implement Cordova plugins&#8230; that will be a wildly convenient way to integrate &#8220;vetted&#8221; plugins in a simple manner.

If this is a space you are working in, jump on board the Meteor core implementation as early as you can, log bugs, submit pull requests, and make it official/important.  This will end up being a significant feather in Meteor&#8217;s hat, making Meteor + Mobile a powerful pairing.


 [1]: https://zeroasterisk.com/2013/08/22/meteor-phonegapcordova-roundup-fall-2013/
 [2]: https://github.com/zeroasterisk/MeteorRider
 [3]: https://github.com/andrewreedy/cordova-loader
 [4]: https://github.com/SpaceCapsule/packmeteor
