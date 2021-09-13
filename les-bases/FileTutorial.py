import os
import shutil

source = "password.png"
target = "img/password.png"
# copier/coller
#shutil.copy(source, target)
# couper/coller
shutil.copy(source, target)
os.remove(source)