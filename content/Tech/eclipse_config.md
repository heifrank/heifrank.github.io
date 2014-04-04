Title: windows下用eclipse开发C++
Date: 2013-10-10
Category: Tech
Tags: develop, eclipse
Slug: eclipse_cplusplus_windows

eclipse + cdt + mingw的一些配置
下载标准版本的eclipse（我用的是4.3.0版本的，也叫kepler），下载对应版本的CDT(8.2.0)，安装mingw，我是用mingw-get-inst-20120426.exe装的（这个版本我用的比较舒服，如果在官网上下载mingw的话，安装完可能缺少libiconv2，它是个windows运行的dll库，一般电脑上貌似没有这个库，如果没有它的话不能执行make命令），选装gcc和g++两个组件，如果按照默认路径（C:\MinGW）装可能会碰到少一点的问题。

cdt有两种下载方式，可以在eclipse的help中通过install安装，也可以在网上下载，然后把下载完的压缩包解压，把里面的features文件夹和plugins文件夹复制到eclipse的根目录中，和eclipse的根目录中的features、plugins文件夹合并就行。

1、头文件unresolved问题  
这个可以通过在环境变量中设置PATH=MinGW\bin来解决，如果设置了这个path的话，那么eclipse会自动找mingw的一些头文件库，加入到工程中的include文件夹下面（刚创建工程的时候只有一个src目录，没有include目录）。不幸的是，有的时候可能不起作用，我的就是加入了变量，但是不管用，后来把变量删了，又重新加入了一次才管用，很奇怪。

如果真的加了变量，再删除，再加入变量还是不可以找到头文件目录的话，可以用下面的方法：  
在具体的工程中，加入依赖的库文件：  
MinGW/include  
MinGW/lib/gcc/mingw32/4.6.2/include  
MinGW/lib/gcc/mingw32/4.6.2/include/c++  
MinGW/lib/gcc/mingw32/4.6.2/include/c++/backward  
MinGW/lib/gcc/mingw32/4.6.2/include/c++/mingw32  
MinGW/lib/gcc/mingw32/4.6.2/include-fixed  
在一个工程中导入这些配置后，可以export这个配置到一个xml中，这样方便以后写其他工程。

另外还有一个解决办法就是在环境变量中添加这些值，需要的有  
PATH=MinGW\bin（这个确定可以找到一些gcc.exe，make.exe等二进制文件，但是不确定能否找到相关的头文件库）  
C_INCLUDE_PATH对应第一个路径  
CPLUS_INCLUDE_PATH对应第二到第六个路径（第二个路径和第六个路径我不知道该归为哪里）  
LIBRARY_PATH的=MinGW\lib（貌似不设置也可以）  

2、cannot run program "g++"  
这个是下载了cdt之后，装好mingw出现的问题，在命令行中我们直接gcc什么的都没问题，说明环境变量中有mingw的相关路径，但是eclipse中没有，解决办法是在eclipse安装包里的plugins目录下，有个叫org.eclipse.cdt.core.win32.x86_5.2.0.201306112328.jar的压缩包，解压这个压缩包，然后把这个jar删除掉，就可以了。注意解压的不是org.eclipse.cdt.core.win32_5.3.0.201306112328.jar!!!

3、build正常，可以生成.exe，但是一执行就显示terminated xxx.exe [C/C++ Application]  
这个有两个解决办法，一个是在你创建的工程中配置linker，在linker-flags中写入-static-libgcc -static-libstdc++  
还有一个解决办法就是在run configurations里配置你要运行的.exe的environment，加入一组键值对path->mingw\bin  
有些人可能在那个window的preferences里面设置environment，但是这个设置有时候好使有时候不好使，坑爹。