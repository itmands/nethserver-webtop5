#!/bin/bash

#import from PST to WebTop5

shopt -s globstar

/usr/bin/which readpst &>/dev/null
if [ "$?" -ne 0 ]; then
    echo "libpst not installed. Run first: yum install libpst "
    exit
fi

if [ "$#" -ne 2 ]; then
    echo "Usage: pst2webtop.sh <filename.pst> <user>"
    exit
fi

dir=`mktemp -d` 
newdir=`mktemp -d` 

domain=`hostname -d` 

user=$2@$domain

while true; do
    read -p "Do you wish to import email? [Y]es/[N]o: " yn
    case $yn in
        [Yy]* ) EMAIL='Y'; break;;
        [Nn]* ) EMAIL='N'; break;;
        * ) echo "Please answer yes or no.";;
    esac
done

mkdir -p /var/lib/nethserver/vmail/$user/Maildir/

if [ -f $1 ]; then
    readpst -o $dir -r $1
else
    echo "File not found: $1"
    exit
fi


cd $dir
for f in **/mbox; do mkdir -p "$newdir/$(dirname "$f")"; mv "$f" "$newdir/$(dirname "$f").mbox" ; done

if [ $EMAIL == "Y" ] ; then
	/usr/share/webtop/doc/mb2md.pl -s $newdir -R -d /var/lib/nethserver/vmail/$user/Maildir/ -r mbox
	chown -R vmail.vmail /var/lib/nethserver/vmail/$user/Maildir/
else
  echo "Email Skipped."
fi

cd $dir
for f in **/calendar; do echo "Events Folder found: $f"; echo "    Import to webtop: "; echo "./pst2webtop_cal.php $2 '$dir/$f' <foldername>" ; echo ; done
for f in **/calendar; do echo "./pst2webtop_cal.php $2 '$dir/$f' <foldername>" >> /tmp/pst2webtop$$.log  ; echo ; done
for f in **/contacts; do echo "Contacts Folder found: $f"  ; echo "    Import to webtop: "; echo "./pst2webtop_card.php $2 '$dir/$f' <foldername>" ; echo ; done
for f in **/contacts; do echo "./pst2webtop_card.php $2 '$dir/$f' <foldername>" >> /tmp/pst2webtop$$.log; echo ; done

echo "log created: /tmp/pst2webtop$$.log"

