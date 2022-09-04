############### Manually Enter Values & Graph Output ###############

def currv(c):
    a = float(c)
    round(a,1)
    if a==0.1:
        return ("#"*5)
    if a==0.2:
        return ("#"*9)
    if a==0.3:
        return ("#"*14)
    if a==0.4:
        return ("#"*20)
    if a==0.5:
        return ("#"*26)
    if a==0.6:
        return ("#"*31)
    if a==0.7:
        return ("#"*38)
    if a==0.8:
        return ("#"*41)
    if a==0.9:
        return ("#"*47)

def openv(o):
    a = float(o)
    round(a,1)
    if a==0.1:
        return ("#"*5)
    if a==0.2:
        return ("#"*9)
    if a==0.3:
        return ("#"*14)
    if a==0.4:
        return ("#"*20)
    if a==0.5:
        return ("#"*26)
    if a==0.6:
        return ("#"*31)
    if a==0.7:
        return ("#"*38)
    if a==0.8:
        return ("#"*41)
    if a==0.9:
        return ("#"*47)

def highv(h):
    a = float(h)
    round(a,1)
    if a==0.1:
        return ("#"*5)
    if a==0.2:
        return ("#"*9)
    if a==0.3:
        return ("#"*14)
    if a==0.4:
        return ("#"*20)
    if a==0.5:
        return ("#"*26)
    if a==0.6:
        return ("#"*31)
    if a==0.7:
        return ("#"*38)
    if a==0.8:
        return ("#"*41)
    if a==0.9:
        return ("#"*47)

def lowv(l):
    a = float(l)
    round(a,1)
    if a==0.1:
        return ("#"*5)
    if a==0.2:
        return ("#"*9)
    if a==0.3:
        return ("#"*14)
    if a==0.4:
        return ("#"*20)
    if a==0.5:
        return ("#"*26)
    if a==0.6:
        return ("#"*31)
    if a==0.7:
        return ("#"*38)
    if a==0.8:
        return ("#"*41)
    if a==0.9:
        return ("#"*47)

    
def cnsl_basedbarh():
    print("Current |",currv(currval))
    print("        |")
    print("        |")
    print("        |")
    print("Open    |",openv(openval))
    print("        |")
    print("        |")
    print("        |")
    print("High    |",highv(highval))
    print("        |")
    print("        |")
    print("        |")
    print("Low     |",lowv(lowval))
    print("        |")
    print("         __________________________________________________")
    print("              0.1       0.3        0.5       0.7       0.9 ")

print("-"*40)
currval =input("Enter The Current Value 0.1, 0.2, 0.3,..: ")
openval =input("Enter The Opening Value 0.1, 0.2, 0.3,..: ")
highval =input("Enter The High Value    0.1, 0.2, 0.3,..: ")
lowval  =input("Enter The Low Value     0.1, 0.2, 0.3,..: ")
print("_"*40)
#####Transversing Values#####



cnsl_basedbarh()
#######################\\#########################\\##################
