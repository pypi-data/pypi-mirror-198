"""Model of an epicycloid. An epicycloid is a specific case of an epitrochoid
where the distance from the rolling circle is equal to its radius.
"""

from typing import List, Tuple
from numbers import Number

from spyrograph.epitrochoid.epitrochoid import Epitrochoid
from spyrograph._cycloid import _Cycloid

class Epicycloid(_Cycloid, Epitrochoid):
    """Model of a epicycloid which is a special case of a epitrochoid where the
    circle is rolling around the outside of the fixed circle and has 1/3 the
    radius of the fixed circle
    """
    def __init__(
            self, R: Number, r: Number, thetas: List[Number] = None,
            theta_start: Number = None, theta_stop: Number = None,
            theta_step: Number = None, origin: Tuple[Number, Number] = (0, 0)
        ) -> None:
        super().__init__(R, r, r, thetas, theta_start, theta_stop, theta_step, origin)
