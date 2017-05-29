---
title: SVN Merge, making sure a branch is updated from trunk, then merging back to trunk
author: alan
type: post
date: 2009-03-05T17:49:34+00:00
url: /2009/03/05/svn-merge-making-sure-a-branch-is-updated-from-trunk-then-merging-back-to-trunk/
categories:
  - development
  - geek
  - php

---
So I&#8217;ve just fought a battle w/ SVN merge and thought I&#8217;d post the solution in case others might find it&#8230;

**Scenario**

Our stable code is in trunk svn://svn.domain.tld/repository/trunk

I&#8217;ve got a branch of trunk svn://svn.domain.tld/repository/branches/dev

Changes have been made to my branch and changes have been made to trunk, since I branched.

I&#8217;m ready to merge my branch back into trunk.

**Approach / Overview**

Basically, to be safe, I need to first update my branch with the changes from trunk and resolve any conflicts. Then test my branch and code again (since I will likely have resolved conflicts and thus made changes to my code). Then finally, merge my updated branch into trunk.

**Step 1 &#8211; update/merge branch from trunk**

`# cd /path-to-my-working-copy-of-the-dev-branch<br />
# svn up<br />
# svn log -q --stop-on-copy`

if the last revision listed is something like r999, the branch was created at revision 999&#8230; take note of this number in your case. Anytime you see me use &#8220;999&#8221; you&#8217;ll want to replace it with your own revision number.

`# svn merge --dry-run -r 999:HEAD svn://svn.domain.tld/repository/trunk`

review the results&#8230; conflicts will be prefaced with a C. If you&#8217;ve got a long list, you can send the results of the dry-run to a text file and review the results there

`# svn merge --dry-run -r 999:HEAD svn://svn.domain.tld/repository/trunk > ../merge-results.txt`

after being sure you want to do this, do the merge, updating the branch with changes from trunk

`# svn merge -r 999:HEAD svn://svn.domain.tld/repository/trunk`

SVN tries to automatically merge changed files as best it can. As conflicts are found, it will prompt you, asking you how you want to handle them. If you are sure your version in the branch is correct, you can use &#8220;mf&#8221; (mine full) to resolve this conflict&#8230; if you are sure the trunk version is correct, you can use &#8220;tf&#8221; (theirs full) to resolve this conflict. More often than not, though, the differences will take manual looking at and sometimes manual editing. You can use &#8220;df&#8221; or &#8220;e&#8221; to do so in the console, but I usually use &#8220;p&#8221; to postone conflict resolution, which creates some extra files and breaks the conflicted file till resolved.

You&#8217;ll probably have several conflicts&#8230; that&#8217;s fine, postpone as much as you need to and we will clean them up when done.

When done, lets get a list of conflicts

`# svn st | grep C`

For each of those files, you&#8217;re going to need to fix the conflict. Open them in your favorite editor and look for a line starting with

    `>>>>>>> .merge-right.r###` or something like that&#8230; that&#8217;s where one version starts, at a line starting with

    `=======` is where that version ends and the next starts, and that one goes until the next

    `>>>>>>> .merge-right.r###`.

You can also diff the other file-copies it will create with different suffixes&#8230; Basically, your goal is to FIX the file in question, it doesn&#8217;t matter what you do with the other file-copies with different suffixes, because the next step will remove them automatically.

`# svn resolved ./path-to/file-in-conflict-state.ext`

Keep checking for conflicts, and resolving them manually (this is the tedious part)

`# svn st | grep C`

Once you get all of the conflicts resolved, just to be safe, check out the differences/status of the working copy

`# svn st`

Test your code

If that looks correct and your code passes QA, lets commit the branch&#8230; finalizing our update/merge

`# svn ci -m "MERGED: updated ./branches/dev with the latest from ./trunk"`

**Step 2 &#8211; update/merge trunk from branch**

`# cd /path-to-my-working-copy-of-the-trunk`

`# svn up`

Remember the revision where we created our branch, from step one? Anytime you see me use &#8220;999&#8221; you&#8217;ll want to replace it with your own revision number.

`# svn merge --dry-run -r 999:HEAD svn://svn.domain.tld/repository/branches/dev`

`# svn merge -r 999:HEAD svn://svn.domain.tld/repository/branches/dev`

`# svn st | grep C`

Fix all of your conflicts. Usually, you can use &#8220;tf&#8221; (theirs full) to accept the version from your branch to overwrite the version in your trunk&#8230; since you&#8217;ve just gone through the trouble of resolving conflicts on your branch&#8230; but if you&#8217;re not 100% sure, manually review them as discussed in step 1.

Once you get all of the conflicts resolved, just to be safe, check out the differences/status of the working copy

`# svn st`

Test your code

If that looks correct and your code passes QA, lets commit the trunk&#8230; finalizing our update/merge

`# svn ci -m "MERGED: updated ./trunk with the latest from ./branches/dev"`

That&#8217;s it.

Easy right?

Not quite.

But, I firmly believe the benefits to using SVN far outweigh the headaches. If you&#8217;re sick and tired of complicated merge-processes, you should checkout [GIT][1]&#8230; an alternative to SVN which handles merges and branching and whatnot much much easier and simpler. We are sticking w/ SVN for now because we&#8217;re already committed, but I&#8217;ve heard nothing but good things about GIT.


 [1]: http://git-scm.com/
