#!/usr/bin/perl

while( 1 ) {

    $time = time();

    system("sh", "./durhamWeather2.sh");
    sleep(2);
    open( FILE, '/Users/scott1/Development/Perl/weatherDump.txt') or die("can't find file\n");
    open( CSV,  ">>/Users/scott1/Desktop/tempPLots.csv");

    while (<FILE>) {
	chomp;
	if ( $_ =~ /\[13\]Images\s+(-?\d+)/ ) {
	    printf (CSV "\n%4.2f, %d", $time, $1);
	    print "$time, temp: $1\n";
	    break;
	}
    }
    close( FILE );
    close( CSV );
    sleep( 16 * 15);
}
