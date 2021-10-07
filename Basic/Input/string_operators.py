Lives = input("Enter the number of lives.")



EL = input("\n \n Please enter the energy level.")


SL = input("\n \n Please enter shield level")


print("\n \n Health has been set. \n \n")

Lives_Symbol = "♥"
SL_Symbol = "♦"
EL_Symbol = "♦"

#Because of the way the computer works it has to be Symbol first then variable

print(f"{Lives_Symbol * int(Lives)}")

print(f"{SL_Symbol * int(EL)}")

print(f"{EL_Symbol * int(SL)}")

#♥ 3


#♦ 4



