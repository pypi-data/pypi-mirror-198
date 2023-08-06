from copy import deepcopy
from typing import Dict, Literal
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

from compas.geometry import Point
from compas.geometry import Translation
from compas.geometry import NurbsSurface
from compas.geometry import Curve
from compas.geometry import Vector
from compas.utilities import flatten

from compas_occ.conversions import compas_point_from_occ_point
from compas_occ.conversions import compas_point_to_occ_point
from compas_occ.conversions import array2_from_points2
from compas_occ.conversions import array1_from_floats1
from compas_occ.conversions import array2_from_floats2
from compas_occ.conversions import array1_from_integers1
from compas_occ.conversions import floats2_from_array2
from compas_occ.conversions import points2_from_array2

from compas_occ.geometry import OCCNurbsCurve

from OCC.Core.Geom import Geom_BSplineSurface
from OCC.Core.GeomFill import GeomFill_BSplineCurves
from OCC.Core.GeomFill import GeomFill_StretchStyle
from OCC.Core.GeomFill import GeomFill_CoonsStyle
from OCC.Core.GeomFill import GeomFill_CurvedStyle
from OCC.Core.GeomAPI import GeomAPI_PointsToBSplineSurface
from OCC.Core.GeomAbs import GeomAbs_C2

from .surface import OCCSurface


class ControlPoints:
    def __init__(self, surface: "OCCNurbsSurface") -> None:
        self.occ_surface = surface

    @property
    def points(self) -> List[List[Point]]:
        return points2_from_array2(self.occ_surface.Poles())

    def __getitem__(self, index: Union[int, Tuple[int, int]]) -> Point:
        try:
            u, v = index
        except TypeError:
            return self.points[index]
        else:
            pnt = self.occ_surface.Pole(u + 1, v + 1)
            return compas_point_from_occ_point(pnt)

    def __setitem__(self, index: Tuple[int, int], point: Point) -> None:
        u, v = index
        self.occ_surface.SetPole(u + 1, v + 1, compas_point_to_occ_point(point))

    def __len__(self) -> int:
        return self.occ_surface.NbVPoles()

    def __iter__(self) -> Iterable:
        return iter(self.points)


