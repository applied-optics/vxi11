include ../config.mk

.PHONY : all install clean dist distclean

all : libvxi11.so.0

libvxi11.so.0 : vxi11_user.o vxi11_clnt.o vxi11_xdr.o
	$(CC) -shared -Wl,-soname,libvxi11.so.0 $^ -o $@

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
	rm -f *.o libvxi11.so.0 vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install: all
	$(INSTALL) libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	ln -sf libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/libvxi11.so
	$(INSTALL) vxi11.h vxi11_user.h $(DESTDIR)$(prefix)/include/

