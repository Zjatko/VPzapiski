# Vaje 06

Use seccomp and landlock in `protect.c` so the executed `./cat` will not be able to execute other programs and not be able to read files outside it's CWD.


## Build

```
make
```

> Try not to override `./cat` so you all have the same binary unless you need to.


## Usage: `cat`

This prints the contents of a file. If you execute `./cat exploit.txt` you should get a shell.

```
./cat <file>
```


## Usage: `protect`

After you're done with editing `./protect.c` you should no longer be able to open files outside your CWD (i.e. `/etc/passwd`) and execute new programs (i.e. when running the exploit).

```
./protect ./cat cat.c
```
