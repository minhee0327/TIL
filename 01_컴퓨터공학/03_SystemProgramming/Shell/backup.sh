#!/bin/bash

if [ -z $1 ]||[ -z $2 ]
then
	echo 'usage: $0 sourcedir targetdir'
else
	SRCDIR=$1
	DSTDIR=$2
	BACKUPFILE=backup.$(date +%y%m%d%H%M%S).tar.gz
	if [ -d $DSTDIR ]
	then
		tar -cvzf $DSTDIR/$BACKUPFILE $SRCDIR
	else
		mkdir $DSTDIR
		tar -cvzf $DSTDIR/$BACKUPFILE $SRCDIR
	fi
fi
