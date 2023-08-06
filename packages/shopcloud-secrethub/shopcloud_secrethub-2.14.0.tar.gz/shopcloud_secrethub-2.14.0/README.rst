Shopcloud SecretHub CLI
=======================

The SecretHub CLI provides the command-line interface to interact with
the SecretHub API.

install
-------

::

   $ pip install shopcloud_secrethub

Usage
~~~~~

**Reading and writing secrets:**

.. code:: sh

   $ secrethub auth
   $ secrethub read <secret-name>
   $ secrethub write <secret-name> <value>

**Provisioning your applications with secrets:**

Provision a template file

.. code:: sh

   $ secrethub inject -i app.temp.yaml -o app.yaml

   # app.temp.yaml
   env_variables:
     ENV: {{ talk-point/test-repo/env }}
     SECRET_KEY: {{ talk-point/test-repo/secret_key }}

Provision to the environment

.. code:: sh

   $ eval `secrethub printenv -i app.temp.yaml`

   # app.temp.yaml
   env_variables:
     ENV: {{ talk-point/test-repo/env }}
     SECRET_KEY: {{ talk-point/test-repo/secret_key }}

**in Code:**

.. code:: py

   from shopcloud_secrethub import SecretHub
   hub = SecretHub(user_app="test-script", api_token='<TOKEN>')
   hub.read('talk-point/test-repo/secret_key')

Deploy to PyPi
~~~~~~~~~~~~~~

.. code:: sh

   $ rm -rf build dist
   $ pip3 install wheel twine
   $ python3 setup.py sdist bdist_wheel
   $ twine upload dist/*
