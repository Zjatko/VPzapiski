# Vaje 07

Fuzz and fix `vulnerable.c` until it has no more crashes.


## Install AFL++

Docker:
```
docker run -ti -v $(pwd):/src aflplusplus/aflplusplus
```

Ubuntu:
```
apt install afl++
```

Arch (AUR):
```
yay -S aflplusplus
```

Source: [https://aflplus.plus/docs/install/](https://aflplus.plus/docs/install/)


## Build and run

Docker:
```
cd /src
make
afl-fuzz -i inputs -o outputs -- ./vulnerable @@
```

Host machine:
```
make fuzz
```

Host without make:
```
export AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1
export AFL_SKIP_CPUFREQ=1
afl-fuzz -i inputs -o outputs -- ./vulnerable @@
```

> Inputs that crashed the program can be found in `./outputs/default/crashes/id*`
