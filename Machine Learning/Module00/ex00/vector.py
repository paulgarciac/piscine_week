class Vector:

    def __init__(self, datalist):
        
        if isinstance(datalist, int):
            self.datalist =  [[i] for i in range(datalist)]
            self.__isColumn = True
        elif isinstance(datalist[0], list):
            self.datalist = datalist
            self.__isColumn = True
        elif isinstance(datalist, list):
            self.datalist = datalist
            self.__isColumn = False
        else:
            print("Objects must be lists or lists of lists (columns or vectors)")
            self.__isColumn = None
            exit()

    def shape(self): #working for columns and matrix. Row vectors are not working here.
            return (len(self.datalist[:]), len(self.datalist[0][:]))

    def __add__(self, v2): # ici, la methode appelle self (ici appele self)
        if isinstance(v2, Vector):
            v3 = []
            if (self.__isColumn == False and v2.__isColumn == False):
                    for i in range(len(self.datalist)):
                        v3.append(self.datalist[i] + v2.datalist[i])
                    return v3
            elif len(self.datalist[:]) == len(v2.datalist[:]):
                if (self.__isColumn == True and v2.__isColumn == True):
                    self_ = [i[0] for i in self.datalist]
                    v2_ = [i[0] for i in v2.datalist]
                    for i in range(len(self_)):
                        v3.append([self_[i] + v2_[i]])
                    return v3
            else:
                print("vectors must be of the same size")
        else:
            print("the second object must be a vector")

    def __dot__(self, v2):
        if isinstance(v2, Vector):
            lig = len(self.datalist[:]) # nb of lines ; vv
            col = len(v2.datalist[0][:]) # nb of columns ; maxmimal in the case of a row vector.
            T = []
            i = 0
            j = 0
            while i < lig: # create the dimensions necessary for the transpose
                T.append([])
                i += 1
            i = 0
            while i < lig:
                j = 0
                while j < col:
                    T[i].append(self.datalist[i][j]*v2.datalist[i][j])
                    j += 1
                i += 1
            return Vector(T)

    def T(self): #working for columns and matrix. Row vectors are not working here.
        T = []
        i = 0
        j = 0
        while j < len(self.datalist[0][:]): # create the dimensions necessary for the transpose
            T.append([])
            j += 1
        while i < len(self.datalist[:]):
            j = 0
            while j < len(self.datalist[0][:]):
                T[j].append(self.datalist[i][j])
                j += 1
            i += 1
        return Vector(T)

    def __mul__(self, v2): #multipling matrix and vector columns one-by-one.
        if isinstance(v2, Vector):
            lig = len(self.datalist[:]) # nb of lines ; vv
            col = len(v2.datalist[0][:]) # nb of columns ; maxmimal in the case of a row vector.
            T = []
            i = 0
            j = 0
            while i < lig: # create the dimensions necessary for the transpose
                T.append([])
                i += 1
            i = 0
            while i < lig:
                j = 0
                while j < col:
                    T[i].append(self.datalist[i][j]*v2.datalist[i][j])
                    j += 1
                i += 1
            return Vector(T)
