Title: 素数筛的复杂度分析
Date: 2014-03-28
Category: Algorithm
Tags: 数论, 素数
Slug: prime_complex


典型的求素数用的是筛子的方法，最简单的程序是这样的
	void getPrime(int n){
		int mk[100005] = {0};
		vector<int> prime;

		for(int i=2; i<=n; i++){
			if(!mk[i])prime.push_back(i);
			for(int j=i+i; j<=n; j+=i)
				mk[j] = 1;
		}
	}

那如果要筛出<=n的质数，大概的复杂度是多少呢？  
其实需要的次数为n x (1 + 1/2 + 1/3 + 1/4 + ... + 1/n)，这个和是发散的，但是这个数小于n x (1 + 1/2 + 1/2 + 1/4 + 1/4 + 1/4 + 1/4 + ...)，也就是小于n x (1 + 1 + 1 + ...)，一共有k个1，其中2的k次方小于等于n。这样看来，其实操作次数并不会太多。