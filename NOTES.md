# Notes

## Container


## busybox

* Error in finding ncurses
change line in check-lxdialog.sh

## initramfs

* Important to generate initramfs from inside of the directory

## C vs. Rust
Rust u8 == C char

## RPI Linux + IIO
```bash
$ make ARCH=arm64 LLVM=1 bcm2711_defconfig
$ make ARCH=arm64 LLVM=1 menuconfig
# > Kernel hacking > Compile-time checks and compiler options > Debug information (Generate DWARF Version 5 debuginfo)
# > Enable loadable module support > Module versioning implementation (gendwarfksyms (from debugging information))
# > General setup > Rust support
# > Kernel hacking > Sample kernel code > Rust samples
# > Device Drivers > Voltage and Current Regulator Support > Onsemi NCV6336 regulator driver
# > Device Drivers > Industrial I/O support > Enable software IIO device support
# > Device Drivers > Industrial I/O support > IIO dummy driver
# > Device Drivers > Industrial I/O support > Rust IIO dummy driver
# > Device Drivers > Industrial I/O support > Light sensors > Rust CM3232 ambient light sensor
# Exit
$ make ARCH=arm64 LLVM=1 -j$(nproc)
$ make ARCH=arm64 LLVM=1 -j$(nproc) rust-analyzer
$ make ARCH=arm64 LLVM=1 -j$(nproc) rustdoc
```
