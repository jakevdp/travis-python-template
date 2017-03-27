# Travis Python Template

[![build status](http://img.shields.io/travis/jakevdp/travis-python-template/master.svg?style=flat)](https://travis-ci.org/jakevdp/travis-python-template)

This package provides a basic template for setting up Travis CI with Python.
It assumes you are using ``conda`` for installation of dependencies, and
``pytest`` to run your unit tests.

## Setting Up Travis

1. Sign in to Travis with your GitHub account ([authentication page](https://travis-ci.org/auth))
   and accept the permissions confirmation (this needs to be done only once).
2. Go to your [Travis profile page](https://travis-ci.org/profile/) and click the
   check-box next to the repository you want to test (you may have to first click
   the "Sync Repositories" button if it is a new repo).
3. Commit a file called ``.travis.yml`` in your repository (note that it must
   start with a "``.``", which marks it as a hidden file). Feel free to copy
   and modify the [one from this repository](.travis.yml).
   Pushing this file to master will trigger a new travis build. If the file is
   already in the repository, a push to master or the opening of a pull request
   will trigger a new build.
4. If you wish, add a "build status" icon to your README. The code looks like this,
   (Note that you must, in two places, replace ``username`` with your GitHub
    username, and ``repo`` with the name of your respository)
   ```
   [![build status](
     http://img.shields.io/travis/username/repo/master.svg?style=flat)](
    https://travis-ci.org/username/repo)
   ```

More detailed info is available from Travis itself; see the
[getting started](https://travis-ci.org/getting_started) page.
For a template with some more advanced info (including coverage, automatic
deployment, etc.) check out the [shablona project](http://github.com/uwescience/shablona).
