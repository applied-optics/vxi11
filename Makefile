#CFLAGS = -Wall -g
CFLAGS = -g

vxi11_cmd: vxi11_cmd.o vxi11_user.o vxi11_clnt.o vxi11_xdr.o
	g++ $(CFLAGS) -o vxi11_cmd vxi11_cmd.o vxi11_user.o vxi11_clnt.o vxi11_xdr.o

vxi11_cmd.o: vxi11_cmd.cc vxi11_user.cc vxi11.h
	g++ $(CFLAGS) -c vxi11_cmd.cc -o vxi11_cmd.o

vxi11_user.o: vxi11_user.cc vxi11.h
	g++ $(CFLAGS) -c vxi11_user.cc -o vxi11_user.o 

vxi11.h vxi11_clnt.c vxi11_xdr.c : vxi11.x
	rpcgen -M vxi11.x

TAGS: $(wildcard *.c) $(wildcard *.h) $(wildcard *.cc)
	etags $^

clean:
	rm -f *.o vxi11_cmd vxi11.h vxi11_svc.c vxi11_xdr.c vxi11_clnt.c TAGS

install:
	cp -f vxi11_cmd /usr/local/bin/
