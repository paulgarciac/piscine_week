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
            print("Objects must be lists or lists of lists (columns)")
            self.__isColumn = None
            exit()

    def shape(self):
        if self.__isColumn == False:
            return (1, len(self.datalist[:]))
        if self.__isColumn == True:
            return (len(self.datalist[:]), len(self.datalist[0][:]))

    def __add__(v1, v2): # ici, la methode appelle self (ici appele v1)
        if isinstance(v2, Vector):
            if len(v1.datalist) == len(v2.datalist):
                v3 = []
                if (v1.__isColumn == True and v2.__isColumn == True):
                    v1_ = [i[0] for i in v1.datalist]
                    v2_ = [i[0] for i in v2.datalist]
                    for i in range(len(v1_)):
                        v3.append([v1_[i] + v2_[i]])
                    return v3
                elif (v1.__isColumn == False and v2.__isColumn == False):
                    for i in range(len(v1.datalist)):
                        v3.append(v1.datalist[i] + v2.datalist[i])
                    return v3
            else:
                print("vectors must be of the same size")

    # def __dot__(v1, v2):

    def T(self):
        T = []
        i = 0
        j = 0
        while j < len(self.datalist[0][:]): # create the dimensions necessary for the transpose
            T.append([])
            j += 1
        while i < len(self.datalist[:]):
            j = 0
            while j < len(self.datalist[0][:]):
                print("i : ", i, ". j :", j)
                print(self.datalist[i][j])
                T[j].append(self.datalist[i][j])
                j += 1
            i += 1
        return T