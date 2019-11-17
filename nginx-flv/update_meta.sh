#!/bin/sh
LIVE_URL=$1
PUSH_URL=$2

META=$(mktemp /tmp/meta.XXXXXXX)

/usr/local/bin/ffprobe -v quiet -print_format json -show_format -show_streams $LIVE_URL > $META

/usr/bin/curl -i 'Content-Type: application/json' --data @$META $PUSH_URL

rm -f $META
