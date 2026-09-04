"""Example Circle Application
File name:    main.py
Author:       YOUR NAME HERE
Date:         5/14/2025
Class:        CS 170
Assignment:   01Lab
Purpose:      Test functions of the Circle class
Hours:        1.5

"""
from Circle import Circle
import random

def randomValue(fLower = -100.0, fUpper = 100.0):
    """Choose a random value

	Args:
		fLower (float): the lowerbound
        fUpper (float): the upperbound


	Returns:
		A floating point value with at most two digits past the decimal
    """
    iValue = int(random.uniform(fLower, fUpper) * 10)
    fValue = iValue / 10
    return fValue

if __name__ == '__main__':
    lCircles = []
    random.seed(300)

    fBoundry = 30
    fMaxRadius = 25
    fBoundryReduction = 0
    fRadiusReduction = 0
    for iCount in range(20):
        lCircles.append(Circle (randomValue(- (fBoundry - fBoundryReduction),
                                            fBoundry - fBoundryReduction),
                                 randomValue(- (fBoundry - fBoundryReduction),
                                             fBoundry - fBoundryReduction),
                                 randomValue(1, fMaxRadius - fRadiusReduction)))
        fBoundryReduction += 1
        fRadiusReduction += 1

    print(lCircles)

    for iIndex, oOuterCircle in enumerate(lCircles):
        for oInnerCircle in lCircles[iIndex+1:]:
            if oOuterCircle.contains(oInnerCircle):
                print(f'OUTER: {oOuterCircle} contains {oInnerCircle}')
            elif oInnerCircle.contains(oOuterCircle):
                print(f'INNER: {oInnerCircle} contains {oOuterCircle}')

    fLargestArea = 0.0
    oLargestCircle = None
    for oCircle in lCircles:
        if oCircle.area() > fLargestArea:
            fLargestArea = oCircle.area()
            oLargestCircle = oCircle

    print(f'Largest {oLargestCircle} area: {fLargestArea}', end='')
    print(f'{oLargestCircle.area()}')

    fFarthestDistFromCenter = 0.0
    oFarthestCircle = None
    for oCircle in lCircles:
        if oCircle.distanceFromCenter() > fFarthestDistFromCenter:
            fFarthestDistFromCenter = oCircle.distanceFromCenter()
            oFarthestCircle = oCircle

    print(f'Farthest {oFarthestCircle} distance: {fFarthestDistFromCenter}',
          end='')
    print(f'{oFarthestCircle.distanceFromCenter()}')

    print(f'{lCircles[0]} == {lCircles[-1]} {lCircles[0] == lCircles[-1]}')
    print(f'{lCircles[0]} < {lCircles[-1]} {lCircles[0] < lCircles[-1]}')
    print(f'{lCircles[-1]} < {lCircles[0]} {lCircles[-1] < lCircles[0]}')"""Example coding standards
File name:    main.py
Author:       YOUR NAME HERE
Date:         5/14/2025
Class:        CS 300
Assignment:   01Lab
Purpose:      Demonstrate coding standards
Hours:        1.5

"""

from datetime import date

if __name__ == '__main__':
  
  print('Hello world!')
  
  print('Today is', date.today())
