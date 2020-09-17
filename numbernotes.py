(Number Bases)
------------

It's the "language" that a number is written down in .

Douze == Twelve
1100 == 12

Base 2: binary
Base 8: octal(rarely used)
Base 10: decimal(what we know from grade school, regular boring ol numbers)
Base 16: hexadecimal, "hex"
Base 64: base 64


base 10 (decimal)

+-----1000's place 10 ^ 3
|+----100's place  10 ^ 2
| | +---10's place   10 ^ 1
| | |+--1's place    10 ^ 0
| | ||
abcd

1 2 3 4

1 1000
2 100s
3 10s
4 1s

1234 == 1 * 1000 + 2 * 100 + 3 * 10 + 4 * 1
        ^ ^ ^ ^

base 2 (binary)

+-----8's place    2 ^ 3
|+----4's place    2 ^ 2
| | +---2's place    2 ^ 1
| | |+--1's place    2 ^ 0
| | ||
abcd

0011 binary

0011 binary == 0 * 8 + 0 * 4 + 1 * 2 + 1 * 1 == 3 decimal
^
binary digits("bit")

8 bits == "byte"
4 bits == "nybble"

To specify the base in code:

Prefix
------
[none] decimal
0b     binary
0x     hex
0o     octal


yello
#ffff00  #ffffff  #000000

red      green    blue
255      255      0        decimal base 10

ff       ff       00       hex     base 16
11111111 11111111 00000000 binary  base 2
--------
  byte

 0
 1
 2
 3
 4
 5
 6
 7
 8
 9
 A
 B
 C
 D
 E
 F
10
11
12
13
.
.
.
FD
FE
FF




0000 0
0001 1
0010 2
0011 3
0100 4
0101 5
0110 6
0111 7
1000 8
1001 9
1010 A
1011 B
1100 C 
1101 D
1110 E
1111 F


0b00101010 == 0x2A
00101010 binary == 2A hex

  0010 1010
    2   A



0b101 == 5

0b1100 == 0xC




0b10110011 == 0xB3 == 179
  *.**..**
  ||||||||
  ||||||||

  ......*.
  ||||||||
  ||||||||
