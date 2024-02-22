#!/usr/bin/perl

print "What is your word?\n";
$word = <>;
@letters = split(//, $word);


@spaces = split(//,("_" x (length($word)-1)));
@guesses = ();

$num1 = $#spaces+1;
$letters = @letters;
$spaces = @spaces;


while ($spaces ne $letters){
	print "Guess a letter: ";
	$guess = <>;


	@guesses[$#guesses+1] = chomp $guess;

	$index=$#letters;
	$num=0;
	while ($index > 0){
		if (@letters[$num] eq $guess){
			@spaces[$num] = $guess;
			$spaces = @spaces;
			} 
		$num++;
		$index--;
	}
	$num1--;
}
