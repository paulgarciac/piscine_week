import sys

phrase = sys.argv[1]
#phrase = "A robot, must protect. its own existence! as long as such protection does not conflict with the First or Second Law"
maxChar = sys.argv[2]
#maxChar = 3

splited = phrase.split()

txt = ""

for word in splited:
    if len(word) > maxChar:
        txt = txt + word + " "
txt = txt[:-1]
txt = set(txt.punctuation)
txt = txt.split()
print(txt)

