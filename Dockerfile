FROM fedora:latest AS base

USER root

WORKDIR /home
RUN dnf update -y
RUN dnf install -y gcc-riscv64-linux-gnu qemu-system-riscv64 kernel-devel lld fedpkg ccache rust rust-src bindgen-cli rustfmt clippy tmux

FROM base AS kbuilddep
RUN fedpkg clone -a kernel

FROM base
COPY --from=kbuilddep /home/kernel/kernel.spec /kconfigs/

RUN dnf builddep -y /kconfigs/kernel.spec
