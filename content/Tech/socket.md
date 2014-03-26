Title: socket基本用法
Date: 2013-11-11
Category: Tech
Tags: learning, socket
Slug: socket_basic

写个文章记录一下基本的socket的使用

##一、面向连接的编程TCP
####1、服务器端：
首先建立socket

	sockfd = socket(AF_INET, SOCK_STREAM, 0)
第二个参数说明是面向连接的编程，如果返回-1代表出错，否则返回socket描述符的值；  
然后本机配置一个sockaddr_in类型的地址

	myaddr.sin_family = AF_INET;  
	myaddr.sin_port = htons(SERVER_PORT);  
	myaddr.sin_addr.s_addr = INADDR_ANY;//这个值代表自动为这个字段填入本机的IP地址  
	memset(&myaddr.sin_zero, 0, sizeof(myaddr.sin_zero));
接下来要将socket和配置的地址绑定

	bind(sockfd, (struct sockaddr *)&myaddr, sizeof(struct sockaddr))
如果返回值为-1代表出错；  
接下来设置同时接收请求的最大数量

	listen(sockfd, NUM)
NUM代表最大的同时请求的数量，这个函数在tcp连接中才有用。  
之后就一直监听sockfd，用accpet函数

	client_fd = accept(sockfd, (struct sockaddr *)&client_addr, &size)
这里的参数意义是，sockfd代表作为服务的socket，第二个参数是代表向服务端发送请求的客户端的地址信息，第三个是一个指向的内容为sizeof(sockaddr_in)的指针，也就是说需要在调用这个函数之前设置size=sizeof(sockaddr_in)，返回值是一个新的socket描述符，就是说accept函数接收了远方客户端的请求，然后把客户端的地址放在了client_addr里，之后为客户端创建了一个新的socket，以后服务器就可以通过这个client_fd来和客户端收发数据了。

####2、客户端：
客户端不需要bind函数，因为客户端很多情况下不需要知道自己用的是哪个端口和服务器通信；客户端也要建立socket，也要配置sockaddr_in类型的地址，这个地址里存放的是远方服务器的地址信息，然后调用connect来进行和服务器的TCP连接，connect函数会自动为客户端分配可用的端口来和服务器通信

	int connect(int sockfd, struct sockaddr* server_addr, int addrlen)
其中sockfd就是客户端创建的文件描述符，server_addr就是要填写的远端服务器的信息，addrlen一般设置为sizeof(struct sockaddr)

####3、收发数据：
面向连接的收发数据函数为send和recv

	int send(int sockfd, const void* msg, int len, int flags)
sockfd是用来传输数据的socket描述符，msg是一个指向要发送的数据的指针，len是以字节为单位的要发送的数据的长度，flags一般设置为0
返回值是实际发送的数据的长度，如果这个长度和len不相等的话，需要自己处理一下

	int recv(int sockfd, void *buf, int len, unsigned int flags)
sockfd是用来接收数据的socket描述符，buf是用来存放接收数据的缓冲区，len是缓冲区的长度（如果定义buf[SIZE]，那么len就为SIZE）,flags一般也设置为0，recv返回实际接收的字节数，如果返回-1说明接收错误。

##二、面向无连接的编程UDP
大致情况和上面相同，不过有几个函数不需要，一个是connect，一个是accept，还有一个是listen。客户端建立完socket，配置好服务器地址之后，直接调用sendto或者recvfrom函数就可以和服务器交互数据了（相比tcp连接少了connect的过程）。服务器创建完socket，绑定端口之后就也可以调用sendto和recvfrom来和客户端交互数据（相比tcp连接少了listen的过程，同时也少了和connect相对应的accept过程）。

	int sendto(int sockfd, const void *msg, int len, unsigned int flags, const struct sockaddr* to, int tolen)
前面四个参数和send的含义一致，to需要填写远端地址，tolen一般设置为sizeof(struct sockaddr)

	int recvfrom(int sockfd, void *buf, int len, unsigned int flags, struct sockaddr* from , socklen_t *fromlen)
前四个参数的含义和recv的一致，调用函数之后，from中写入了数据来源的地址，fromlen是一个指向内容为sizeof(struct sockaddr)的指针，就是说调用函数之前要设置*fromlen = sizeof(struct sockaddr)。


##三、小小的感受
connect和accept的关系和sendto和recvfrom的关系很像，参数设置也很像，如果sendto和recvfrom不收发数据的话，那两者的参数基本就一致了。connect对应sendto，把sendto的第2到第5个参数去掉，含义就和connect一样了；accept对应recvfrom，把recvfrom的第2到第5个参数去掉，含义就和accept一样了。
