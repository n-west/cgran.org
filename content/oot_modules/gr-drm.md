---
brief: DRM transmitter using GNU Radio
author:
  - Felix Wunsch <uncnr[at]student.kit.edu>
copyright_owner:
  - Felix Wunsch
  - Communications Engineering Lab, Karlsruhe Institute of Technology
dependencies:
  - gnuradio (>= 3.7.0)
  - UHD
  - FAAC
  - FAAD2
repo: https://github.com/kit-cel/gr-drm.git
stable_release: HEAD
tags:
  - DRM
  - receiver
  - audio
  - standard
website: https://github.com/kit-cel/gr-drm
title: gr-drm
icon: https://avatars2.githubusercontent.com/u/11016077?v=3&s=200
---

This project features a DRM/DRM+ software transmitter fully integrated into GNU
Radio Companion.

You are also free to play around with several robustness modes (RM) and
spectrum occupancies (SO, signal bandwidth) ranging from 4.5 to 20 kHz. The
corresponding bit rates vary from below 5 kbps to about 55 kbps. A
configuration that is widely used is RM B (==1) and 10 kHz bandwidth (SO 3).
Among other parameters, the station label and a text message can also be set by
simply adapting the correspondant blocks' values.
