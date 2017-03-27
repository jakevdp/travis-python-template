# Travis Python Template

[![build status](http://img.shields.io/travis/jakevdp/travis-python-template/master.svg?style=flat)](https://travis-ci.org/jakevdp/travis-python-template)

Small template for setting up Travis CI with Python. This assumes you are using
``conda`` for installation of dependencies, and ``pytest`` to run your unit tests.


## Steps

1. Sign in to Travis with your GitHub account ([authentication page](https://travis-ci.org/))
   and accept the permissions confirmation (this needs to be done only once).
2. Go to your [Travis profile page](https://travis-ci.org/profile/) and click the
   check-box next to the repository you want to test (you may have to first click
   the "Sync Repositories" button if it is a new repo).
3. Commit a file called ``.travis.yml`` in your repository (note that it must
   start with a "``.``", which marks it as a hidden file). Feel free to copy
   and modify the one from this repository. Pushing this file to master will
   trigger the Travis build.
4. If you wish, add a "build status" icon to your README. The code looks like this,
   (Note that you must, in two places, replace ``username`` with your GitHub
    username, and ``repo`` with the name of your respository)

   ```
   [![build status](
     http://img.shields.io/travis/username/repo/master.svg?style=flat)](
    https://travis-ci.org/username/repo)
   ```
