'''colors = {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
colors["black"] = '#000000'
colors["white"] = '#FFFFFF'
colors["purple"] = '#800000'
colors["aqua"] = '#00FFFF'
colors["yellow"] = '#FFFF00'
print(colors)'''


colors = {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
colors_2 = {'black':'#000000', 'white':'#FFFFFF' , 'purple':'#800000' , 'aqua':'#00FFFF' , 'yellow':'#FFFF00'}
colors.update(colors_2)
print(colors)
