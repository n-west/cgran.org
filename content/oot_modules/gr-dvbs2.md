---
title: gr-dvbs2
brief: A DVB-S2 and DVB-S2X transmitter for GNU Radio
author:
  - Ron Economos <w6rz@comcast.net>
copyright_owner:
  - Ron Economos
dependencies:
  - gnuradio (>= 3.7)
repo: https://github.com/drmpeg/gr-dvbs2.git
stable_release: HEAD
tags:
  - mpeg
  - video
  - receiver
  - blocks
website: https://github.com/drmpeg/gr-dvbs2
---

The goal of this project is to build a software-defined DVB-S2
transmitter, based on the EN 302 307 V1.3.1 Second Generation
framing structure, channel coding and modulation systems for
Broadcasting, Interactive Services, New Gathering and other
broadband satellite applications standard:

http://www.etsi.org/deliver/etsi_en/302300_302399/302307/01.03.01_60/en_302307v010301p.pdf

The baseband framing, baseband scrambling, LDPC (low density
parity check), BCH (Bose, Chaudhuri, Hocquenghem), bit interleaver
and physical layer framing and scrambling blocks are from G4GUO's
DATV-Express Digital Amateur Television project datvexpress_gui
(https://github.com/G4GUO/datvexpress_gui/tree/master/DVB-S2)
and converted to GnuRadio 3.7.x.
