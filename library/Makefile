include ../config.mk

.PHONY : all install clean dist distclean

UNAME:=$(shell uname -s)

ifneq ($(UNAME),SunOS)
	LDFLAGS:=$(LDFLAGS) -Wl,--version-script=linker.version
endif

all : libvxi11.so.${SOVERSION}

libvxi11.so.${SOVERSION} : vxi11_user.o vxi11_clnt.o vxi11_xdr.o
	$(CC) $(LDFLAGS) -shared -Wl,-soname,libvxi11.so.${SOVERSION} $^ -o $@

vxi11_user.o: vxi11_user.c vxi11.h
	$(CC) -fPIC $(CFLAGS) -c $< -o $@

vxi11_clnt.o : vxi11_clnt.c
	$(CC) -fPIC $(CFLAGS) -c $< -o $@

vxi11_xdr.o : vxi11_xdr.c
	$(CC) -fPIC $(CFLAGS) -c $< -o $@

vxi11.h vxi11_clnt.c vxi11_xdr.c : vxi11.x
	rpcgen -M vxi11.x

TAGS: $(wildcard *.c) $(wildcard *.h) $(wildcard *.c)
	etags $^

clean:
	rm -f *.o libvxi11.so.${SOVERSION} vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install: all
	$(INSTALL) -d $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	$(INSTALL) libvxi11.so.${SOVERSION} $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	ln -sf libvxi11.so.${SOVERSION} $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/libvxi11.so
	$(INSTALL) -d $(DESTDIR)$(prefix)/include/
	$(INSTALL) vxi11_user.h $(DESTDIR)$(prefix)/include/

