
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
	import nologin
	nologin.main()
else:
	import nologin32
	nologin32.main()
