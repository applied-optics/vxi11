include ../config.mk

.PHONY : all static shared install clean dist distclean

UNAME:=$(shell uname -s)

ifneq ($(UNAME),SunOS)
	LDFLAGS:=$(LDFLAGS) -Wl,--version-script=linker.version
endif

OBJ:=vxi11_user.o vxi11_clnt.o vxi11_xdr.o
SDIR:=build-static
DDIR:=build-shared

all : static shared
static : libvxi11.a
shared : libvxi11.so

libvxi11.so : libvxi11.so.${SOVERSION}
	ln -sf libvxi11.so.${SOVERSION} libvxi11.so

libvxi11.so.${SOVERSION} : $(addprefix ${DDIR}/,${OBJ})
	$(CC) $(LDFLAGS) -shared -Wl,-soname,libvxi11.so.${SOVERSION} $^ -o $@

libvxi11.a : $(addprefix ${SDIR}/,${OBJ})
	$(AR) rcs $@ $^

${DDIR}/%.o : %.c vxi11.h | ${DDIR}
	$(CC) -fPIC $(CFLAGS) -c $< -o $@

${SDIR}/%.o : %.c vxi11.h | ${SDIR}
	$(CC) $(CFLAGS) -c $< -o $@

vxi11.h vxi11_clnt.c vxi11_xdr.c : vxi11.x
	rpcgen -M vxi11.x

${SDIR} ${DDIR}:
	@mkdir $@

TAGS: $(wildcard *.c) $(wildcard *.h) $(wildcard *.c)
	etags $^

clean:
	rm -rf ${SDIR} ${DDIR}
	rm -f *.o libvxi11.so libvxi11.so.${SOVERSION} libvxi11.a vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install: all
	$(INSTALL) -d $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	$(INSTALL) libvxi11.a $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	$(INSTALL) libvxi11.so.${SOVERSION} $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/
	ln -sf libvxi11.so.${SOVERSION} $(DESTDIR)$(prefix)/lib${LIB_SUFFIX}/libvxi11.so
	$(INSTALL) -d $(DESTDIR)$(prefix)/include/
	$(INSTALL) vxi11_user.h $(DESTDIR)$(prefix)/include/

