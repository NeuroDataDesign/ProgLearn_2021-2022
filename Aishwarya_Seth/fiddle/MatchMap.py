#Sample association: 
#    Out of 5 red balls and 7 blue balls, & 5 balls being selected, find probability distribution of number of red balls
    
#Idk about the math also, this is literally a random example that I made up. 

match_mapping = {} 

def nCr(n, r):
 
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res


def retrieve_mapping(num_matches):
    if num_matches in match_mapping.keys():
        return match_mapping[num_matches]
    else:
        #Calculate probability of picking matches out of say, 5 nodes in the layer 
        #This section + parameters will vary according to which algorithm we settle on 
        match_mapping[num_matches] = nCr(5, num_matches) * nCr(7, 12 - num_matches) / nCr(12,5)


print("Dictionary is updated whenever a new value is encountered - proobability associated is calculated \
and appended to the dictionary")
print("Retrieving value for Value not in Dictionary")
print("Output suppressed: final dictionary shown on terminal, created for inputs 1 to 5")
for i in range(1,6):
    retrieve_mapping(i)


print("Created Dictionary: ", match_mapping)
print("Retrieving Mapping for an Existing Value: ", retrieve_mapping(1))