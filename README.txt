RPC PROTOCOL FOR COMMUNICATING WITH VXI11-ENABLED DEVICES OVER ETHERNET FROM LINUX
==================================================================================
(including instruments such as oscilloscopes, by manufacturers such as
Agilent and Tektronix, amongst others).

By Steve D. Sharples, June 2006.

This is a collection of source code that will allow you to talk to ethernet-
enabled instruments that use the VXI11 protocol, from Linux. This includes
a wide range of instruments (including oscilloscopes, logic analysers, 
function generators etc) by a wide range of manufacturers (including 
Tektronix and Agilent to name just a couple). An interactive "send and 
receive" utility is included as an example.

You may want to build on to this libraries for your specific instruments - 
I'm currently working on libraries for talking to Agilent Infiniium scopes,
and will probably do the same for Tektronix scopes too. Basically if you've
got a Programmer's Reference for your instrument, and this code, you should
be able to cobble something together.

This collection of code has been produced because I grew frustrated at how
difficult it seemed to be to do a relatively simple task. None of the 
major manufacturers had any "out of the box" Linux solutions to talking to
their instruments (although often I would talk to technical folks who would
try their best to help). One of the solutions offered was to use something
called NI VISA; parts of this are closed source, it was enormous, and I had
worries about legacy issues with changing PC hardware.

Via Guy McBride at Agilent, I obtained a copy of a vxi11.x RPC file similar
to the one included here (although no-one at Agilent seemed to know or care
where it came from). After lots of searching on the information superhighway
I located what I believe is the original source (or something like it); see
the section on vxi11.x below. This source seems to have literally been written
from the published VXI11 protocol. I also received from Agilent a simple
example program that showed you how to use the protocol; working from this 
and the (open) source that uses the vxi11.x that is included here, I wrote
vxi11_cmd and the user libraries.

This collection of source code consists of:

(1) vxi11.x
This file, vxi11.x, is the amalgamation of vxi11core.rpcl and vxi11intr.rpcl
which are part of the asynDriver (R4-5) EPICS module, which, at time of
writing, is available from:
http://www.aps.anl.gov/epics/modules/soft/asyn/index.html
More general information about EPICS is available from:
http://www.aps.anl.gov/epics/
This code is open source, and is covered under the copyright notice and
software license agreement shown below, and also at:
http://www.aps.anl.gov/epics/license/open.php

It is intended as a lightweight base for the vxi11 rpc protocol. If you
run rpcgen on this file, it will generate C files and headers, from which
it is relatively simple to write C programs to communicate with a range
of ethernet-enabled instruments, such as oscilloscopes and function
generators by manufacturers such as Agilent and Tektronix (amongst many
others).

(2) vxi11_user.cc (and vxi11_user.h)
These are (fairly) friendly user libraries. At the core are 4 key functions:
vxi11_open(), vxi11_close(), vxi11_send() and vxi11_receive(). These allow
you to talk to your device. There are also some other functions that I
considered to be generally useful (send_and_receive, functions for sending
and receiving fixed length data blocks etc) that are all non-instrument-
specific.

(3) vxi11_cmd.c
This is a fairly simple interactive utility that allows you to send
commands and queries to your vxi11-enabled instrument, which you
locate by way of IP address. I recommend you start with *IDN? It shows you
how the vxi11_user library works

(4) Makefile
Type "make" to compile the source above. Type "make clean" to remove
old object files and ./vxi11_cmd. Type "make install" to copy 
./vxi11_cmd to /usr/local/bin/

(5) GNU_General_Public_License.txt
Fairly obvious. All programs, source, readme files etc NOT covered by any
other license (e.g. vxi11.x, which is covered by its own open source 
license) are covered by this license.

These programs are free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

These programs are distributed in the hope that they will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

The author's email address is steve.no.spam.sharples@nottingham.ac.uk
(you can work it out!)
