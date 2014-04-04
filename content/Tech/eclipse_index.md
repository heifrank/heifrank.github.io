Title: eclipse的C++索引index
Date: 2014-04-04
Category: Tech
Tags: develop, eclipse
Slug: eclipse_index

eclipse中经常碰到一些头文件找不到的问题，就是程序能编译通过，但是编辑器上就是显式unresolved include files，这个时候，可以对工程进行配置，右键工程的property，找到C/C++ General，里面有个Paths and Symbols，在include的GNU C和GNU C++中都添加相应的头文件，如果只配置C++，那么以.c为后缀的文件就不能找到相应的头文件了，所以把两个都配上。配置好之后如果还不行，那就右键工程，点index，Rebuild就可以了。