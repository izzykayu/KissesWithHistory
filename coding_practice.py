import datetime
from functools import reduce

# empty list to hold the contents of the file
lst = []
with open('cleaned_GPMDB_table.tsv', 'r') as f:
    # move the file past the header line as we do not need it
    f.readline()
    # go through every line in the file
    for line in f:
        # strip the line endings(this removes the \n from the end of each line) then split the line on the \t
        temp = line.strip().split('\t')
        # check that there are the correct number of columns in the row otherwise raise an exception
        if len(temp) == 23:
            lst.append(temp)
        else:
            raise Exception('There are not 23 columns in line {} of the file.'.format(len(lst) + 1))


# function used by map to create a dictionary containing the date from the row and the taxons
def extract(row):
    return {'date': datetime.datetime.strptime(row[1], "%Y:%m:%d:%H:%M:%S").date(), 'taxon': row[22]}


# function to reduce the dictionary to a dictionary of counts
def reduce_dict(counts_dictionary, taxon_dictionary):
    # each row contains a comma separated list of taxons, split on the comma to count each taxon separately
    for value in taxon_dictionary['taxon'].split(','):
        # remove any white spaces so that ' human' will be the same as 'human' etc...
        value = value.strip()
        # increment the count for the taxon or initialize it to 0 and add 1 if it does not exist
        counts_dictionary[value] = counts_dictionary.get(value, 0) + 1
    # return the updated counts dictionary
    return counts_dictionary

# apply the extract function using map to the list of rows from the file
date_taxon_list = map(extract, lst)
# filter the mapped data so that only entries within the specified dates kept
date_taxon_2010_list = filter(
    lambda row: row['date'].year == 2010 and 6 <= row['date'].month <= 9, date_taxon_list)

# reduce the filtered list of dictionaries down to a single dictionary containing a count for each taxon
counts = reduce(reduce_dict, date_taxon_2010_list, {})
# find the taxon with the highest count and print it
print(max(counts.items(), key=lambda k: k[1]))


import masses	# good practice to keep constants in a separate module


list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}]

# Iterative Solution
for protein_dict in list_of_protein_dicts:
    valid = True	# assume valid, unless you find evidence when iterating
    running_mass = masses.mass_h2o
    for char in protein_dict['seq'].upper():
        if char in masses.aa_masses:
            running_mass += masses.aa_masses[char]
        else:
            valid = False
            print(protein_dict['seq'], ' is invalid')
            break
    if valid:	# an alternate way would be to use for-else structure (see solution for ques 1)
        mz = running_mass/protein_dict['ch']
        print('m/z of ', protein_dict['seq'], ': ', mz)
# dictionary used for reverse complementing
reverse_comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
# list to hold unique sequences
list_of_sequences = []

while True:
    # get input from the user
    input_sequence = input('Enter DNA sequence or done to exit: ')
    # stop getting input if the user inputs done
    if input_sequence == 'done':
        break
    # check that all the characters are valid
    reversed_seq = ''
    for char in input_sequence[::-1]:
        # I create a variable for the upper case character as I use the upper case multiple times
        upper_char = char.upper()
        # if a character is invalid then break
        if upper_char not in ['A', 'C', 'G', 'T']:
            print('{} is an invalid character'.format(char))
            break
        comp_upper_char = reverse_comp[upper_char]
        # an 'inline if' - these are if statements for assigning variables
        # it will use the uppercase char if the original is uppercase otherwise it will use lowercase
        reversed_seq += comp_upper_char if char.isupper() else comp_upper_char.lower()
    # this will only execute if the the break was not called, which means the sequence was valid
    else:
        if reversed_seq not in list_of_sequences:
            print('{} has been added to the list'.format(reversed_seq))
            list_of_sequences.append(reversed_seq)
        else:
            print('{} is already in list'.format(reversed_seq))

# --PRE COMPUTE VALUES NEEDED FOR OUTPUT--
# Dictionary which keeps count of each nucleotide
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
number_of_sequences = len(list_of_sequences)
# variable to count the total number of nucleotides
length_of_all_sequences = 0
# iterate over each sequence and add its length to length_of_all_sequences
for sequence in list_of_sequences:
    length_of_all_sequences += len(sequence)
    # Update the counts for each nucleotide for each sequence
    for key in counts:
        counts[key] += sequence.upper().count(key)

# --OUTPUT CALCULATED VALUES--
print('Sequences')
print('\t' + ', '.join(list_of_sequences))
print('--* Statistics *--')
print('\tfrequencies:')
for key, value in counts.items():
    print('\t\t {}/{}\t: {}/{}'.format(key, key.lower(), value, length_of_all_sequences))
print('\tnumber of sequences:')
print('\t\t', number_of_sequences)
print('\taverage number of characters per sequence:')
print('\t\t{:.3f}'.format(length_of_all_sequences / number_of_sequences))
