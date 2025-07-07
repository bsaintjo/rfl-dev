#!/bin/sh

docker run --rm -it -v "$(pwd)":/rfl -w /rfl rust-for-linux:latest /bin/bash
