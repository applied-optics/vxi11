VERSION=1.10

include config.mk

DIRS=library utils

.PHONY : all clean install

all :
	for d in ${DIRS}; do $(MAKE) -C $${d}; done

clean:
	for d in ${DIRS}; do $(MAKE) -C $${d} clean; done

install:
	for d in ${DIRS}; do $(MAKE) -C $${d} install; done

	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_send $(DESTDIR)$(prefix)/bin/
	$(INSTALL) libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	ln -sf libvxi11.so.0 $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/libvxi11.so
	$(INSTALL) vxi11.h vxi11_user.h $(DESTDIR)$(prefix)/include/

dist : distclean
	mkdir vxi11-$(VERSION)
	cp -pr library utils vxi11-$(VERSION)/
	cp -p Makefile CMakeLists.txt CHANGELOG.txt README.txt GNU_General_Public_License.txt vxi11-$(VERSION)/
	tar -zcf vxi11-$(VERSION).tar.gz vxi11-$(VERSION)

distclean : 
	rm -rf vxi11-$(VERSION)
	rm -f vxi11-$(VERSION).tar.gz
