Project Haystack
----------------
To be defined

Installation
------------

Download the project from Pypi:

.. code-block:: bash

    $ pip install proj-haystack

Quick start
-----------

The below example shows how to obtain an auth token from a Haystack server. 

.. code-block:: python

    from proj_haystack.scram import get_auth_token

    # define these settings specific for your use case
    host_url = "http://localhost:8080"
    username = "su"
    password = "su"

    # get the auth token
    auth_token = get_auth_token(host_url, username, password)
    print(f"Here is the auth token: {auth_token}")

License
-------
To be defined