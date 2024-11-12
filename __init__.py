import os
from cudatext import *

class Command:
    
    def on_open_pre(self, ed_self, filename):
        ext = filename.rfind('.') + 1
        if  ext != 0 and filename[ext:].lower() in ('jpg', 'jpeg', 'png', 'bmp', 'ico'):
            print('Ignoring picture:', filename)
            file_open(filename, options='/view-hex')
            return False
            
