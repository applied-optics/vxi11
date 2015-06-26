include ../config.mk

.PHONY : all install clean

CFLAGS:=${CFLAGS} -I../library

all : vxi11_cmd vxi11_send

vxi11_cmd: vxi11_cmd.o ../library/libvxi11.so.${SOVERSION}
	$(CC) -o $@ $^ $(LDFLAGS)

vxi11_cmd.o: vxi11_cmd.c ../library/vxi11_user.c ../library/vxi11.h
	$(CC) $(CFLAGS) -c $< -o $@

vxi11_send: vxi11_send.o ../library/libvxi11.so.${SOVERSION}
	$(CC) -o $@ $^ $(LDFLAGS)

vxi11_send.o: vxi11_send.c ../library/vxi11_user.c ../library/vxi11.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o vxi11_cmd vxi11_send

install: all
	$(INSTALL) -d $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_send $(DESTDIR)$(prefix)/bin/

