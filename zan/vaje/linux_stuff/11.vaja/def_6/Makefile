CXX=afl-cc

all: vulnerable

vulnerable: vulnerable.c
	$(CXX) -o $@ $<

fuzz: vulnerable
  AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES=1 \
  AFL_SKIP_CPUFREQ=1 \
  afl-fuzz -i inputs -o outputs -- ./vulnerable @@
