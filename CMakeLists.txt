project(vxi11)

cmake_minimum_required(VERSION 2.6)

set (VERSION 1.10)

add_custom_command(OUTPUT ${vxi11_SOURCE_DIR}/vxi11.h
		${vxi11_SOURCE_DIR}/vxi11_clnt.c
		${vxi11_SOURCE_DIR}/vxi11_xdr.c
		${vxi11_SOURCE_DIR}/vxi11_svc.c
	PRE_BUILD
	COMMAND rpcgen -M ${vxi11_SOURCE_DIR}/vxi11.x
	MAIN_DEPENDENCY ${vxi11_SOURCE_DIR}/vxi11.x
	COMMENT "Generating RPC code")

# ==================================================
# Shared library for vxi11
# ==================================================

add_library(vxi11 SHARED
	vxi11_user.cc vxi11_user.h
	vxi11.h
	vxi11_clnt.c
	vxi11_xdr.c
	vxi11.x
)

set_target_properties(vxi11 PROPERTIES
	VERSION 0.${VERSION}
	SOVERSION 0
)

if (CYGWIN)
	include_directories(/usr/include/tirpc)
	target_link_libraries(vxi11 tirpc)
endif (CYGWIN)

# ==================================================
# Command line utility
# ==================================================

add_executable(vxi11_cmd vxi11_cmd.cc)
target_link_libraries(vxi11_cmd vxi11)
