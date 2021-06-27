def rxn(i, reactants, products, eq):
    #i is the reaction number index for multiple reactions
    #Define lists
    atom = [];
    atom1 = [];
    #This loop will cycle through the input components and list, append them into the list
    for comp in reactants[0:]:
        atom.append(list(comp));
    
    #This loop will cycle through the output components and list, append them into the list

    for comp in products[0:]:
        atom1.append(list(comp));    
        
    #The output should give a list that contains the inputs and outputs with each seprated by atom
    #Chemical reaction should also be given as an output    
    return atom, atom1, eq, reactants[1]+ "->";



print(rxn( 1, reactants = ("CH4" , 2 * "O2") , products =("NH3" ,"C"), eq = True));