class OCCNurbsSurface(OCCSurface, NurbsSurface):
    """Class representing a NURBS surface based on the BSplineSurface of the OCC geometry kernel.

    Parameters
    ----------
    name : str, optional
        The name of the curve

    Attributes
    ----------
    points : list[list[:class:`~compas.geometry.Point`]], read-only
        The control points of the surface.
    weights : list[list[float]], read-only
        The weights of the control points of the surface.
    u_knots : list[float], read-only
        The knots of the surface in the U direction, without multiplicities.
    v_knots : list[float], read-only
        The knots of the surface in the V direction, without multiplicities.
    u_mults : list[int], read-only
        The multiplicities of the knots of the surface in the U direction.
    v_mults : list[int], read-only
        The multiplicities of the knots of the surface in the V direction.

    Other Attributes
    ----------------
    occ_surface : ``Geom_BSplineSurface``
        The underlying OCC surface.

    Examples
    --------
    Construct a surface from points...

    .. code-block:: python

        from compas.geometry import Point
        from compas_occ.geometry import OCCNurbsSurface

        points = [
            [Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0)],
            [Point(0, 1, 0), Point(1, 1, 2), Point(2, 1, 2), Point(3, 1, 0)],
            [Point(0, 2, 0), Point(1, 2, 2), Point(2, 2, 2), Point(3, 2, 0)],
            [Point(0, 3, 0), Point(1, 3, 0), Point(2, 3, 0), Point(3, 3, 0)],
        ]

        surface = OCCNurbsSurface.from_points(points=points)

    Construct a surface from points...

    .. code-block:: python

        from compas.geometry import Point
        from compas_occ.geometry import OCCNurbsSurface

        points = [
            [Point(0, 0, 0), Point(1, 0, +0), Point(2, 0, +0), Point(3, 0, +0), Point(4, 0, +0), Point(5, 0, 0)],
            [Point(0, 1, 0), Point(1, 1, -1), Point(2, 1, -1), Point(3, 1, -1), Point(4, 1, -1), Point(5, 1, 0)],
            [Point(0, 2, 0), Point(1, 2, -1), Point(2, 2, +2), Point(3, 2, +2), Point(4, 2, -1), Point(5, 2, 0)],
            [Point(0, 3, 0), Point(1, 3, -1), Point(2, 3, +2), Point(3, 3, +2), Point(4, 3, -1), Point(5, 3, 0)],
            [Point(0, 4, 0), Point(1, 4, -1), Point(2, 4, -1), Point(3, 4, -1), Point(4, 4, -1), Point(5, 4, 0)],
            [Point(0, 5, 0), Point(1, 5, +0), Point(2, 5, +0), Point(3, 5, +0), Point(4, 5, +0), Point(5, 5, 0)],
        ]

        weights = [
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ]

        surface = OCCNurbsSurface.from_parameters(
            points=points,
            weights=weights,
            u_knots=[1.0, 1 + 1/9, 1 + 2/9, 1 + 3/9, 1 + 4/9, 1 + 5/9, 1 + 6/9, 1 + 7/9, 1 + 8/9, 2.0],
            v_knots=[0.0, 1/9, 2/9, 3/9, 4/9, 5/9, 6/9, 7/9, 8/9, 1.0],
            u_mults=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            v_mults=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            u_degree=3,
            v_degree=3,
        )

    """

    def __init__(self, name: str = None) -> None:
        super().__init__(name=name)
        self._points = None

    def __eq__(self, other: "OCCNurbsSurface") -> bool:
        for a, b in zip(flatten(self.points), flatten(other.points)):
            if a != b:
                return False
        for a, b in zip(flatten(self.weights), flatten(other.weights)):
            if a != b:
                return False
        for a, b in zip(self.u_knots, self.v_knots):
            if a != b:
                return False
        for a, b in zip(self.u_mults, self.v_mults):
            if a != b:
                return False
        if self.u_degree != self.v_degree:
            return False
        if self.is_u_periodic != self.is_v_periodic:
            return False
        return True

    # ==============================================================================
    # Data
    # ==============================================================================

    @property
    def data(self) -> Dict:
        """dict : Represenation of the surface as a Python dict."""
        return {
            "points": [[point.data for point in row] for row in self.points],
            "weights": self.weights,
            "u_knots": self.u_knots,
            "v_knots": self.v_knots,
            "u_mults": self.u_mults,
            "v_mults": self.v_mults,
            "u_degree": self.u_degree,
            "v_degree": self.v_degree,
            "is_u_periodic": self.is_u_periodic,
            "is_v_periodic": self.is_v_periodic,
        }

    @data.setter
    def data(self, data: Dict) -> None:
        points = [[Point.from_data(point) for point in row] for row in data["points"]]
        weights = data["weights"]
        u_knots = data["u_knots"]
        v_knots = data["v_knots"]
        u_mults = data["u_mults"]
        v_mults = data["v_mults"]
        u_degree = data["u_degree"]
        v_degree = data["v_degree"]
        is_u_periodic = data["is_u_periodic"]
        is_v_periodic = data["is_v_periodic"]
        self.occ_surface = Geom_BSplineSurface(
            array2_from_points2(points),
            array1_from_floats1(weights),
            array1_from_floats1(u_knots),
            array1_from_floats1(v_knots),
            array1_from_integers1(u_mults),
            array1_from_integers1(v_mults),
            u_degree,
            v_degree,
            is_u_periodic,
            is_v_periodic,
        )

    @classmethod
    def from_data(cls, data: Dict) -> "OCCNurbsSurface":
        """Construct a BSpline surface from its data representation.

        Parameters
        ----------
        data : dict
            The data dictionary.

        Returns
        -------
        :class:`OCCNurbsSurface`
            The constructed surface.

        """
        points = [[Point.from_data(point) for point in row] for row in data["points"]]
        weights = data["weights"]
        u_knots = data["u_knots"]
        v_knots = data["v_knots"]
        u_mults = data["u_mults"]
        v_mults = data["v_mults"]
        u_degree = data["u_degree"]
        v_degree = data["v_degree"]
        is_u_periodic = data["is_u_periodic"]
        is_v_periodic = data["is_v_periodic"]
        return OCCNurbsSurface.from_parameters(
            points,
            weights,
            u_knots,
            v_knots,
            u_mults,
            v_mults,
            u_degree,
            v_degree,
            is_u_periodic,
            is_v_periodic,
        )

    # ==============================================================================
    # Constructors
    # ==============================================================================

    @classmethod
    def from_parameters(
        cls,
        points: List[List[Point]],
        weights: List[List[float]],
        u_knots: List[float],
        v_knots: List[float],
        u_mults: List[int],
        v_mults: List[int],
        u_degree: int,
        v_degree: int,
        is_u_periodic: bool = False,
        is_v_periodic: bool = False,
    ) -> "OCCNurbsSurface":
        """Construct a NURBS surface from explicit parameters.

        Parameters
        ----------
        points : list[list[:class:`~compas.geometry.Point`]]
            The control points of the surface.
        weights : list[list[float]]
            The weights of the control points.
        u_knots : list[float]
            The knots in the U direction, without multiplicities.
        v_knots : list[float]
            The knots in the V direction, without multiplicities.
        u_mults : list[int]
            The multiplicities of the knots in the U direction.
        v_mults : list[int]
            The multiplicities of the knots in the V direction.
        u_dergee : int
            Degree in the U direction.
        v_degree : int
            Degree in the V direction.
        is_u_periodic : bool, optional
            Flag indicating that the surface is periodic in the U direction.
        is_v_periodic : bool, optional
            Flag indicating that the surface is periodic in the V direction.

        Returns
        -------
        :class:`OCCNurbsSurface`

        """
        surface = cls()
        surface.occ_surface = Geom_BSplineSurface(
            array2_from_points2(points),
            array2_from_floats2(weights),
            array1_from_floats1(u_knots),
            array1_from_floats1(v_knots),
            array1_from_integers1(u_mults),
            array1_from_integers1(v_mults),
            u_degree,
            v_degree,
            is_u_periodic,
            is_v_periodic,
        )
        return surface

    @classmethod
    def from_points(
        cls,
        points: List[List[Point]],
        u_degree: int = 3,
        v_degree: int = 3,
    ) -> "OCCNurbsSurface":
        """Construct a NURBS surface from control points.

        Parameters
        ----------
        points : list[list[:class:`~compas.geometry.Point`]]
            The control points.
        u_degree : int, optional
        v_degree : int, optional

        Returns
        -------
        :class:`OCCNurbsSurface`

        """
        u = len(points[0])
        v = len(points)
        weights = [[1.0 for _ in range(u)] for _ in range(v)]
        u_degree = u_degree if u > u_degree else u - 1
        v_degree = v_degree if v > v_degree else v - 1
        u_order = u_degree + 1
        v_order = v_degree + 1
        x = u - u_order
        u_knots = [float(i) for i in range(2 + x)]
        u_mults = [u_order]
        for _ in range(x):
            u_mults.append(1)
        u_mults.append(u_order)
        x = v - v_order
        v_knots = [float(i) for i in range(2 + x)]
        v_mults = [v_order]
        for _ in range(x):
            v_mults.append(1)
        v_mults.append(v_order)
        is_u_periodic = False
        is_v_periodic = False
        return cls.from_parameters(
            points,
            weights,
            u_knots,
            v_knots,
            u_mults,
            v_mults,
            u_degree,
            v_degree,
            is_u_periodic,
            is_v_periodic,
        )

    @classmethod
    def from_step(cls, filepath: str) -> "OCCNurbsSurface":
        """Load a NURBS surface from a STP file.

        Parameters
        ----------
        filepath : str

        Returns
        -------
        :class:`OCCNurbsSurface`

        """
        raise NotImplementedError

    @classmethod
    def from_fill(
        cls,
        curve1: OCCNurbsCurve,
        curve2: OCCNurbsCurve,
        curve3: OCCNurbsCurve = None,
        curve4: OCCNurbsCurve = None,
        style: Literal["stretch", "coons", "curved"] = "stretch",
    ) -> "OCCNurbsSurface":
        """Construct a NURBS surface from the infill between two, three or four contiguous NURBS curves.

        Parameters
        ----------
        curve1 : :class:`~compas_occ.geometry.OCCNurbsCurve`
        curve2 : :class:`~compas_occ.geometry.OCCNurbsCurve`
        curve3 : :class:`~compas_occ.geometry.OCCNurbsCurve`, optional.
        curve4 : :class:`~compas_occ.geometry.OCCNurbsCurve`, optional.
        style : Literal['stretch', 'coons', 'curved'], optional.

            * ``'stretch'`` produces the flattest patch.
            * ``'curved'`` produces a rounded patch.
            * ``'coons'`` is between stretch and coons.

        Raises
        ------
        ValueError
            If the fill style is not supported.

        Returns
        -------
        :class:`OCCNurbsSurface`

        """

        if style == "stretch":
            style = GeomFill_StretchStyle
        elif style == "coons":
            style = GeomFill_CoonsStyle
        elif style == "curved":
            style = GeomFill_CurvedStyle
        else:
            ValueError("Scheme is not supported")

        surface = cls()
        if curve3 and curve4:
            occ_fill = GeomFill_BSplineCurves(
                curve1.occ_curve,
                curve2.occ_curve,
                curve3.occ_curve,
                curve4.occ_curve,
                style,
            )
        elif curve3:
            occ_fill = GeomFill_BSplineCurves(
                curve1.occ_curve, curve2.occ_curve, curve3.occ_curve, style
            )
        else:
            occ_fill = GeomFill_BSplineCurves(curve1.occ_curve, curve2.occ_curve, style)
        surface.occ_surface = occ_fill.Surface()
        return surface

    @classmethod
    def from_extrusion(cls, curve: Curve, vector: Vector) -> "OCCNurbsSurface":
        """Construct a NURBS surface from an extrusion of a basis curve.

        Note that the extrusion surface is constructed by generating an infill
        between the basis curve and a translated copy with :meth:`from_fill`.

        Parameters
        ----------
        curve : :class:`compas_occ.geometry.Curve`
            The basis curve for the extrusion.
        vector : :class:`compas.geometry.Vector`
            The extrusion vector, which serves as a translation vector for the basis curve.

        Returns
        -------
        :class:`OCCNurbsSurface`

        """
        other = curve.transformed(Translation.from_vector(vector))
        return cls.from_fill(curve, other)

    @classmethod
    def from_interpolation(
        cls, points: List[Point], precision: float = 1e-3
    ) -> "OCCNurbsSurface":
        """Construct a NURBS surface by approximating or interpolating a 2D collection of points.

        Parameters
        ----------
        points : [list[:class:`compas.geometry.Point`], list[:class:`compas.geometry.Point`]]
            The 2D collection of points.
        precision : float, optional
            The fitting precision.

        Returns
        -------
        :class:`OCCNurbsSurface`

        """
        points = array2_from_points2(points)
        surface = GeomAPI_PointsToBSplineSurface(
            points, 3, 8, GeomAbs_C2, precision
        ).Surface()
        return cls(surface)

    # ==============================================================================
    # Conversions
    # ==============================================================================

    # ==============================================================================
    # OCC
    # ==============================================================================

    # ==============================================================================
    # Properties
    # ==============================================================================

    @property
    def points(self) -> List[List[Point]]:
        if not self._points:
            self._points = ControlPoints(self.occ_surface)
        return self._points

    @property
    def weights(self) -> List[List[float]]:
        weights = self.occ_surface.Weights()
        if not weights:
            weights = [[1.0] * len(self.points[0]) for _ in range(len(self.points))]
        else:
            weights = floats2_from_array2(weights)
        return weights

    @property
    def u_knots(self) -> List[float]:
        return list(self.occ_surface.UKnots())

    @property
    def v_knots(self) -> List[float]:
        return list(self.occ_surface.VKnots())

    @property
    def u_mults(self) -> List[int]:
        return list(self.occ_surface.UMultiplicities())

    @property
    def v_mults(self) -> List[int]:
        return list(self.occ_surface.VMultiplicities())

    # ==============================================================================
    # Methods
    # ==============================================================================

    def copy(self) -> "OCCNurbsSurface":
        """Make an independent copy of the current surface.

        Returns
        -------
        :class:`compas_occ.geometry.OCCNurbsSurface`

        """
        cls = type(self)
        return cls.from_data(deepcopy(self.data))
