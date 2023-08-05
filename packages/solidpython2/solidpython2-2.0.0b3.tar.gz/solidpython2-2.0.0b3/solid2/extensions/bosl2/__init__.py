from ... import config

if config.use_implicit_builtins:
    raise Exception("ExpSolid: unfortunately ImplicitCAD can't handle bosl2...")

from .all import *

#TODO: extend this with all kinds of bosl2 features
from ...core.object_base import ObjectBase
ObjectBase.tag = lambda self, *args, **kwargs: tag(*args, **kwargs)(self)
ObjectBase.attach = lambda self, *args, **kwargs: attach(*args, **kwargs)(self)


#============ attachable add =============
#enhance the add function of the attachable OpenSCADObject so it can be used
#properly: cf. 07-libs-bosl2-attachable.py
attachable_default_add = attachable.add

def attachable_add(self, c):
    if len(self.children) == 0:
        attachable_default_add(self, c)
    elif len(self.children) == 1:
        attachable_default_add(self, union()(c))
    else:
        assert(len(self.children) == 2)
        self.children[1].add(c)

attachable.add = attachable_add
#============ attachable add end =============

