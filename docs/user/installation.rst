.. _installation:

Installation
============

To install mysolr from Pypi: ::

  pip install mysolr


From source code: ::

  python setup.py install

Dependencies
------------

requests
++++++++

Mysolr uses requests_ module for sending HTTP requests. So, if you install 
mysolr from source code you have to install_ it.

anyjson
+++++++

.. versionadded:: 0.8.1

Since using eval could be dangerous. We decided to use anyjson_ which tries
to use the fastest json library in your enviroment, using simplejson by default.


Concurrent search
-----------------

Concurrent search feature is only available for python 2.X because it depends
on Gevent and grequests. So if you want to use this feature, you have to install
it as an extra.

::

  pip install "mysolr[async]"


.. _requests: http://python-requests.org
.. _anyjson: https://bitbucket.org/runeh/anyjson
.. _install: http://docs.python-requests.org/en/latest/user/install/