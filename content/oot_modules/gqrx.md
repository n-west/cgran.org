---
title: gqrx
type: application
contact :  {author: Alexandre Csete,
            email: bistromath@gmail.com}
website: http://gqrx.dk/
copyright_owner:
    - Alexandre Csete
stable_release: tags/2.3.0
gr_compat: {min: v3.6, max: v3.7.*}
dependencies: 
    - OsmoSDR
    - Qt
brief: >
    Gqrx can operate as a traditional AM/FM/SSB receiver with audio output or as an
    FFT-only instrument.
repo: https://github.com/csete/gqrx.git
---

Gqrx is an experimental software defined radio receiver implemented using GNU
Radio and the Qt GUI toolkit.

The first time you start gqrx it will open a device configuration dialog.
Supported devices that are connected to the computer are discovered
automatically and you can select any of them in the drop-down list.

If you don't see your device listed in the drop-down list it could be because:

* The driver has not included in a binary distribution
* The udev rule has not been properly configured

You can test your device first with rtl_test, qthid, or uhd_usrp_probe that
come with the respective packages.

Gqrx supports multiple configurations and sessions if you have several devices
or if you want to use the same device under different configurations. You can
load a configuration from the GUI or using the -c command line argument. See
"gqrx --help" for a complete list of command line arguments.

Tutorials and howtos are being written and published on the website
http://gqrx.dk/
