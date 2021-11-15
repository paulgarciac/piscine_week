t = (21, 42, 21, 45)

txt = ''
for i in t:     
    txt = txt + str(i) + ", "
txt = txt[:-2]

print(f"The {len(t)} numbers are: {txt}")
