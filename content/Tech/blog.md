Title: 折腾博客
Date: 2014-03-26
Category: Tech
Tags: blog
Slug: blog_notice

博客出问题好久了，一直没有注意搞，今天终于好好弄了一遍，记录一些问题。  

记得在git shell中加入git remote add origin https://github.com/heifrank/heifrank.github.io.git，查看的时候可以用git remote -v来查  
之前出的问题是git的submodule相关的，不太了解git具体怎么用，好像说是要用gitmodule这个文件，还有一些命令什么的，没搞清楚  
其实说白了就是pelican-themes和pelican-plugins是两个子模块，之前不用指定gitmodule就能用，现在不行了，必须用gitmodule  
我于是把主题和插件的位置都换成了本机的绝对路径，就没问题了，具体可以见pelicanconf.py的设置即可  

开始配置的时候好像还需要git user什么的，记不清了，记下有这么个东西就好，省的以后出错了都不知道该往什么方向改。