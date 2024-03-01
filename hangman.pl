#!/usr/bin/perl

print "What is your word?\n";
$word = <>;
@letters = split(//, $word);


@spaces = split(//,("_" x (length($word)-1)));
@guesses = ();

$num1 = $#spaces+1;
#$letters = join("",@letters);
#$spaces = join("",@spaces);


print "$letters\n$spaces\n";


while (@spaces =~ /_/){
	print "Guess a letter: ";
	$guess = <>;


	@guesses[$#guesses+1] = chomp $guess;

	$index=$#letters;
	$num=0;
	while ($index > 0){
		if (@letters[$num] eq $guess){
			@spaces[$num] = $guess;
			#$spaces = join("",@spaces);
			#print "$spaces\n";
			} 
		$num++;
		$index--;
	}
	$num1--;
}
