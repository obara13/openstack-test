#!/bin/sh

cd /opt/stack
for i in [!^d]*
do
	cd $i
	git pull
	cd ..
done
cd

