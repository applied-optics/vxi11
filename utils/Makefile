include ../config.mk

.PHONY : all install clean

all : vxi11_cmd vxi11_send

vxi11_cmd: vxi11_cmd.o ../library/libvxi11.so.0
	$(CXX) -o $@ $^ $(LDFLAGS)

vxi11_cmd.o: vxi11_cmd.cc vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

vxi11_send: vxi11_send.o ../library/libvxi11.so.0
	$(CXX) -o $@ $^ $(LDFLAGS)

vxi11_send.o: vxi11_send.cc vxi11_user.cc vxi11.h
	$(CXX) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o vxi11_cmd vxi11_send

install: all
	$(INSTALL) vxi11_cmd $(DESTDIR)$(prefix)/bin/
	$(INSTALL) vxi11_send $(DESTDIR)$(prefix)/bin/

