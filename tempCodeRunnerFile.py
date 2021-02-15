def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        v.set(total) 
        expression = "" 
    except: 
        v.set(" error ") 
        expression = "" 
