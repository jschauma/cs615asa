#! /bin/sh

echo "Content-type: text/html"
echo

###

DATASET="pagecounts-20160804-100000.gz"
DATAFILE="/var/www/${DATASET}"
EXPECTED="/var/www/expected"
MAXTIME="295"
INCREMENT="5"
SUBMISSION="$(mktemp ${TMPDIR:-/tmp}/XXXXXX)"
OUTDIR="$(mktemp -d ${TMPDIR:-/tmp}/XXXXXX)"
OUTPUT="${OUTDIR}/your-output"

cleanup() {
	rm -fr "${SUBMISSION}" "${OUTDIR}"
}

receiveSubmission() {

	if [ x"${REQUEST_METHOD}" != x"POST" ]; then
		echo "Invalid HTTP Method."
		exit 1
	fi
	if [ x"${CONTENT_TYPE}" != x"application/x-www-form-urlencoded" ]; then
		echo "Invalid Content-Type: '${CONTENT_TYPE}'"
		exit 1
	fi

	dd of="${SUBMISSION}" bs=1 count=$CONTENT_LENGTH
	chmod a+rx "${SUBMISSION}"

	echo "Upload complete. Now running some tests."
	echo "Depending on what you're doing in your script,"
	echo "this might take a moment."
	echo
}

###

trap cleanup 0

receiveSubmission

(
"${SUBMISSION}" "${DATAFILE}" > "${OUTPUT}" || {
	echo "Unable to execute your program."
	exit 1
}
) &

sleep 2
s=0
while [ 1 ]; do
	if ! kill -0 $! 2>/dev/null; then
		break
	else
		if [ $s -gt ${MAXTIME} ]; then
			echo "Terminated program after $s seconds."
			kill -9 $!
			exit 1
		else
			s=$(( $s + ${INCREMENT} ))
			sleep ${INCREMENT}
			echo "..."
		fi
	fi
done

cd ${OUTDIR}
cp ${EXPECTED} ${OUTDIR}/expected
out="$(diff -bu your-output expected 2>&1)"
if [ $? -gt 0 ]; then
	echo "Incorrect output."
	echo
	echo "${out}"
	echo
	cat <<EOH
Note: this was run against the file '${DATASET}'.

If you are convinced that your program is correct
and that this script is wrong (which, by the way,
is entirely possible), please send a mail to the
class mailing list with all relevant details.
EOH
else
	cat <<EOH
Pass.

Alrighty, then.  Now let's turn it up to 11.
Take your script, and add command-line options
to allow the user to specify other domains
besides 'en' as well as options to only produce
one of the desired stats.

The resulting usage for your script will then be:

$ wikistats -h
 -b           only print 'total bytes' stats
 -d <domain>  if not specified, default to 'en'
              note: the special domain 'all' is also valid
 -f           only print 'most frequent' stats
 -h           print this help and exit
 -l           only print 'largest object' stats
 -r           only print 'requests per second' stats
 -u           only print 'unique objects' stats
$ wikistats -b -d fr.m pagecounts-20160802-070000.gz
14965877981
$ wikistats -d de.m.q -l pagecounts-20160802-070000.gz
Johann_Wolfgang_von_Goethe
$ 


As before, you can test your script via curl(1),
this time like so:

curl --data-binary @wikistats http://ec2-54-145-67-75.compute-1.amazonaws.com/cgi-bin/hw5-2.cgi
EOH

fi

exit 0
