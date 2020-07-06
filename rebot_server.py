# import os
#
# os.chdir("RPC_project")
#
# #os.system('cd {}'.format(path))
# output = os.popen('kill -f python manage.py runserver').read()
#
# print(output)

import subprocess

# subprocess.run(['cd','RPC_project'], shell=True, check=True)
subprocess.run(['manage.py','runserver'],shell=True)