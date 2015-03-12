---
brief: GNU Radio block for Digital Speech Decoder
author:
  - Clayton Smith <argilo@gmail.com>
copyright_owner:
  - Clayton Smith
dependencies:
  - libsndfile
  - gnuradio (>= 3.7)
repo: https://github.com/argilo/gr-dsd.git
stable_release: HEAD
title: gr-dsd
tags:
  - speech
  - encoder
  - blocks
website: https://github.com/argilo/gr-dsd
---

The block expects 48000 samples per second input, and outputs sound at
8000 samples per second.  The input should be FM-demodulated (for
example, with GNU Radio's Quadrature Demod block) and should be between
-1 and 1 while receiving digital signals.  (A quadrature demod gain of
1.6 works well for me for EDACS Provoice.)  The input signal should
also be free of DC bias, so make sure you are tuned accurately, or
filter out DC.

To save CPU cycles, the block detects when the input is zero and avoids
sending it through DSD.  Thus it helps to put a squelch block before
gr-dsd, especially if you're using many copies of gr-dsd in parallel.

The underlying DSD and mbelib were taken from:

    https://github.com/szechyjs/dsd
    https://github.com/szechyjs/mbelib

No modifications to mbelib were required, but DSD has been modified to
bypass the sound card.  The GNU Radio block itself was adapted from the
gr-howto-write-a-block sample included with GNU Radio.
