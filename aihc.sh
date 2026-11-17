#!/bin/sh

export AIHC_CORE_LIBS_ROOT=/usr/share/aihc

exec /usr/libexec/aihc ${1+"$@"}
