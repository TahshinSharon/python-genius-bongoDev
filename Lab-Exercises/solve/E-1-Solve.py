#Input Section
Name=input("Enter Your Name: ")
Age =int(input("Enter Your Age: "))
DevStatus=input("Are you a developer? (yes/no): ").lower()

#Logic Section
if Age < 18:
    tier = "Tier 3: Guest"
elif Age >= 18 and DevStatus == "yes":
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Access"

#Profile card using an f-string
print(f"""
----- Profile Configuration Summary -----
Name: {Name}
Age: {Age}
Developer: {DevStatus}
Assigned Clearance: {tier}
-----------------------------------------
""")