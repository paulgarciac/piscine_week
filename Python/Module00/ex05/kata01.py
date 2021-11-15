languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

txt = ''
for key in languages:     
    txt = txt + key + " was created by " + languages[key] + f"\n"
print(txt[:-3])