class Color:
    def getANSI(textColor, textStyle, bgColor):
        e = "\033[1;31;40m"
        tc = textColor.upper()
        ts = textStyle.upper()
        bc = bgColor.upper()
        if(tc=="BLACK"):
            tcc = 30
        elif(tc=="RED"):
            tcc = 31
        elif(tc=="GREEN"):
            tcc = 32
        elif(tc=="YELLOW"):
            tcc = 33
        elif(tc=="BLUE"):
            tcc = 34
        elif(tc=="PURPLE"):
            tcc = 35
        elif(tc=="CYAN"):
            tcc = 36
        elif(tc=="WHITE"):
            tcc = 37
        else:
            print(f"{e} Invalid Text Color at '{tc}' ")
        if(bc=="BLACK"):
            bcc = 40
        elif(bc=="RED"):
            bcc = 41
        elif(bc=="GREEN"):
            bcc = 42
        elif(bc=="YELLOW"):
            bcc = 43
        elif(bc=="BLUE"):
            bcc = 44
        elif(bc=="PURPLE"):
            bcc = 45
        elif(bc=="CYAN"):
            bcc = 46
        elif(bc=="WHITE"):
            bcc = 47
        else:
            print(f"{e} Invalid Background Color at '{bc}' ")
        if(ts=="NORMAL"):
            tsc = 0
        elif(ts=="BOLD"):
            tsc = 1
        elif(ts=="UNDERLINE"):
            tsc = 2
        elif(ts=="NEGATIVE1"):
            tsc = 3
        elif(ts=="NEGATIVE2"):
            tsc = 4
        else:
            print(f"{e} Invalid Style at '{ts}' ")
        try:
            return f"\033[{tcc};{tsc};{bcc}m"
        except Exception as e
            exit()
