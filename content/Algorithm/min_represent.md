Title: 字符串最小表示
Date: 2015-02-19
Category: Algorithm
Tags: 字符串
Slug: poj_1509

##字符串最小表示

这个是求字符串循环之后的最小串：把字符串先复制一份放到原串末尾，然后对两个串相互比较，这里先比较i=0和j=1这两个串，如果出现了字符不相等的情况，需要选择i和j其中一个改变其值，改多少呢？

如果a[i+k] > a[j+k]，那么把i变成i+k+1即可，为什么呢？为什么i不可能是i到i+k中的值呢？因为无论i取i到i+k中的任何值（假设为i+m），那么我们都可以找到另一个串a[j+m]比a[i+m]要小（因为a[j+k] < a[i+k]），因此i如果变成i+m的话，其实不是最优的。

贴下关键部分的代码


	int go(){
		int i = 0, j = 1, k = 0;
		int sz = strlen(a);
		for(int m = 0; m < sz; m++)
			a[m + sz] = a[m];
		while(i < sz && j < sz && k < sz){
			if(a[i + k] == a[j + k])k++;
			else{
				if(a[i + k] > a[j + k]){
					i = i + k + 1;
				}else{
					j = j + k + 1;
				}
				k = 0;
				if(i == j)j = i + 1;
			}
		}
		return min(i, j) + 1;
	}