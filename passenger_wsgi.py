import sys, os
INTERP = os.path.join(os.environ['HOME'], 'dev.cameronyick.us', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

#APP is the filename
from DemoFile import app as application
