#Fill in the date and the name in the string

letter = ''' Dear <|Name|>
            You are selected!
            <|Date|> '''

print(letter.replace("<|Name|>","Yogiraj").replace("<|Date|>","20th August")) #What happended here is that first with one replace one string was created and with the other replace we replaced the Date in the new string that was earlier created. THis is called the chaining of the replace function.