#!/bin/sh
set -e

if [ "${1:0:1}" != "-" ]; then
    PS1=${PS1} exec "$@"
fi

exec suricata -c /home/work/suricata.yaml -i eno2
