#!/usr/bin/env bash

qemu-system-x86_64 \
	-kernel obj/linux-x86_64/arch/x86_64/boot/bzImage \
	-initrd obj/initramfs-busybox-x86_64.cpio.gz \
	-nographic -append "console=ttyS0" -m 1024 \
	-fsdev local,id=fsdev0,path=/rfl/chardev-rs,security_model=passthrough \
        -device virtio-9p-pci,fsdev=fsdev0,mount_tag=hostshare \
