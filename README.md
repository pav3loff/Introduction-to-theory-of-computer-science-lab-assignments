# Introduction-to-theory-of-computer-science-lab-assignments
Python source codes for lab assignments on UTR class @FER, University of Zagreb

This is the source code which simulates finite automata with epsilon transitions.
The task is given as lab assignment on Introduction to theory of computer science 
class at Faculty of electrical engineering and computing (FER), University of Zagreb.

The code is public, free to use and fully functional. Use it on your own risk.

### AUTOMATA FUNCTIONALITY DESCRIPTION BELOW ###

Program reads automata definition from standard input.

Definition is given is such fashion:

  -In first line input strings are given and split by "|", ex. a,b,c|b,d,e|f,g,h|t,r,w
  
  -In second line all the possible states are split by ",", ex. s1,s2,s3,s4,s5
  
  -In third line all the possible symbols the automata works with are split by ",", ex. a,b,c,d,e,f,g
  
  -in fourth line acceptable states are split by ",", ex. s4, s5
  
  -In fifth line the starting state is given, ex. s1
  
  -In sixth and all the other lines transition functions are given like following: s1,a->s2
                                                                                   s2,b->s3
                                                                                   s3,c->s4
                                                                                   
                                                                                   
After the automata definition is given, the program will write out which states automata was in for

every symbol in given input string, ex:


01 s1|s2,s3|s4,s5

02 s3|s2,s4|s3

03 s4|s1|s2,s3,s5


States will be printed in alphabetical order.

Epsilon transition is coded by symbol "$".

If there are no next states for given current states in given transition, next states (empty states) are coded by symbol "#".

### SIMPLE EXAMPLE ON HOW AUTOMATA WILL WORK FOR GIVEN INPUT ###

Given input:

a,pnp,a|pnp,lab2|pnp,a|pnp,lab2,utr,utr

p5,s3,s4,st6,s1,s2

a,lab2,pnp,utr

p5

s1

s3,a->s2

s3,lab2->p5,s4

s4,$->st6

s4,utr->p5,s3

s1,a->stanje2

s1,pnp->s3

s2,$->st6

s2,a->#


Result:

01 s1|st6,s2|#|#

02 s1|s3|p5,s4,st6

03 s1|s3|st6,s2

04 s1|s3|p5,s4,st6|p5,s3|#
