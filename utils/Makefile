include ../config.mk

.PHONY : all install clean

CFLAGS:=${CFLAGS} -I../library
LDFLAGS:=${LDFLAGS} -L../library -lvxi11

all : vxi11_cmd vxi11_send

vxi11_cmd vxi11_send: %: %.o
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o vxi11_cmd vxi11_send

install: all
	$(INSTALL) -d $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_send $(DESTDIR)$(prefix)/bin/

