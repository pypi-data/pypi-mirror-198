============
Introduction
============

The Netskope module which provides a RESTful API that is
published using Swagger on https://<TENANT>.goskope.com/apidocs/ along with other
Netskope APIs.

This module aims to provide a class hierarchy to simplify access to these
published APIs, performing the 'heavy lifting' whilst providing full access to
to their functionality. This is achieved by providing simple wrappers that enable
you to take the swagger documented object paths, fields and where appropriate 
JSON body from the documentation and pass them to simple get, create, delete and
update methods. These methods simply return a *requests* response object.

Some basic configuration, such a base url and API key are read
from an ini file. An example of which is provided. When instantiating/initialising
this will read config.ini by default. Alternatively a path can be provided.

For more detailed documentation please see: 
https://python-netskope.readthedocs.io/en/latest/

PyPi:
https://pypi.org/project/netskope/

GitHub:
https://github.com/neerdael-nl/python-netskope

All feedback please to jneerdael@netskope.com

Thanks

John Neerdael
