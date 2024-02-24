#!/usr/bin/perl

print "Enter a word: ";
$word = <>;
@letters = split (//,$word);

@spaces = split(//,("_" x (length($word)-1)));

if (@spaces =~ /\"_"*/){
	print "true\n";
}
