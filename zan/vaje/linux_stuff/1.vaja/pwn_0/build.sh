#!/bin/sh

gcc -o main main.c -std=c99 -fno-stack-protector -no-pie
