######
ka_com
######

.. start short_desc

**Communication Area**

.. end short_desc

Installation
============
.. start installation

``ka_com`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: shell

	$ python -m pip install ka_com

To install with ``conda``:

.. code-block:: shell

	$ conda install -c conda-forge ka_com

.. end installation

This requires that the ``readme`` extra is installed:

.. code-block:: bash

	$ python -m pip install ka_com[readme]

Configuration
=============

The Configuration of general or tenant specific Package logging is defined in Yaml Configuration Files in the data directory <Package Name>/data of the Package.

.. _configuration-file-label:
.. list-table:: *Configuration Files*
   :widths: auto
   :header-rows: 1

   * - Logging Type
     - Configuration File
     - Description
   * - general
     - log.yml
     - the Python Logger compatible general Configuration file is used to
       define tenant independend logging
   * - tenant
     - log.main.tenant.yml
     - the Python Logger compatible tenant Configuration file is used to
       define tenant dependend logging

Modules
=======
``ka_com`` contains the following modules.

------------
Base Modules
------------

.. _base-modules-label:
.. list-table:: *Base Modules*
   :widths: auto
   :header-rows: 1

   * - Module
     - Description
   * - com.py
     - Communication Class

---------------
Utility Modules
---------------

.. _utility-modules-label:
.. list-table:: *Utility Modules*
   :widths: auto
   :header-rows: 1

   * - Module
     - Description
   * - ioc.py
     - Input/Output Control Class
   * - pacmod.py
     - Package Module Class

---------------
Special Modules
---------------

.. _special-utility-modules-label:
.. list-table:: *Special Utility Modules*
   :widths: auto
   :header-rows: 1

   * - Module
     - Description
   * - __init__.py
     - Init Module
   * - __version__.py
     - Version Module

Appendix
========

.. contents:: **Table of Content**
