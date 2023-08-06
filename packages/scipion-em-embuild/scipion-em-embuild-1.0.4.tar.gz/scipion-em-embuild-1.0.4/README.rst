=================
EMBuild plugin
=================

EMBuild: Model building of protein complexes from intermediate-resolution cryo-EM maps with deep learning-guided automatic assembly.

**Installing the plugin**
=========================

In order to install the plugin follow these instructions:

**Install the plugin**

.. code-block::

     scipion installp -p scipion-em-embuild

or through the **plugin manager** by launching Scipion and following **Configuration** >> **Plugins**


**To install in development mode**

- Clone or download the plugin repository

.. code-block::

          git clone https://github.com/scipion-em/scipion-em-embuild.git

- Install the plugin in developer mode.

.. code-block::

  scipion installp -p local/path/to/scipion-em-embuild --devel

===============
Buildbot status
===============

Status devel version:

.. image:: http://scipion-test.cnb.csic.es:9980/badges/embuild_devel.svg

Status production version:

.. image:: http://scipion-test.cnb.csic.es:9980/badges/embuild_prod.svg

