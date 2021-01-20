#String -> List
def perm_gen_lex(a): 
    """Generates a list of all possible permutations of a string and 
    orders it in lexicographic order"""

    if len(a) <= 1:
        if len(a) == 0:
            return []
        return [a]

    final_list = []

    for char in a:
        simpler_string = a.replace(char,'') #removes a char to create a shorter string

        for perm in perm_gen_lex(simpler_string): #goes through each permutation
            final_list.append(char + perm) #adds back the original character and appends into list
    return final_list

 