# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__ = "lj"
__date__ = "$09-Apr-2011 14:27:16$"

if __name__ == "__main__":
    print "Hello World"

from di import *



class GitCopyEngine:
    def __init__(self, name='?'):
        self.name = name
        print "-> init FastCopyEngine: "
        
    def run(self):
        print '--> coping with:' + self.name

class RsyncCopyEngine:
    def __init__(self, name='?'):
        self.name = name
        print "-> init SlowCopyEngine: "
        
    def run(self):
        print '--> coping with:' + self.name
        


class FileCopier:
    def __init__(self, name='?'):
        self.name = name
        print "-> init FileCopier: "

    def do_copy(self):
        print "-> starting: " + self.engine.name
        self.engine.run()
        
 


# simple example, RsyncCopyEngine is a class not an object
#dependency injection setter
worker1 = inject(FileCopier, engine=RsyncCopyEngine)
worker1.do_copy();

#console:
# Hello World
#-> init FileCopier:
#-> init SlowCopyEngine:
#-> starting: ?
#--> coping with:?


# simple example 2
# simple example, RsyncCopyEngine is now an object
worker2 = inject(FileCopier, engine=RsyncCopyEngine('woow'))
worker2.do_copy();

#console:
#-> init SlowCopyEngine:
#-> init FileCopier:
#-> starting: woow
#--> coping with:woow


# simple example 3 multiple parameters
# simple example, RsyncCopyEngine is now an object
worker2 = inject(FileCopier, engine=RsyncCopyEngine('woow'), path="/root", ignore_filename="./ignore")
worker2.do_copy();
print worker2.ignore_filename

#console:
#-> init SlowCopyEngine:
#-> init FileCopier:
#-> starting: woows
#--> coping with:woow
#./ignore



# double dependencies setter

#dependency injection creation ( name is a dependency of those)
git01 = inject(GitCopyEngine, name="Git 01")
git02 = inject(GitCopyEngine, name="Git 02")
rsync = inject(RsyncCopyEngine, name="rsync")

#dependency injection setter
worker = inject(FileCopier, filpath="", engine=git01)
worker.do_copy();

#dependency injection setter
worker = inject(worker, filpath="", engine=git02)
worker.do_copy();



