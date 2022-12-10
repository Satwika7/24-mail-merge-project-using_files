#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
change_name = "[name]"
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    text_in_letter = letter.read()
    for each_name in names_list:
        changed_text=text_in_letter.replace(change_name,each_name.strip())
        with open(f"Output/ReadyToSend/{each_name.strip()}_letter.txt",mode="w") as output_letter:
            output_letter.write(changed_text)

