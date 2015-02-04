title: gr-fcdproplus
author: Volker Schroer
description: Hardware interface to funcube pro+
type: Blocks
repo: https://github.com/dl1ksv/gr-fcdproplus.git

r-fcdproplus is an linux and OSX addon for gnuradio to implement a funcube dongle pro+ source.
On linux it autodetects the correct soundcard from /proc/asound/cards.
This idea was taken from the osmosdr drivers.

To control the device  the hidapi usb version is used.
