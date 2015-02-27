---
title: gr-radar
type: application
contact :  {author: Stefan Wunsch,
            email: stefan.wunsch@student.kit.edu}
website: https://grradar.wordpress.com
copyright_owner: Communications Engineering Lab, KIT
stable_release: master
gr_compat: {min: v3.7, max: v3.7.4}
dependencies: {UHD, Qt, Qwt, python-matplotlib}
description: A radar toolbox from GSoC '14
---

The basic flowgraph for many radar applications is shown below. First a signal
is generated and send and received with some hardware. TX and RX signal are
compared with an estimator and the result is displayed on the screen.

The toolbox uses tagged streams for packaging data and to make sure that
corresponding data is processed together in one work function call. In most
cases streams are used up to the evaluation of the signal attributes which are
used for calculating range, velocity or azimuth. This attributes are most often
peaks of a FFT spectrum. After this point there is no use for tagged streams
and it is practical to switch to the message system of GNU Radio. This data is
packed as PMTs (polymorphic types). Read the subsection 'Message structure and
identifiers' for more information.

The send and receive part of the flowgraph is implemented in two ways. First
you can use the USRP Echotimer. This block takes a tagged stream and ensure
that this package is send and received synchronously. Further information in
the section 'USRP Echotimer'. If you want to test your flowgraphs without the
need of hardware you can use a simulator for the propagation effects. A
simulator for static targets with constant attributes like range and velocity
is implemented. It is possible to emulate a moving target if you use sliders
for variables in GNU Radio Companion. The static target simulators has
implemented a callback that updates the targets attributes in runtime.
