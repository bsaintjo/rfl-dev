#!/bin/sh

(
cd /rfl/obj/initramfs/x86_64-busybox/
find . -print0 | cpio --null -ov --format=newc | gzip -9 >/rfl/obj/initramfs-busybox-x86_64.cpio.gz
)
