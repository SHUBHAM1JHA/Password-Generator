import random

file=open('pwd.txt',"a")
char = "aBcDeFgHiJkLmNoPqRsTuVwXyZ!@#$1234567890"
true=False
y="y"
Y="Y"
special_char="!@#$()_" #7
numbers="1234567890"

capital_alphas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
capandnum="ABCDEFGHIJKL1234567890MNOPQRSTUVWXYZ"
capandsym="ABCDEFGHI!@#$()_JKLMNOPQRSTUVWXYZ"
capandnumandsym="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

small_alphas="abcdefghijklmnopqrstuvwxyz"
smlandnum="abcdefghijklmn1234567890opqrstuvwxyz"
smlandsym="abcdefghijklmno!@#$()_pqrstuvwxyz"
smlandnumandsym="abcdefghijk1234567890lmnopqrst!@#$()_uvwxyz"

rand_alphas="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"



def gp(x):
    pwd = "".join(random.sample(char, x))
    return pwd


def write(na,gppp):
        file.write("    "+nam+"::: "+gppp+'\n\n')
        file.close()

nam=input(" Provide a name for password:\n\t--> ")
len=input("\n Length of password:\n\t--> ")
length=int(len)
l=length

true=True

while true:
    input("\n\tPress Enter to generate new password")
    gpp=gp(length)
    print("\n\t"+gpp)
    inp=input("\n Is it perfect? [y/n] <| You can also press enter for no |>\n\t-->")
    if inp==y or inp==Y:
        file.write("    "+nam+"::: "+gpp+'\n\n')
        file.close()
        print(f"\n\t\tDone! Saved password '{gpp}' for {nam}.\n\n")
        exit=input(" Press enter to exit.")
        break
    else:
        continue
