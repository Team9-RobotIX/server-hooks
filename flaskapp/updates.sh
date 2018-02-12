#!/bin/bash
echo "User: "
whoami
echo "Current dir: "
pwd

cd /var/www/html/production/ && git fetch --all && git reset --hard origin/master
cd /var/www/html/development/ && git fetch --all && git reset --hard origin/development
