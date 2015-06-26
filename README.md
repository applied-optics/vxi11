RPC PROTOCOL FOR COMMUNICATING WITH VXI11-ENABLED DEVICES OVER ETHERNET FROM LINUX
==================================================================================

(including instruments such as oscilloscopes, by manufacturers such as
Agilent and Tektronix, amongst others).

By Steve D. Sharples, June 2006.


Background
----------

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
`vxi11_cmd` and the user libraries.


Source code
-----------

This package consists of a user library, `libvxi11`, two command line
utilities, `vxi11_cmd` and `vxi11_send`, and a Python wrapper for libvxi11.

To compile, run `make`, then and `make install` to install.

See `library/vxi11_user.h` for the functions provided by the library.


Utilities
---------

`vxi11_cmd` is a simple interactive utility that allows you to send commands
and queries to your VXI11 enabled instrument. You will need to consult the
reference manual for your device to find the appropriate commands. You could
start by sending `*IDN?`.

`vxi11_send` is a simple interactive utility that allows you to send a single
command to your VXI11 enabled instrument.


License
-------

library/vxi11.x is covered by its own license, see the file for more details.

Fairly obvious. All programs, source, readme files etc NOT covered by any
other license (e.g. vxi11.x, which is covered by its own open source 
license) are covered by the GNU GPL version 2 or later.

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
