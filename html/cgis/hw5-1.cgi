#! /usr/pkg/bin/perl

use warnings;
use strict;
use CGI qw(:standard);

my $SCRIPT = $ENV{'SCRIPT_NAME'};

my %RESULTS = (
		# grep -c ^en
		"q1" => "3079227",
		# grep "^en" | sort -k3 | tail -1
		# Note: multiple valid, students can argue
		"q2" => "Belgium",
		# grep "^en" | awk '{ sum += $4; } END { print sum ; }'
		"q3" => "260225865937",
		# grep "^en" | awk '{ sum += $3; } END { print sum / 3600; }'
		"q4" => "8038.8",
		# grep "^en" | awk '{ s = $4 / $3; if (s > l) { l = s; largest = $2; }} END { print largest; }'
		"q5" => "Module:Syrian_and_Iraqi_insurgency_detailed_map/doc",
	);

print "Content-Type: text/html\n\n";

###
### Functions
###

sub printHead() {
	print <<EOH
<HTML>
  <HEAD>
    <TITLE>CS615 - HW5</TITLE>
  </HEAD>
  <BODY>
  <H1>Stevens Institute of Technology - Department of Computer Science</H1>
  <H2>CS615 HW5</H2>
EOH
;
}

sub checkAnswers() {
	my $q = new CGI;
	my @names = $q->param;
	my $err = 0;

	foreach my $k (@names) {
		if ($RESULTS{$k} && ($q->param($k) eq $RESULTS{$k})) {
			next;
		}
		print "<b>Incorrect answer for $k.</b><br>\n";
		$err = 1;
	}

	if ($err) {
		print "<p>Sorry, please <a href=\"$SCRIPT\">try again</a>.</p>\n";
		print "<p>If you are convinced that your answers are correct\n";
		print " (which is entirely possible, by the way),\n";
		print " please send an email to the class mailing list to argue your case.</p>\n";
	} else {
		my $a1 = $RESULTS{"q1"};
		my $a2 = $RESULTS{"q2"};
		my $a3 = $RESULTS{"q3"};
		my $a4 = $RESULTS{"q4"};
		my $a5 = $RESULTS{"q5"};
		print <<EOF
<p>Excellent start.</p>
<p>Now take the commands you used to find these answers, and
put them in a script.  The script will take as input the name
of the data file and The output will then be exactly as shown:</p>

<p><blockquote><tt><pre>\$ wikistats inputfile
Unique objects: $a1
Most frequent object: $a2
Total bytes transferred: $a3
Requests per second: $a4
Largest object: $a5
\$ </pre></tt></blockquote></p>

<p>You can submit the script by running this command:</p>

<p><blockquote><tt><pre>curl --data-binary \@wikistats http://ec2-54-145-67-75.compute-1.amazonaws.com/cgi-bin/hw5-2.cgi</pre></tt></blockquote></p>
EOF
;
        }
        print <<EOF
  <HR>
  <a href="$SCRIPT">Back</a>
EOF
;
}

sub printForm() {
	print <<EOH
  <P>
    <FORM name="hw5" action="$SCRIPT" method="GET">
      <TABLE BORDER="0">
        <TR>
          <TD>How many unique objects were requested for <em>en</em> only?</td>
          <TD><input name="q1"></TD>
        </TR>
        <TR>
          <TD>Which is the most often requested object for <em>en</em>?</td>
          <TD><input name="q2"></TD>
        </TR>
        <TR>
          <TD>For <em>en</em> only, how much data was transferred in total?</TD>
          <TD><input name="q3"></TD>
        </TR>
        <TR>
          <TD>For <em>en</em> only, how many requests per second were handled during this hour?</td>
          <TD><input name="q4"></TD>
        </TR>
        <TR>
          <TD>Which was the largest object requested for <em>en</em>?</TD>
          <TD><input name="q5"></TD>
        </TR>
        <TR>
          <TD colspan="2"><input type="submit" value="Submit" /></TD>
        </TR>
      </TABLE>
    </FORM>
EOH
;
}

sub printFoot() {
	print <<EOH
  </BODY>
</HTML>
EOH
;
}

###
### Main
###

printHead();

if ($ENV{'QUERY_STRING'}) {
	checkAnswers();
} else {
	printForm();
}

printFoot();
