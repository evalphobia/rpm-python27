# original: 
#   - author nmilford
#   - from https://github.com/nmilford/specfiles/blob/master/python-2.7/python27-setuptools-0.6c11.spec

%define name python27-setuptools
%define version 1.1.6
%define unmangled_version 1.1.6
%define release 1

Summary: Download, build, install, upgrade, and uninstall Python packages -- easily!
Name: %{name}
Version: %{version}
Release: %{release}
Source0: setuptools-%{unmangled_version}.tar.gz
License: PSF or ZPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
Vendor: Phillip J. Eby <distutils-sig@python.org>
Requires: python27-devel
Url: http://pypi.python.org/pypi/setuptools
Packager: evalphobia <evalphobia@gmail.com> 
AutoReq: no

%description
===============================
Installing and Using Setuptools
===============================

.. contents:: **Table of Contents**


-------------------------
Installation Instructions
-------------------------

Upgrading from Distribute
=========================

Currently, Distribute disallows installing Setuptools 0.7+ over Distribute.
You must first uninstall any active version of Distribute first (see
`Uninstalling`_).

Upgrading from Setuptools 0.6
=============================

Upgrading from prior versions of Setuptools is supported. Initial reports
good success in this regard.

Windows
=======

The recommended way to install setuptools on Windows is to download
`ez_setup.py`_ and run it. The script will download the appropriate .egg
file and install it for you.

.. _ez_setup.py: https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

For best results, uninstall previous versions FIRST (see `Uninstalling`_).

Once installation is complete, you will find an ``easy_install.exe`` program in
your Python ``Scripts`` subdirectory.  For simple invocation and best results,
add this directory to your ``PATH`` environment variable, if it is not already
present.


Unix-based Systems including Mac OS X
=====================================

Download `ez_setup.py`_ and run it using the target Python version. The script
will download the appropriate version and install it for you::

    > wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python

Note that you will may need to invoke the command with superuser privileges to
install to the system Python.

Alternatively, on Python 2.6 and later, Setuptools may be installed to a
user-local path::

    > wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    > python ez_setup.py --user


Advanced Installation
=====================

For more advanced installation options, such as installing to custom
locations or prefixes, download and extract the source
tarball from `Setuptools on PyPI <https://pypi.python.org/pypi/setuptools>`_
and run setup.py with any supported distutils and Setuptools options.
For example::

    setuptools-x.x$ python setup.py --prefix=/opt/setuptools

Use ``--help`` to get a full options list, but we recommend consulting
the `EasyInstall manual`_ for detailed instructions, especially `the section
on custom installation locations`_.

.. _EasyInstall manual: https://pythonhosted.org/setuptools/EasyInstall
.. _the section on custom installation locations: https://pythonhosted.org/setuptools/EasyInstall#custom-installation-locations


Downloads
=========

All setuptools downloads can be found at `the project's home page in the Python
Package Index`_.  Scroll to the very bottom of the page to find the links.

.. _the project's home page in the Python Package Index: https://pypi.python.org/pypi/setuptools

In addition to the PyPI downloads, the development version of ``setuptools``
is available from the `Bitbucket repo`_, and in-development versions of the
`0.6 branch`_ are available as well.

.. _Bitbucket repo: https://bitbucket.org/pypa/setuptools/get/default.tar.gz#egg=setuptools-dev
.. _0.6 branch: http://svn.python.org/projects/sandbox/branches/setuptools-0.6/#egg=setuptools-dev06

Uninstalling
============

On Windows, if Setuptools was installed using an ``.exe`` or ``.msi``
installer, simply use the uninstall feature of "Add/Remove Programs" in the
Control Panel.

Otherwise, to uninstall Setuptools or Distribute, regardless of the Python
version, delete all ``setuptools*`` and ``distribute*`` files and
directories from your system's ``site-packages`` directory
(and any other ``sys.path`` directories) FIRST.

If you are upgrading or otherwise plan to re-install Setuptools or Distribute,
nothing further needs to be done. If you want to completely remove Setuptools,
you may also want to remove the 'easy_install' and 'easy_install-x.x' scripts
and associated executables installed to the Python scripts directory.

