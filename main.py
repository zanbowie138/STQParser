import re

# Config
INPUT_FILEPATH = "res/49-64.txt"
OUTPUT_FILEPATH = "output/out.txt"

print(f"Reading {INPUT_FILEPATH}...")

txt_arr = []
with open(INPUT_FILEPATH, "r") as f: 
    # Remove new lines, tabs, and other non-space whitespace in each line
    txt_arr = [re.sub("\n|\t|\v|\r|\f","",l) for l in f]

    # Remove array elements that are only whitespace or blank
    txt_arr = [i for i in txt_arr if i != "" and not i.isspace()]

    # Remove intro and outro lines
    txt_arr = txt_arr[6:-2]

txt = "\n".join(txt_arr)

with open("debug/debug.txt", "w") as f: 
    f.write(txt)

print("Created file without whitespace!")

sections = dict()

# Iterate through file, going one entire stq topic at a time
# First, finds the #[NUMBER]:, and then takes all the characters, until the next instance of #[NUMBER]:
for section in re.findall('#..:[\s\S]*?(?=#..:|$)', txt):
    # First line: number
    # From "Be prepared to define the following terms." to "Applied Concepts" is vocabulary
    # From "Respond to the following prompts." to underscores is free response

    # Split stq section into seperate lines
    lines = section.split("\n")

    # Get question number
    question_number = lines[0].split(":")[0][1:]

    # Get all vocab lines
    # Starts after "Be prepared to define...\n" and gets all text until "\nApplied Concepts"
    vocab = [v[2:] for v in re.search('Be prepared to define.*\n([\s\S]*?)\nApplied Concepts', section).group(1).split("\n")]

    # Get all free response questions
    # Starts after "Respond to the...\n" and captures all text until the end, not including trailing underscores
    fr = re.search("Respond to the.+\n([\s\S]*?)_*$", section).group(1).split("\n")

    # Add into dictionary
    # sections {
    #   [NUMBER] {
    #       "vocab" = {}
    #       "fr" = {}
    #   }
    # }
    sections[question_number] = dict(vocab = vocab, fr = fr)

print("Created dictionary!")

# TODO: Implement whatever you want with the dictionary

# Example output (for debug purposes)
output = ""

for topic_num in sections:
    output += f'STQ Topic #{topic_num}\n\n'
    output += "\n".join(sections[topic_num]["vocab"]) + "\n\n"
    output += "\n".join(sections[topic_num]["fr"]) + "\n\n\n"

with open(OUTPUT_FILEPATH, "w") as f: 
    f.write(output)

print("Wrote output file to " + OUTPUT_FILEPATH)