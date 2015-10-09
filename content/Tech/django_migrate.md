Title: django制作first app(1)
Date: 2015-10-7
Category: Tech
Tags: develop, django, migrate
Slug: django_app_1

django中的migrate有三种：
1、makemigrate
2、sqlmigrate
3、migrate

makemigrate，基于当前的model，根据对models的修改，创建新的迁移文件
sqlmigrate，用于显示迁移的SQL语句
migrate，是真正用于执行迁移操作的命令

一般用法是修改models之后，以如下命令顺序执行
	
	python manage.py makemigrate
	python manage.py sqlmigrate appname 0001
	python manage.py migrate

一些简单的查询语句都可以通过对python的对象的操作来实现，比如

	Question.objects.filter(id=1)
	Question.objects.all()
	Question.objects.get(pk=1)
	
	# Question是Choice的外键
	q = Question.objects.get(pk=1)
	c = q.choice_set.create(choice_text='abc', votes=0)
	c = q.choice_set.create(choice_text='def', votes=0)
	q.choice_set.all()
	
	Choice.objects.filter(question__pub_date__year=2015)
	c = q.choice_set.filter(choice_text__startswith='abc')
	c.delete()
