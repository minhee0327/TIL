#!/bin/bash

LOGDIR=/var/log
GZIPDAY=1
DELDAY=2
cd $LOGDIR
echo "cd $LOGDIR"

sudo find . -type f -name '*log.?' -mtime +$GZIPDAY -exec bash -c "gzip {}" \; 2> /dev/null
sudo find . -type f -name '*gz' -mtime +$DELDAY -exec bash -c "rm -f"\; 2> /dev/null


