import os 
import sys
module_path = os.path.abspath(os.path.join(__file__, *([os.pardir]*3)))
if module_path not in sys.path:
    sys.path.append(module_path)
    sys.path.append(module_path+"\\")
    sys.path.append('..\..\..')
    sys.path.append('..\..')
    sys.path.append('..')

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project_root to sys.path
if project_root not in sys.path:
    sys.path.append(project_root)