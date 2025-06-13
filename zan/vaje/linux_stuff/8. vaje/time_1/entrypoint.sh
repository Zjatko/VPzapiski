#!/bin/sh

set -e

./server /tmp/socket &
socat -T 30 \
  TCP-LISTEN:1337,nodelay,reuseaddr,fork \
  UNIX-CONNECT:/tmp/socket
