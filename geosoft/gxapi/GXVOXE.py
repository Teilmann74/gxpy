### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVOXE:
    """
    GXVOXE class.

    `GXVOX` evaluator class. Used to sample values from
    the voxel.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOXE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVOXE`
        
        :returns: A null `GXVOXE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVOXE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVOXE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1):
        """
        Create a handle to an `GXVOXE` object
        """
        ret_val = gxapi_cy.WrapVOXE.create(GXContext._get_tls_geo(), p1._wrapper)
        return GXVOXE(ret_val)






    def profile(self, p2, p3, p4, p5, p6):
        """
        Extract a profile of data along points provided.
        """
        self._wrapper.profile(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6)
        




    def value(self, p2, p3, p4, p5):
        """
        Get a value at a specific point
        """
        ret_val = self._wrapper.value(p2, p3, p4, p5)
        return ret_val




    def vector(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Extract a profile of data along a vector
        """
        self._wrapper.vector(p2, p3, p4, p5, p6, p7, p8._wrapper, p9)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer