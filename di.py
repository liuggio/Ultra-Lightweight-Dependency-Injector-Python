__author__="liuggio"
__date__ ="$09-Apr-2011 14:27:45$"

from types import *

def inject(class_holder, **dependencies):
    if isinstance(class_holder, ClassType):
        # if it is not instantiated we create a new istance
        istance = class_holder()
    else:
        # if it is already instantiated we create/overwrite the attribute
        istance=class_holder
    for dependency in dependencies:
        if isinstance(dependencies[dependency], ClassType):
            # we want the istance not the class
            dependencies[dependency]=dependencies[dependency]()
        setattr(istance, dependency, dependencies[dependency])
    return istance

if __name__ == "__main__":
    # todo
    #      doc comment
    #      unit-test
    #      examples
    pass
