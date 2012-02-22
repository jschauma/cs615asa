#! /bin/sh
#
# $Author: jschauma $
# $Id: runcmd.sh,v 1.1 2006/01/30 17:30:56 jschauma Exp $
#
# Given a test file containing lines such as
#
# hostname        ip.address      # commment
#
# This program runs a given command for each host in that file.  The command
# given on the command-line is executed once for each hostname that applies.
# If the command contains the string "@HOST@", then this string is substituted
# with the hostname of the machine the program is currently operating on.
#
# See -h for details.


FILE=${RUNCMD_HOSTS}
MATCH_FIELD=0

usage()
{
	echo "Usage: $0 [ -? | -h ] [ -c <pattern> ] [ -H <pattern> ]"
	echo "    [ -s <pattern> ] [ -f <file> ] -C <command>"
	echo "    -?, -h        print a usage message and exit successfully"
	echo "    -c <pattern>  only operate on hosts in the file that match"
	echo "                  the specified comment pattern"
	echo "    -f <file>     specify the location of the file to read the"
	echo "                  machine descriptions from."
	echo "    -H <pattern>  only operate on hosts in the file that match"
	echo "                  the specified hostname pattern"
	echo "    -s <pattern>  only operate on hosts in the file that match"
	echo "                  the specified subnet pattern"
	echo "    -C <command>  specify the command to run for each machine"
}

while getopts C:H:?c:f:hs: opts
do
	case "$opts" in
		C)
			CMD="$OPTARG";
			;;
		H)
			MATCH_FIELD=1
			MATCH="$OPTARG";
			;;
		h|\?)
			usage
			exit 0
			;;
		c)
			MATCH_FIELD=3
			MATCH="$OPTARG";
			;;
		f)
			FILE="$OPTARG";
			;;
		s)
			MATCH_FIELD=2
			MATCH="$OPTARG";
			;;
		-)	shift; break
			;;
	esac
done

if [ -z "${FILE}" ]; then
	echo "$0: Either set \$RUNCMD_HOSTS or use '-f <file>'"
	exit 1
elif [ ! -r ${FILE} ]; then
	echo "$0: Unable to read ${FILE}."
	exit 1
fi

if [ -z "${CMD}" ]; then
	usage
	exit 1
fi

awk -v CMD="${CMD}" -v MF=${MATCH_FIELD} -v PAT="${MATCH}" <${FILE} '

/^#/ { next }

{
	HOST=$1
	RUNCMD=CMD
	gsub("@HOST@", HOST, RUNCMD)
}


MF == 3 {
	sub("^.*# ","")
	if ($0 ~ PAT)
		system(RUNCMD)
}

MF < 3 && $MF ~ PAT {
	system(RUNCMD)
}
'
