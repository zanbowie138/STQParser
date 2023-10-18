import re
import os

def find_idx(arr, substring) -> int:
    for idx, line in enumerate(arr):
        if substring in line:
            return idx
    else:
        assert(False)


# Config
INPUT_FILEPATH = "res/33-48.txt"
OUTPUT_FILEPATH = "output/out.txt"

txt_arr = []
with open(INPUT_FILEPATH, "r") as f: 
    # Remove new lines, tabs, and other non-space whitespace in each line
    txt_arr = [re.sub("\n|\t|\v|\r|\f","",l) for l in f]

    # Remove array elements that are only whitespace or blank
    txt_arr = [i for i in txt_arr if i != "" and not i.isspace()]

    # Remove intro and outro
    txt_arr = txt_arr[6:-2]

txt = "\n".join(txt_arr)

sections = dict()
question_sections = txt.split("#")[1:]

output = ""

for section in question_sections:
    # First line: number
    # From "Be prepared to define the following terms." to "Applied Concepts" is vocabulary
    # From "Respond to the following prompts." to end is free response
    lines = section.split("\n")[:-2]
    output += "\n".join(lines) + "\n\n"

    # Get question number
    question_number = lines[0].split(":")[0]

    # Get all vocab lines
    vocab = [v[2:] for v in lines[find_idx(lines, "Be prepared to define")+1: find_idx(lines, "Applied Concepts")]]

    # Get all free response questions
    fr = lines[find_idx(lines, "Respond to the following prompts")+1:]

    

    
    


with open(OUTPUT_FILEPATH, "w") as f: 
    f.write(output)

# print(txt)