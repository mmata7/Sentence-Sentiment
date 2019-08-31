with open("C:/File Location" ,"r") as B: #Text File Being Analyzed#
        text = B.read()
        text = text.replace("\n", " ")
        text = text.replace('-', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace(',', '')
        text = text.replace('[', '')
        text = text.replace(']', '')
        text = text.replace(':', '')
        text = text.replace(';', '')
        text = text.replace("'s", '')
        text = text.replace("“",'')
        text = text.replace("”",'')
        text = text.replace("?",'.')
        text = text.replace("!",'.')
        text = text.replace(text, text.lower())
        text = text.split(". ")
        B = text


with open("C:/File Location", "r") as P: #Positive Sentiment Word File#
        text = P.read()
        text = text.replace("\n", " ")
        text = text.split(' ')
        P = text

with open("C:/File Location", "r") as N: #Negative Sentiment Word File#
        text = N.read()
        text = text.replace("\n", " ")
        text = text.split(' ')
        N = text



def Count():
    counts = []
    line = 0

    for line in B:
        count = 0
        C = line.split(" ")

        for i in N:
            if i in C:
                count -= 1

        for i in P:
            if i in C:
                count += 1

        Pos = 0
        Neg = 0
        Neu = 0

        if count < 0:
            count = 'Negative'
            counts.append(str(count))

        elif count > 0:
            count = "Positive"
            counts.append(str(count))

        else:
            count = "Neutral"
            counts.append(str(count))

    Pos = 0
    Neg = 0
    Neu = 0
    for h in counts:
        if h == 'Positive':
            Pos += 1
        elif h == 'Negative':
            Neg += 1
        else:
            Neu +=1

    print("Positive:", Pos)
    print("Negative:", Neg)
    print("Neutral:", Neu)
    print("Total:", Neu + Pos + Neg)


Count()
