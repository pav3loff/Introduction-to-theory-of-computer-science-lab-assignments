# Introduction-to-theory-of-computer-science-lab-assignments
Python source codes for lab assignments on UTR class @FER, University of Zagreb

This is the source code which simulates finite automata with epsilon transitions.
The task is given as lab assignment on Introduction to theory of computer science 
class at Faculty of electrical engineering and computing (FER), University of Zagreb.

The code is public, free to use and fully functional. Use it on your own risk.

### AUTOMATA FUNCTIONALITY DESCRIPTION BELOW ###

Program reads automata definition from standard input.→→
Definition is given is such fashion:__
  -In first line input strings are given and split by "|", ex. a,b,c|b,d,e|f,g,h|t,r,w__
  -In second line all the possible states are split by ",", ex. s1,s2,s3,s4,s5__
  -In third line all the possible symbols the automata works with are split by ",", ex. a,b,c,d,e,f,g__
  -in fourth line acceptable states are split by ",", ex. s4, s5__
  -In fifth line the starting state is given, ex. s1__
  -In sixth and all the other lines transition functions are given like following: s1,a->s2__
                                                                                   s2,b->s3__
                                                                                   s3,c->s4__
                                                                                   
After the automata definition is given, the program will write out which states automata was in for__ 
every symbol in given input string, ex:__

01 s1|s2,s3|s4,s5__
02 s3|s2,s4|s3__
03 s4|s1|s2,s3,s5__

States will be printed in alphabetical order.__
Epsilon transition is coded by symbol "$".__
If there are no next states for given current states in given transition, next states (empty states)__
are coded by symbol "#"__

### SIMPLE EXAMPLE ON HOW AUTOMATA WILL WORK FOR GIVEN INPUT ###__
Given input:__
a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr__
p5,s3,s4,st6,s1,s2__
a,lab2,pnp,utr__
p5__
s1__
s3,a->s2__
s3,lab2->p5,s4__
s4,$->st6__
s4,utr->p5,s3__
s1,a->stanje2__
s1,pnp->s3__
s2,$->st6__
s2,a->#__

Result:__
01 s1|st6,s2|#|#__
02 s1|s3|p5,s4,st6__
03 s1|s3|st6,s2__
04 s1|s3|p5,s4,st6|p5,s3|#__
