#! /bin/sh

echo "Content-type: text/html"
echo

###

DATASET="pagecounts-20160802-070000.gz"
DATAFILE="/var/www/${DATASET}"
EXPECTED="/var/www/expected2"
MAXTIME="595"
INCREMENT="5"
SUBMISSION="$(mktemp ${TMPDIR:-/tmp}/XXXXXX)"
OUTDIR="$(mktemp -d ${TMPDIR:-/tmp}/XXXXXX)"
OUTPUT="${OUTDIR}/your-output"
ERRFILE="${OUTDIR}/.err"

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
	echo "this might take a while."
	echo
}

###

#trap cleanup 0

receiveSubmission

(
"${SUBMISSION}" -h > "${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
	exit 1
}
"${SUBMISSION}" -b -d zh.m.voy "${DATAFILE}" >>"${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
	exit 1
}
"${SUBMISSION}" -f -d ny "${DATAFILE}" >>"${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
	exit 1
}
"${SUBMISSION}" -r -d es.m "${DATAFILE}" >>"${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
	exit 1
}
"${SUBMISSION}" -l -d all "${DATAFILE}" >>"${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
	exit 1
}
"${SUBMISSION}" -u -d all "${DATAFILE}" >>"${OUTPUT}" || {
	echo "Unable to execute your program."
	echo >"${ERRFILE}"
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

if [ -f "${ERRFILE}" ]; then
	exit 1
fi

cd ${OUTDIR} 
cp ${EXPECTED} ${OUTDIR}/expected
out="$(diff -bu your-output expected 2>&1)"
if [ $? -gt 0 ]; then
	echo "Incorrect output."
	echo
	echo "I ran the following commands:"
cat <<EOH
yourfile -h "${DATASET}"
yourfile -b -d zh.m.voy "${DATASET}
yourfile -f -d ny "${DATASET}"
yourfile -r -d es.m "${DATASET}"
yourfile -l -d all "${DATASET}"
yourfile -u -d all "${DATASET}"
EOH

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

Well done!  Now tar it up and submit your
work.  Remember to include the script itself
as well as a README file explaining how
you solved the problems, why you chose
the solutions you did pick, what you learned
etc.

Submit a single tar archive named after
your username and send it via email to
jschauma@stevens.edu with a subject of
"[CS615] HW5".

Thanks, and have a nice day!
EOH

fi

exit 0
