# 7. running on real hardware

Status: geohot stuff not sure I'm gonna do

- [ ]  Talking to an FPGA(C, 200) -- A little code for the USB MCU to bitbang JTAG.
- [ ]  Building an FPGA board -- Board design, FPGA BGA reflow, FPGA flash, a 50mhz clock, a USB JTAG port and flasher(no special hardware, a little cypress usb mcu to do jtag), a few leds, a reset button, a serial port(USB-FTDI) also powering via USB, an sd card, expansion connector(ide cable?), and an ethernet port. Optional, expansion board, host USB port, NTSC TV out, an ISA port, and PS/2 connector on the board to taunt you. We provide a toaster oven and a multimeter thermometer to do reflow.
- [ ]  Bringup -- Compiling and downloading the Verilog for the board