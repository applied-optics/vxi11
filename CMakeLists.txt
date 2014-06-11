# For compiling on Windows.

project(vxi11)

cmake_minimum_required(VERSION 2.6)

set (VERSION 1.10)

if (NOT WIN32)
add_custom_command(OUTPUT ${vxi11_SOURCE_DIR}/vxi11.h
		${vxi11_SOURCE_DIR}/vxi11_clnt.c
		${vxi11_SOURCE_DIR}/vxi11_xdr.c
		${vxi11_SOURCE_DIR}/vxi11_svc.c
	PRE_BUILD
	COMMAND rpcgen -M ${vxi11_SOURCE_DIR}/vxi11.x
	MAIN_DEPENDENCY ${vxi11_SOURCE_DIR}/vxi11.x
	COMMENT "Generating RPC code")
endif (NOT WIN32)

# ==================================================
# Shared library for vxi11
# ==================================================

set(vxi11_SRCS library/vxi11_user.c library/vxi11_user.h)
if (WIN32)
	include_directories(C:\\VXIpnp\\WINNT\\include)
	link_directories(C:\\VXIpnp\\WINNT\\lib\\msc)
else (WIN32)
	set(vxi11_SRCS ${vxi11_SRCS} library/vxi11.h library/vxi11_clnt.c
		library/vxi11_xdr.c library/vxi11.x)
endif (WIN32)


add_library(vxi11 SHARED ${vxi11_SRCS})

set_target_properties(vxi11 PROPERTIES
	VERSION 0.${VERSION}
	SOVERSION 0
)

if(WIN32)
	target_link_libraries(vxi11 visa32)
endif(WIN32)

if (CYGWIN)
	include_directories(/usr/include/tirpc)
	target_link_libraries(vxi11 tirpc)
endif (CYGWIN)

# ==================================================
# Command line utility
# ==================================================

add_executable(vxi11_cmd utils/vxi11_cmd.c)
target_link_libraries(vxi11_cmd vxi11)

add_executable(vxi11_send utils/vxi11_send.c)
target_link_libraries(vxi11_send vxi11)
