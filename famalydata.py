family_key = "Makarovs"
your_family_key = input("Family Key: ")
while your_family_key != family_key:
    your_family_key = input("Enter a valid key: ")

art_pas = "comp"
sas_pas = "moloko"
kat_pas = "dog"
gen_pas = "rabbit"
pas = input("Face Key: ")
info = []

if pas == art_pas:
    print("")
    print("Artem Makarov")
    print("9 years")
    print("Male")
    print("22 October 2013")
if pas == sas_pas:
    print("")
    print("Sasha Makarov")
    print("2 years")
    print("Male")
    print("3 September 2020")
if pas == kat_pas:
    print("")
    print("Kate Makarova")
    print("35 years")
    print("Female")
    print("20 April 1988")
if pas == gen_pas:
    print("")
    print("Family Owner")
    print("Gene Makarov")
    print("39 years")
    print("Male")
    print("16 March 1983")
