#! /usr/pkg/bin/perl -T

use warnings;
use strict;
use CGI qw(:standard);

my $SCRIPT = $ENV{'SCRIPT_NAME'};

$ENV{'PATH'} = "/bin:/usr/pkg/bin:/usr/local/bin";
delete @ENV{'IFS', 'CDPATH', 'ENV', 'BASH_ENV'};

print "Content-Type: text/html\n\n";

###
### Functions
###

sub printHead() {
	print <<EOH
<HTML>
  <HEAD>
    <TITLE>Foghorn Leghorn Configuration Management</TITLE>
  </HEAD>
  <BODY>
  <H1>Foghorn Leghorn Configuration Management</H1>
EOH
;
}

sub copyIntoPlace($$) {
	my ($u, $dest) = @_;

	if ($dest =~ m/^((.ssh\/)?([a-zA-Z0-9_.]+))$/) {
		$dest = $1;
	} else {
		print "<b>Invalid destination.</b><br>\n";
		end();
		printFoot();
		exit 0;
	}

	my $file = "/home/foghorn/files/$u";
	my $target = "/home/$u/$dest";

	system("/usr/local/bin/$u-cp $file $target 2>&1") == 0 or do {
		print "<b>Unable to copy $file to $target.</b><br>\n";
		end();
		printFoot();
		exit 0;
	};

	print "<b>Ok, file installed as $target.</b><br>\n";
	unlink "$file";
	unlink "$file.sig";

	print "<p><img src=\"../foghorn.png\"></p>\n";
}

sub acceptFile() {
	my $q = new CGI;
	my $home = "/home/foghorn";

	my $pass = `cat $home/chicken`;
	chomp($pass);

	if (!$q->param("chicken") || $q->param("chicken") ne $pass) {
		print "<b>Unauthorized.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	}

	if (!$q->param("dest")) {
		print "<b>What in the world's that hen up to now?</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	}

	my $dest = $q->param("dest");

	if (!$q->param("key")) {
		print "<b>Missing file.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	}

	if (!$q->param("team")) {
		print "<b>Missing team name.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	}

	if (!$q->param("sig")) {
		print "<b>Missing signature.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	}

	my $team = $q->param("team");
	if ($team =~ m/^(.*\/)?(.*)/) {
		$team = $2;
	}

	my $fh = $q->upload('key');
	open(LOCAL, ">$home/files/$team") or do {
		print "<b>Unable to open $home/files/$team: $!.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	};
	while( <$fh>) {
		print LOCAL $_;
	}
	close($fh);
	close(LOCAL); 

	$fh = $q->upload('sig');
	open(LOCAL, ">$home/files/$team.sig") or do {
		print "<b>Unable to open $home/files/$team.sig: $!.</b><br>\n";
		print "Please <a href=\"$SCRIPT\">try again</a>.<br>\n";
		return;
	};
	while( <$fh>) {
		print LOCAL $_;
	}
	close($fh);
	close(LOCAL); 

	print "<p><b>Alrighty, then.  Lemme put those in the right place, I suppose.</b></p>\n";

	verifySig($team);
	copyIntoPlace($team, $dest);

	end();
}


sub end() {
        print <<EOF
  <HR>
  <a href="$SCRIPT">Back</a>
EOF
;
}

sub printForm() {
	print <<EOH
  <h2>Now looka, I say, looka here!</h2>
  <p>
    <FORM name="foghorn" action="$SCRIPT" enctype="multipart/form-data" method="POST">
      <input type="hidden" name="dest" value="chicken">
      <TABLE BORDER="0">
        <TR>
          <TD>Password (MD5):</td>
          <TD><input name="chicken"></TD>
        </TR>
        <TR>
          <TD>Team:</td>
          <TD><input name="team"></TD>
        </TR>
        <TR>
          <TD>File:</td>
          <TD><input type="file" name="key"></TD>
          <TD ROWSPAN="3"><img src="../Foghorn_Leghorn.png"></TD>
        </TR>
        <TR>
          <TD>Signature:</td>
          <TD><input type="file" name="sig"></TD>
        </TR>
        <TR>
          <TD valign="top"><input type="submit" value="Submit" /></TD>
          <TD>&nbsp;</TD>
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

sub verifySig($) {
	my ($n) = @_;

	my $f = "/home/foghorn/files/$n";
	my @args = ("gpg", "--no-default-keyring", "--keyring /var/www/.gnupg/$n.gpg",
			"--verify", "$f.sig", "$f");
	system("gpg --no-default-keyring --keyring /var/www/.gnupg/$n.gpg --verify $f.sig $f >/dev/null 2>&1") == 0 or do {
		print "<b>Invalid signature.</b><br>\n";
		end();
		printFoot();
		exit 0;
	};

	print "<b>Ok, valid signature, so far so good...</b><br>\n";
}

###
### Main
###

printHead();

if ($ENV{'REQUEST_METHOD'} eq "POST") {
	acceptFile();
} else {
	printForm();
}

printFoot();
