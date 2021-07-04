import pandas as pd

class rxn:
    def __init__(self, i, reactants, products,eq):

        global a 
        self.reactants = reactants
        self.products = products
        self.eq = eq
        import pandas as pd
        global df;
        
        df = pd.read_csv('ElementData.csv')
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


        global elem
        LookForNumber = 0

        for comp in self.reactants:
            for elem in comp:
                if not isfloat(elem) and LookForNumber == 1: 
                    num_list.append('1')
                    LookForNumber = 0
                if elem.isupper():
                    element_list.append(elem)
                    LookForNumber = 1
               # if elem.islower():element_list.append(elem)
                if isfloat(elem):
                    num_list.append(elem)
                    LookForNumber = 0
        return pd.DataFrame([element_list, num_list])
    
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
        
        
                   
                
        


data = rxn( 1, reactants = ("C1H3") , products =("NH3" ,"C"), eq = True);
data.MW()
print(data.atom_sort())

