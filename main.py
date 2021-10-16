#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []
template = ""

with open("./input/names/invited_names.txt", mode="r") as names:
    l = names.readlines()
    for n in l:
        name_list.append(n.rstrip("\n"))


with open("./input/letters/starting_letter.txt", mode="r") as f:
    template = f.read()


for n in name_list:
    letter = template.replace("[name]", n)
    with open("./output/readytosend/" + n + ".txt", mode="w") as f:
        f.write(letter)



