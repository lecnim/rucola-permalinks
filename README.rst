=================
rucola-permalinks
=================

.. image:: https://travis-ci.org/lecnim/rucola-permalinks.svg
    :target: https://travis-ci.org/lecnim/rucola-permalinks

A Rucola plugin used to create custom permalinks for site pages.

Installation
------------

You can install using ``pip``: ::

    pip install rucola-permalinks

Usage
-----

You can use the plugin without arguments, it changes permalink of each
``html`` file to a pretty one: ``foo.html => foo/index.html``

An example project directory: ::

    src/
        about.html
        contact.html
        index.html
    script.py

Content of ``script.py``:

.. code-block:: python

    from rucola import Rucola
    from rucola_permalinks import Permalinks

    app = Rucola('.')
    app.use(
        Permalinks()
    )
    app.build()

Result of ``build`` directory: ::

    build/
        about/
            index.html
        contact/
            index.html
        index.html


Options
~~~~~~~

style
    TODO:


License
-------

MIT