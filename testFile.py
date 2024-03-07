from Apartment import Apartment
from lab06 import *

def test_Apartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert a1.getRent() == 950
    assert a1.getMetersFromUCSB() == 215
    assert a1.getCondition() == "average"
    assert a2 < a1
    assert a0 > a1
    assert a3 == a3
def test_lab06():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad"
