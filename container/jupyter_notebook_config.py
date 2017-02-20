# disable auth; these notebooks are meant to be run from
# inside a Docker container running on a laptop
import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python2'
c.NotebookApp.token = ''
c.NotebookApp.password = ''