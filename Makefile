
# Used to compile the shared library to interface between python and C.

BOOSTPYTHON = -I /usr/include/python3.5/ -lboost_python-py35
SHAREDSET   = -shared -Wl,-soname,example -fPIC
OBJECTFILES = -o example.so
CPPFILES    = example.cpp
COUT        = example
CC          = g++

all: 
	$(CC) $(SHAREDSET) $(OBJECTFILES) $(CPPFILES) $(BOOSTPYTHON)
