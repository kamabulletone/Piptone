

def f21(x):
    if (x[0] == "slash"):
        if (x[2] == 2009):
            if (x[3] == 2015):
                return 0
            elif (x[3] == 1983):
                if (x[4] == "flux"):
                    return 1
                elif (x[4] == "qmake"):
                    return 2
            elif (x[3] == 1988):
                if (x[4] == "flux"):
                    return 3
                elif (x[4] == "qmake"):
                    return 4
        elif (x[2] == 2005):
            return 5
    elif (x[0] == "frege"):
        if (x[1] == "vue"):
            if (x[3] == 2015):
                if (x[2] == 2009):
                    return 6
                elif (x[2] == 2005):
                    return 7
            elif (x[3] == 1983):
                return 8
            elif (x[3] == 1988):
                return 9
        elif (x[1] == "red"):
            return 10
        elif (x[1] == "tex"):
            return 11
    elif (x[0] == "sql"):
        return 12


print(f21(["frege","vue",2009,2015,"flux"]))

print(f21(["frege","tex",2005,2015, "flux"]))