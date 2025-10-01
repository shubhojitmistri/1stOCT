#EXERCISE.1
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('yup'))

#EXERCISE.2
from itertools import permutations

perm = permutations([1, 2, 3])

for i in perm:
    print(i)

#EXERCISE.3 
from itertools import permutations

def unique_permutations(list_1, list_2):
    # If the first list is shorter than the second, swap them
    if len(list_1) < len(list_2):
        list_1, list_2 = list_2, list_1

    # Initialize an empty list to store the result
    result = []

    # Generate all permutations of the longer list taken len(list_2) at a time
    for perm in permutations(list_1, len(list_2)):
        # Create pairs of elements from 'perm' and 'list_2' using the zip function
        pairs = zip(perm, list_2)

        # Convert the pairs to a list
        list_pairs = list(pairs)

        # Extend the 'result' list with these permutations
        result.append(list(list_pairs))

    # Return the result as a list of lists, where each inner list is a list of tuples
    return result

list_1 = ["a", "b", "c", "d"]
list_2 = [1, 2, 3]
print(unique_permutations(list_1, list_2))

#EXERCISE.4
from itertools import permutations  
permu = permutations(['n','i','n','j','a'],2)  
print(permu)  
for p in list(permu):  
   print(p)