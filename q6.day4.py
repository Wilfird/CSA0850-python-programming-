def removeChar(s, c) :
    counts = s.count(c)
    s = list(s)
    while counts :
        counts -= 1
        s = '' . join(s)
    print(s) 
    if name == '_main_' :
       s = "geeksforgeeks"
    removeChar(s,'g')
