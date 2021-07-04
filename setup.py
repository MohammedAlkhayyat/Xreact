import pandas as pd

class rxn:
    def __init__(self, i, reactants, products,equa):

        global a 
        self.reactants = reactants
        self.products = products
        self.equa = equa
        import pandas as pd
        global df;
        try:
            df = pd.read_csv('ElementData.csv')
        except:
            df = pd.read_csv('Database.csv')

    def atoms(self):
        
        
        
        
    #i is the reaction number index for multiple reactions
    #Define lists
        atom = [];
        atom1 = [];
    
    
        #This loop will cycle through the input components and list, append them into the list
        for comp in self.reactants:
            atom.append(list(comp));
    
        #This loop will cycle through the output components and list, append them into the list

        for comp in self.products:
            atom1.append(list(comp));    
        
        #The output should give a list that contains the inputs and outputs with each seprated by atom
        #Chemical reaction should also be given as an output    
        return atom, atom1;
    
    
    def atom_sort(self):
        num = 1
        element_list = []
        stio_list = []
        num_list = []
        end = 0
        r = 0
        global elem
        LookForNumber = 0
        LookForFloat = ''
        Acc = ''
        AccU = ''
        LookForAcc = ''
        for batch in self.reactants, self.products:
            for comp in batch:
                for elem in comp:
                    if LookForAcc == 1:
                        if isfloat(elem):
                            num_list = num_list[:len(num_list)-1]
                            num_list.append(Acc + elem)
                            LookForAcc = 0
                            break
                        LookForAcc = 0
                    if LookForFloat == 1:
                        if elem.islower():
                            element_list = element_list[:len(element_list)-1]
                            element_list.append(AccU + elem)
                            LookForFloat = 0
                            end = 1
                            LookForNumber = 1
                            continue
                        LookForFloat = 0
                    if not isfloat(elem) and LookForNumber == 1: 
                        num_list.append('1')
                        LookForNumber = 0
                    if elem.isupper():
                        element_list.append(elem)
                        AccU = elem
                        LookForFloat = 1
                        LookForNumber = 1
                        
                        end = 1
                    if isfloat(elem):
                        num_list.append(elem)
                        LookForNumber = 0
                        LookForAcc = 1
                        Acc = elem
                        end = 0
            if end == 1: 
                num_list.append('1')
                LookForNumber = 0
            if r == 0: 
                reac = pd.DataFrame([element_list, num_list])
                r+=1
            if r == 1: 
                prod = pd.DataFrame([element_list, num_list])
                r-=1            
                        
            return reac, prod
        
    def MW(self):
        try:
            for index, row in df.iterrows():
                if row['Symbol'] == data.atoms()[0][0][0] : print(row['AtomicMass'])
        except:
            print('Erorr in inlet element')
            
def isfloat(X):
    try:
        float(X)
        return True
    except:
        return False
        
        
                   
                
        


data = rxn( 1, reactants = ("NH3" , "B") , products =("C2H" ,"Co"), equa = True);
data.MW()
print(data.atom_sort())

