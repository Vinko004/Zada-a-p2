
def rekurzija(string):
    if len(string) == 0:
        return 
    else:
        print(string[-1])
        rekurzija(string[:-1])
        
string = input("Unesite string: ")

rekurzija(string)