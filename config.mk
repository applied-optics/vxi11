CFLAGS=$(OPTS) $(shell pkg-config --cflags libtirpc)
LDFLAGS=

INSTALL=install
MAKE=make

prefix=/usr/local

SOVERSION=1
