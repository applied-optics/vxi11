/* Revision history: */
/* $Id: vxi11_cmd.c,v 1.3 2007-07-10 13:45:00 sds Exp $ */
/*
 * $Log: not supported by cvs2svn $
 * Revision 1.2  2006/06/26 12:43:11  sds
 * Used the new vxi11_() functions that used the CLINK structure.
 *
 * Revision 1.1  2006/06/26 10:23:52  sds
 * Initial revision
 *
 */

/* vxi11_cmd.c
 * Copyright (C) 2006 Steve D. Sharples
 *
 * A simple interactive utility that allows you to send commands and queries to
 * a device enabled with the VXI11 RPC ethernet protocol. Uses the files
 * generated by rpcgen vxi11.x, and the vxi11_user.h user libraries.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 * 
 * The author's email address is steve.sharples@nottingham.ac.uk
 */

#include "vxi11_user.h"
#define BUF_LEN 100000

int	main(int argc, char *argv[]) {

static char	*device_ip;
static char	*device_name;
char		cmd[256];
char		buf[BUF_LEN];
int		ret;
long		bytes_returned;
CLINK		*clink;

	clink = new CLINK;

	if (argc < 2) {
		printf("usage: %s your.inst.ip.addr [device_name]\n",argv[0]);
		exit(1);
		}

	device_ip = argv[1];
	if (argc > 2) {
		device_name = argv[2];
		ret=vxi11_open_device(device_ip,clink,device_name);
		}
	else {
		ret=vxi11_open_device(device_ip,clink);
		}

	if (ret != 0) {
		printf("Error: could not open device %s, quitting\n",device_ip);
		exit(2);
		}

	while(1){
		memset(cmd, 0, 256);		// initialize command string
		memset(buf, 0, BUF_LEN);	// initialize buffer
		printf("Input command or query ('q' to exit): ");
		fgets(cmd,256,stdin);
		cmd[strlen(cmd)-1] = 0;		// just gets rid of the \n
		if (strncasecmp(cmd, "q",1) == 0) break;

		if (vxi11_send(clink, cmd) < 0) break;
		if (strstr(cmd, "?") != 0) {
			bytes_returned = vxi11_receive(clink, buf, BUF_LEN);
			if (bytes_returned > 0) {
				printf("%s\n",buf);
				}
			else if (bytes_returned == -15) {
				printf("*** [ NOTHING RECEIVED ] ***\n");
				}
			else	break;
			}
		}

	ret=vxi11_close_device(device_ip,clink);
	return 0;
	}

