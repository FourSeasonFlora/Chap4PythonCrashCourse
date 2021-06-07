favorite_numbers = list(range(1,30,2))
print (favorite_numbers)

family_members = input ("Enter family  members here: ")
family_member_confirm = f"\n The family members provided are: {family_members.title()}\n"

for family in family_members:
    print (family_member_confirm)




family_members = ['Mom', 'Dad', 'Brother', 'Sister']
for family in family_members:
    print (family)



family_members = input ("Enter family  members here: ")
family_member_confirm = f"\n The family members provided are: {family_members.title()}\n"
for family in family_member_confirm:
    print (family)



family_members = ['mom', 'dad', 'brother', 'sister']
for family in family_members:
    print (f"\n{family.title()}, is a person that can be in a family.")
    print (f"An important person in a family is {family.title()}.\n")

print ("Families are great!")