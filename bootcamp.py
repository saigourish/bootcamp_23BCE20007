x=True
while(x):
    x=input("Hello ,how can I help you regarding ipl team information !")
    if("CSK" in x):
        print("CSK has MS Dhoni as capitan")
    elif("GT" in x):
        print("GT has Shubman Gill ac capitan")
    elif("DC" in x):
        print("DC has Rishabh Pant as capitan")
    elif("KKR" in x):
        print("KKR has Shreyas Iyer as capitan")
    elif("PK" in x):
        print("PK has Shikkar Dhawan as capitan")
    elif("break" or "quit" in x):
        x = False
    else:
        print("Information you asked is not about IPL")