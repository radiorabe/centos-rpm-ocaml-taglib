#!/bin/bash
#
# RPM build wrapper for ocaml-taglib, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/liquidsoap.repo https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_7/home:radiorabe:liquidsoap.repo

yum -y install \
    epel-release \
    http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

chown root:root ocaml-taglib.spec

build-rpm-package.sh ocaml-taglib.spec
