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
if pas == sas_pas:
    print("")
    print("Sasha Makarov")
    print("2 years")
    print("Male")
if pas == kat_pas:
    print("")
    print("Kate Makarova")
    print("35 years")
    print("Female")
if pas == gen_pas:
    print("")
    print("Family Owner")
    print("Gene Makarov")
    print("39 years")
    print("Male")
print("Thank You!")
