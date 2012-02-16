Redmine Tree Fix
================

Overview
--------
In Redmine 1.3.1 I encountered a bug in the tree of issues. Sometimes, the
tree is not properly updated, so some subtasks end up not in the place they
should be. This script fixes the MPTT in the database (lft & rgt markers).

This script was tested on Redmine 1.3.1 stable.

How To Use
----------
As a good practice, you should create virtual Python environment
(for example, in the directory, where you donwloaded the script).

    virtualenv .env --no-site-packages

...then you need sqalchemy:

    .env/bin/pip install sqalchemy

...and proper database driver (i.e. MySQL):

    .env/bin/pip install mysql-python

Now edit the treefix.py file and put your db configuration string in the file.
Then run the script and it will fix the tree.
