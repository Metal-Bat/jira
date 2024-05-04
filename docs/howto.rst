How To - Project Documentation
======================================================================

Get Started
----------------------------------------------------------------------

Documentation can be written as rst files in `jira/docs`.


To build and serve docs, use the commands::

    docker compose -f local.yml up docs



Changes to files in `docs/_source` will be picked up and reloaded automatically.

`Sphinx <https://www.sphinx-doc.org/>`_ is the tool used to build documentation.

Docstring to Documentation
----------------------------------------------------------------------

The sphinx extension `apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html/>`_ is used to automatically document code using signatures and docstring.

Numpy or Google style docstring will be picked up from project files and available for documentation. See the `Napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_ extension for details.

For an in-use example, see the `page source <_sources/users.rst.txt>`_ for :ref:`users`.

To compile all docstring automatically into documentation source files, use the command:
    ::

        make apidocs


This can be done in the docker container:
    ::

        docker run --rm docs make apidocs
