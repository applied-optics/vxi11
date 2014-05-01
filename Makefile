VERSION=1.10

CFLAGS = -g
LDFLAGS =
INSTALL = install
prefix = /usr/local

.PHONY : all install clean dist distclean

all : vxi11_cmd vxi11_send libvxi11.so.0

vxi11_cmd: vxi11_cmd.o libvxi11.so.0
	$(CC) -o $@ $^ $(LDFLAGS)

vxi11_cmd.o: vxi11_cmd.c vxi11_user.c vxi11.h
	$(CC) $(CFLAGS) -c $< -o $@

vxi11_send: vxi11_send.o libvxi11.so.0
	$(CC) -o $@ $^ $(LDFLAGS)

vxi11_send.o: vxi11_send.c vxi11_user.c vxi11.h
	$(CC) $(CFLAGS) -c $< -o $@

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
	rm -f *.o libvxi11.so.0 vxi11_cmd vxi11_send vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install: all
	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_send $(DESTDIR)$(prefix)/bin/
	$(INSTALL) libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	ln -sf libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/libvxi11.so
	$(INSTALL) vxi11.h vxi11_user.h $(DESTDIR)$(prefix)/include/

dist : distclean
	mkdir vxi11-$(VERSION)
	cp -p vxi11_cmd.c vxi11_send.c vxi11_user.c vxi11_user.h vxi11.x vxi11-$(VERSION)/
	cp -p Makefile CHANGELOG.txt README.txt GNU_General_Public_License.txt vxi11-$(VERSION)/
	tar -zcf vxi11-$(VERSION).tar.gz vxi11-$(VERSION)

distclean : 
	rm -rf vxi11-$(VERSION)
	rm -f vxi11-$(VERSION).tar.gz
