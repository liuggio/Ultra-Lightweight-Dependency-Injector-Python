### What is it?

Is just a dependency injector

it's a design pattern for maintain high level on the software quality
[http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs](http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs "http://docs.djangoproject.com/en/dev/misc/design-philosophies/?from=olddocs")



#### ** and is not a Service Locator.**

is useful for small-sized projects, when you want to maintain decency in your code without using invasive frameworks

is useful if you want to test the code, to give a mock object dependencies

is useful to understand how work a stupid dependency injector

is useful to reuse the code

is NOT useful if you have a lot of injected object, is better use a Service Locator and a PROPER DIC framework.

#### ++ todo

injection without instantiation, using __metaclass__ ??
 

 


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


#### The code
	from types import *
	def inject(class_holder, **dependencies):
            if isinstance(class_holder, ClassType):
                istance = class_holder()
            else:
                istance=class_holder
            for dependency in dependencies:
                if isinstance(dependencies[dependency], ClassType):
                    dependencies[dependency]=dependencies[dependency]()
                setattr(istance, dependency, dependencies[dependency])
            return istance

