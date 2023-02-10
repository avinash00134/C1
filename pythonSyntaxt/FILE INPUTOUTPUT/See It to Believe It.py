my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()


# The open() Function
my_file = open('output.txt' , 'r+')



# Writing
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for value in my_list:
  my_file.write(str(value) + "\n")
  
my_file.close()



# Reading
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()


# Read between the line
my_file = open("text.txt","r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()




# PSA: Buffering Data
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print read_file.read()
read_file.close()



# The 'with' and 'as' Keywords
with open("text.txt", "w") as textfile:
  textfile.write("Success!")




# Try It Yourself
with open("text.txt") as my_file:
  pass




# Case Closed?
with open("text.txt", "w") as my_file:
  my_file.write("My Data!")
  
if not file.closed:
  file.close()

print my_file.closed



# DNA analysis
sample = ['Avinash','raj','manish']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i + 3) < len(dna):
      codons.append(dna[i:(i + 3)])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print("There were %d codon matches in %s. Further investigation should be done") %(num_matches, dna_sample)
  else:
    print("There were only %d codon matches in %s. As the dna test clears this suspect of any allegations they can be freed") % (num_matches, dna_sample)
    
is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')




# 