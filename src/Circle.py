"""Example Circle File
File name:    Circle.py
Author:       YOUR NAME HERE
Date:         5/14/2025
Class:        CS 170
Assignment:   01Lab
Purpose:      Implement a Cirlce
Hours:        1.5

"""
import math

class Circle:
    """Represent a circle with a center point and a radius.

    The class provides basic geometry operations such as calculating area,
    determining whether one circle contains another, and comparing circles.
    """

    __PI = 3.1415926535897932384626

    def __init__(self, fX, fY, fRadius):
        """Initialize the circle with a center coordinate and radius.

        Args:
            fX (float): the x coordinate of the center
            fY (float): the y coordinate of the center
            fRadius (float): the radius of the circle
        """
        self.__tCenter = (fX, fY)
        if fRadius < 0.0:
            raise ValueError(f'Invalid Radius: {fRadius}')
        self.__fRadius = fRadius

    @property
    def center(self):
        """Return the circle's center coordinates.

        Returns:
            tuple: the center point as a tuple
        """
        return self.__tCenter

    @property
    def radius(self):
        """Return the circle's radius.

        Returns:
            float: the radius of the circle
        """
        return self.__fRadius

    @staticmethod
    def distance(fX1, fY1, fX2, fY2):
        """Compute the straight-line distance between two points.

        Args:
            fX1 (float): the x coordinate of point 1
            fY1 (float): the y coordinate of point 1
            fX2 (float): the x coordinate of point 2
            fY2 (float): the y coordinate of point 2

        Returns:
          float: the calculated distance
        """
        return math.sqrt((fX1 - fX2) ** 2 + (fY1 - fY2) ** 2)

    def __str__(self):
        """Return a readable string representation of the circle.

        Returns:
            str: a formatted string describing the circle
        """
        return f'center: {self.__tCenter} radius: {self.__fRadius}'

    def __repr__(self):
        """Return a constructor-like representation for debugging.

        Returns:
            str: a string showing the circle's constructor arguments
        """
        sName = self.__class__.__name__
        return f'{sName}({self.__tCenter[0]},{self.__tCenter[1]},' +\
            f'{self.__fRadius})'

    def contains(self, oOtherCircle):
        """Return True when this circle fully contains another circle.

        Args:
            oOtherCircle (Circle): the circle to test for containment

        Returns:
            bool: True if this circle contains the other circle
        """
        bContains = False

        fCenterDist = Circle.distance(oOtherCircle.center[0],
                                      oOtherCircle.center[1],
                                      self.__tCenter[0], self.__tCenter[1])
        if fCenterDist + oOtherCircle.radius <= self.__fRadius:
            bContains = True

        return bContains

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: the area of the circle
        """
        fArea = Circle.__PI * self.__fRadius ** 2
        return fArea

    def distanceFromCenter(self):
        """Measure the distance from this circle's center to the origin.

        Returns:
            float: the distance from the circle's center to the origin
        """
        return Circle.distance(0, 0, self.__tCenter[0], self.__tCenter[1])

    def __eq__(self, oOther):
        """Compare two circles by center and radius.

        Args:
            oOther (Circle): the circle to compare against

        Returns:
            bool: True if the circles are equal
        """
        bEqual = False

        if self.__fRadius == oOther.radius and \
            self.__tCenter[0] == oOther.center[0] and \
            self.__tCenter[1] == oOther.center[1]:
            bEqual = True

        return bEqual

    def __lt__(self, oOther):
        """Compare circles by closeness to the origin, then by area if needed.

        Args:
            oOther (Circle): the circle to compare against

        Returns:
            bool: True if this circle is less than the other
        """
        bLessThan = False
        if self.distanceFromCenter() < oOther.distanceFromCenter():
            bLessThan = True
        elif self.distanceFromCenter() == oOther.distanceFromCenter():
            if self.area() < oOther.area():
                bLessThan = True

        return bLessThan
