class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition
    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"
    def __eq__(self, rhs):
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == rhs.condition:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def __lt__(self, rhs):
        if self.rent < rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                conditions = {"bad":0, "average":1, "excellent":2}
                return conditions[self.condition] > conditions[rhs.condition]
            else:
                return False
        else:
            return False
    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                conditions = {"bad":0, "average":1, "excellent":2}
                return conditions[self.condition] < conditions[rhs.condition]
            else:
                return False
        else:
            return False
    
