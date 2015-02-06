title: gr-fosphor
author: Sylvain Munaut
description: OpenCL/GL accelerated spectrum analyzer. A GPU accelerated spectrum analysis blocks. Works with gr-osmosdr's spectrum analyzer tool
type: Blocks
repo: git://git.osmocom.org/gr-fosphor
save_as: gr-fosphor.html

While the OsmoSDR is still not available, some Osmocom team members (notably Steve Markgraf) have been hacking away on an alternative least-cost solution: rtl-sdr. So what is rtl-sdr? It is a creative form of using consumer-grade DVB-T USB receivers, turning them into fully-fledged software defined radios. Those DVB-T receivers supported by rtl-sdr are based on the Realtek RTL2832U chipset plus a tuner IC like the Elonics E4000

```
function test() {
  console.log("notice the blank line before this function?");
}
```

The RTL2832U has some undocumented commands/registers, by which it can be placed into a mode where it simply forwards the unprocessed raw baseband samples (up to 2.8 MS/s 8-bit I+Q) via high-speed USB into the PC, where they are routed into gnuradio. At a street price of about USD 20 to USD 25, they are undoubtedly the most capable low-cost SDR hardware that can be bought. So now there is really no more excuse for anyone to not learn gnuradio. You don't have to buy a USRP, not even a FCDP or an OsmoSDR: A USD 20 device is all that's needed for receiving signals like GSM, GMR, DECT, TETRA, APCO25 and many others.
