VERSION=1.08

#CFLAGS = -Wall -g
CFLAGS = -g
INSTALL = install
prefix = /usr/local
CXX = g++

.PHONY : install clean dist distclean

vxi11_cmd: vxi11_cmd.o vxi11_user.o vxi11_clnt.o vxi11_xdr.o
	$(CXX) $(CFLAGS) -o $@ $^

vxi11_cmd.o: vxi11_cmd.cc vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

vxi11_user.o: vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

vxi11.h vxi11_clnt.c vxi11_xdr.c : vxi11.x
	rpcgen -M vxi11.x

TAGS: $(wildcard *.c) $(wildcard *.h) $(wildcard *.cc)
	etags $^

clean:
	rm -f *.o vxi11_cmd vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install: vxi11_cmd
	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/

dist : distclean
	mkdir vxi11-$(VERSION)
	cp -p vxi11_cmd.cc vxi11_user.cc vxi11_user.h vxi11.x vxi11-$(VERSION)/
	cp -p Makefile CHANGELOG.txt README.txt GNU_General_Public_License.txt vxi11-$(VERSION)/
	tar -zcf vxi11-$(VERSION).tar.gz vxi11-$(VERSION)

distclean : 
	rm -rf vxi11-$(VERSION)
	rm -f vxi11-$(VERSION).tar.gz
