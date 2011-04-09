### What is it?

Is just a dependency injector

it's a design pattern for maintain high level on the software quality
[http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs](http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs "http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs")



#### ** and is not a Service Locator.**

is useful for small and medium-sized projects, where you want to maintain decency in the code without using invasive framework.

is useful if you want to test the code, to give a mock object dependencies.

is useful to understand how work a simple dependency injector

is useful to reuse the code

It is useful if you have a lot of requests injected object, since each request to reallocate use a Service Locator

 


### What is a Dependency Injection or DI?
[martinfowler.com/articles/injection.html](http://martinfowler.com/articles/injection.html "Martin Fowler DependencyInjection")

### How it works?

	from di import *
	
	# instance = inject(Class, tuple of parameters)
	
	EmailSender = inject(Mailer, dispatcher=SmtpLibV02)
	# EmailSender is now instantiated 
	# and has the attribute 'dispatcher' with SmtpLib instantiated


----------------------


### Install

please fork it and add some ideas :)
	
	git clone git@github.com:liuggio/Ultra-Lightweight-Dependency-Injector-Python.git di
	cd di
	python example.py 

#### Few Examples 

[https://github.com/liuggio/Ultra-Lightweight-Dependency-Injector-Python/blob/master/example.py](https://github.com/liuggio/Ultra-Lightweight-Dependency-Injector-Python/blob/master/example.py "https://github.com/liuggio/Ultra-Lightweight-Dependency-Injector-Python/blob/master/example.py")