#!/bin/sh

cd
git clone http://github.com/openstack-dev/devstack.git
cd devstack/
git checkout -b folsom remotes/origin/stable/folsom
git branch

