#!/usr/bin/env bash
#

if [ $# -ne 1 ]; then
    echo "Supply file"
    exit 1
fi

grep . $1 > /var/tmp/tmp.file
cat /var/tmp/tmp.file > $1
rm -f /var/tmp/tmp.file

exit 0

