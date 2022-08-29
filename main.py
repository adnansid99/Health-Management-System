# Health management system
from func.selectName import *
from func.selectTask import *
from func.selectFileAction import *
from func.mainAction import mainAction

x = selectName()
y = selectTask()
z = selectFileAction()

mainAction(x, y, z)
