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
class GXPGEXP:
    """
    GXPGEXP class.

    The `GXPGEXP` class is similar to the `GXEXP` class, but is used
    to apply math expressions to pagers (`GXPG` objects).
    
    It works only on PGs of the same dimensions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPGEXP(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPGEXP`
        
        :returns: A null `GXPGEXP`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXPGEXP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXPGEXP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_pager(self, pg, var):
        """
        This method adds an pager to the `GXPGEXP` object with a
        variable name.
        """
        self._wrapper.add_pager(pg._wrapper, var.encode())
        



    @classmethod
    def create(cls):
        """
        This method creates an `GXPGEXP` object.
        """
        ret_val = gxapi_cy.WrapPGEXP.create(GXContext._get_tls_geo())
        return GXPGEXP(ret_val)






    def do_formula(self, formula, max_len):
        """
        This method runs a formula on the pagers.
        """
        self._wrapper.do_formula(formula.encode(), max_len)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer