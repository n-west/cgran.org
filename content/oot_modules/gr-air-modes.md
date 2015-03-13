---
title: gr-air-modes
brief: A receiver for Mode S transponder signals
author:
  - Nick Foster <bistromath@gmail.com>
copyright_owner:
  - Nick Foster
dependencies:
  - gnuradio (>= 3.6)
  - SQLite
  - Numpy
  - Scipy
  - osmosdr
repo: https://github.com/bistromath/gr-air-modes.git
stable_release: master
tags:
  - application
  - mode-s
  - ads-b
  - standard
  - aerospace
  - receiver
website: https://github.com/bistromath/gr-air-modes
---

gr-air-modes implements a software-defined radio receiver for Mode S
transponder signals, including ADS-B reports from equipped aircraft.

Mode S is the transponder protocol used in modern commercial aircraft.
A Mode S-equipped aircraft replies to radar interrogation by either
ground radar (secondary surveillance) or other aircraft ("Traffic
Collision Avoidance System", or TCAS). The protocol is an extended
version of the Mode A/C protocol used in transponders since the 1940s.
Mode S reports include a unique airframe identifier (referred to
as the "ICAO number") and altitude (to facilitate separation control).
This receiver listens to the 1090MHz downlink channel; interrogation
requests at 1030MHz are not received or decoded by this program.

Automatic Dependent Surveillance-Broadcast (ADS-B) is a communication
protocol using the Extended Squitter capability of the Mode S transport
layer. There are other implementations (VDL Mode 2 and UAT, for
instance) but Mode S remains the primary ADS-B transport for commercial
use. The protocol is:

* Automatic: it requires no pilot input
* Dependent: it is dependent on altimeter, GPS, and other aircraft
  instrumentation for information
* Surveillance: it provides current information about the transmitting
  aircraft
* Broadcast: it is one-way, broadcast to all receivers within range.

ADS-B-equipped aircraft broadcast ("squitter") their position, velocity,
flight number, and other interesting information to any receiver within
range of the aircraft. Position reports are typically generated once per
second and flight indentification every five seconds.