--------------------------------
Using Setuptools and EasyInstall
--------------------------------

Here are some of the available manuals, tutorials, and other resources for
learning about Setuptools, Python Eggs, and EasyInstall:

* `The EasyInstall user's guide and reference manual`_
* `The setuptools Developer's Guide`_
* `The pkg_resources API reference`_
* `Package Compatibility Notes`_ (user-maintained)
* `The Internal Structure of Python Eggs`_

Questions, comments, and bug reports should be directed to the `distutils-sig
mailing list`_.  If you have written (or know of) any tutorials, documentation,
plug-ins, or other resources for setuptools users, please let us know about
them there, so this reference list can be updated.  If you have working,
*tested* patches to correct problems or add features, you may submit them to
the `setuptools bug tracker`_.

.. _setuptools bug tracker: https://bitbucket.org/pypa/setuptools/issues
.. _Package Compatibility Notes: https://pythonhosted.org/setuptools/PackageNotes
.. _The Internal Structure of Python Eggs: https://pythonhosted.org/setuptools/formats.html
.. _The setuptools Developer's Guide: https://pythonhosted.org/setuptools/setuptools.html
.. _The pkg_resources API reference: https://pythonhosted.org/setuptools/pkg_resources.html
.. _The EasyInstall user's guide and reference manual: https://pythonhosted.org/setuptools/easy_install.html
.. _distutils-sig mailing list: http://mail.python.org/pipermail/distutils-sig/


-------
Credits
-------

* The original design for the ``.egg`` format and the ``pkg_resources`` API was
  co-created by Phillip Eby and Bob Ippolito.  Bob also implemented the first
  version of ``pkg_resources``, and supplied the OS X operating system version
  compatibility algorithm.

* Ian Bicking implemented many early "creature comfort" features of
  easy_install, including support for downloading via Sourceforge and
  Subversion repositories.  Ian's comments on the Web-SIG about WSGI
  application deployment also inspired the concept of "entry points" in eggs,
  and he has given talks at PyCon and elsewhere to inform and educate the
  community about eggs and setuptools.

* Jim Fulton contributed time and effort to build automated tests of various
  aspects of ``easy_install``, and supplied the doctests for the command-line
  ``.exe`` wrappers on Windows.

* Phillip J. Eby is the seminal author of setuptools, and
  first proposed the idea of an importable binary distribution format for
  Python application plug-ins.

* Significant parts of the implementation of setuptools were funded by the Open
  Source Applications Foundation, to provide a plug-in infrastructure for the
  Chandler PIM application.  In addition, many OSAF staffers (such as Mike
  "Code Bear" Taylor) contributed their time and stress as guinea pigs for the
  use of eggs and setuptools, even before eggs were "cool".  (Thanks, guys!)

* Since the merge with Distribute, Jason R. Coombs is the
  maintainer of setuptools.  The project is maintained in coordination with
  the Python Packaging Authority (PyPA) and the larger Python community.

.. _files:


%prep
%setup -n setuptools-%{unmangled_version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --single-version-externally-managed --root=$RPM_BUILD_ROOT --prefix=/usr
# --record=INSTALLED_OBJECTS
# Lets not overwrite the default one in CentOS/RHEL
rm -f $RPM_BUILD_ROOT/usr/bin/easy_install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
#-f INSTALLED_OBJECTS
/usr/lib/python2.7/site-packages/easy_install.py
/usr/lib/python2.7/site-packages/easy_install.pyc
/usr/lib/python2.7/site-packages/easy_install.pyo
/usr/lib/python2.7/site-packages/pkg_resources.py
/usr/lib/python2.7/site-packages/pkg_resources.pyc
/usr/lib/python2.7/site-packages/pkg_resources.pyo
/usr/lib/python2.7/site-packages/setuptools/
/usr/lib/python2.7/site-packages/setuptools-1.1.6-py2.7.egg-info/
/usr/lib/python2.7/site-packages/_markerlib/
/usr/bin/easy_install-2.7

%defattr(-,root,root)
%doc CHANGES.txt 'CHANGES (links).txt' CONTRIBUTORS.txt DEVGUIDE.txt README.txt
