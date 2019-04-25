# 复习

1、we call 1 and 0 "bits".

2、Today we call a "byte" a sequence of 8 bits(1s and 0s).

比如 00001111

3、How a number maps to a letter. 
The most popular convention ended up being American Standard Code for Information Interchange, or ASCII.
This standard maps a number to a letter.
The number 90 is Z, which in bit is 1011010, which gets mapped to the ASCII table inside the computer.

4、 >>> 0b1011010
	90
	>>>ord('Z')
	90
	>>>chr(90)
	'Z'
	
5、The problem with ASCII is that it only encodes English and maybe a few other similar languages.
Remember that a byte can hold 256 numbers.
Different countries created their own encoding conventions for their language

To solve the problem(不同国家用不同的编码), a group of people created Unicode.
It is meant to be a "universal encoding" of all human languages.
You can use 32 bits to encode a Unicode character, and that is more characters than we could possibly find.
A 32-bit number means we can store 4294967295 characters(2^32).
Which is enough space for every possible human language and probably a lot of alien ones too.
多余的空间甚至可以用来给smile emojis。

6、但是32 bits (4 bytes) 太浪费空间了，有些字不需要那么多bits表示。
可以用更好的方式，比如大部分字符用8 bits 表示，其他的就转化为用16或32 bits来表示。

The convention for encoding text in Python is called "UTF-8", which means "Unicode Transformation Format 8 Bits."
You can also use other convention(encodings), but UTF-8 is the current standard.

7、b' xxxx' is raw bytes.

8、DBES ，which stands for Decode Bytes, Encode Strings. 可以记成"deebess",
When you have bytes and need a string, decode bytes. # 有bytes，想要string =》 Decode Bytes
whne you have a string and need bytes, encode strings. # 有string， 想要bytes => Encode Stings
字符encode成 bytes , 而 bytes decode 成字符

 


