print("success m8")

''' Absolute Imports
from .\\root_package > python main.py 
from ./root_package $ python3 main.py   
'''
# import module1
# import module2
# from package1 import module3
# from package1 import module4
# from package2 import module5
# from package2 import module6
# from package2.package3 import module7

''' Absolute Imports
from ..\\root_package > python -m root_package.main 
from ../root_package $ python3 -m root_package.main     
'''
# from root_package import module1
# from root_package import module2
# from root_package.package1 import module3
# from root_package.package1 import module4
# from root_package.package2 import module5
# from root_package.package2 import module6
# from root_package.package2.package3 import module7


''' Relative imports (relative to this module)
from ..\\root_package > python -m root_package.main 
from ../root_package $ python3 -m root_package.main     
'''
# from ... import module1
# from ... import module2
# from ...package1 import module3
# from ...package1 import module4
# from .. import module5
# from .. import module6
# from . import module7