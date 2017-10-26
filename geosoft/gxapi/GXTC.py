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
class GXTC:
    """
    GXTC class.

    The `GXTC` object is used in gravitational modelling to create
    a terrain correction grid from a topography grid. This is
    accomplished with a call first to `grregter`, which determines
    the terrain correction from an input topography grid, then
    to `grterain`, which calculates the actual corrections at
    the input positions.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTC`
        
        :returns: A null `GXTC`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, img, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        """
        Creates a Terrain Correction object
        """
        ret_val = gxapi_cy.WrapTC.create(GXContext._get_tls_geo(), img._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        return GXTC(ret_val)



    @classmethod
    def create_ex(cls, img, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        """
        Creates a Terrain Correction object	with surveytype
        """
        ret_val = gxapi_cy.WrapTC.create_ex(GXContext._get_tls_geo(), img._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        return GXTC(ret_val)






    def grregter(self, im_gi, p3):
        """
        Create a terrain correction grid for a topo grid.
        """
        self._wrapper.grregter(im_gi._wrapper, p3._wrapper)
        




    def grterain(self, gv_vx, p3, p4, p5, p6, p7, p8):
        """
        Calculate terrain corrections.
        """
        self._wrapper.grterain(gv_vx._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8)
        




    def grterain2(self, gv_vx, p3, p4, p5, p6, p7, p8, p9):
        """
        Calculate terrain corrections (work for marine gravity too).
        """
        self._wrapper.grterain2(gv_vx._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9)
        




    def g_gterain(self, gv_vx, p3, p4, p5, p6, p7, p8):
        """
        Calculate GG terrain corrections
        """
        self._wrapper.g_gterain(gv_vx._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer