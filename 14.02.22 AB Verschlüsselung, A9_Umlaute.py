def ohne_umlaute(text):
    neuer_text=str()
    for z in text:
        q=z
        if z=='Ä' or z=='ä':
            q='AE'
        elif z=='Ö' or z=='ö':
            q='OE'
        elif z=='Ü' or z=='ü':
            q='UE'
        elif z=='ß':
            q='SS'
            
        neuer_text += q
        
    return neuer_text
