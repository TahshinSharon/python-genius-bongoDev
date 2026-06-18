#Solution For  Exercises-1

1. Collect User Information

The system asks the user for:

Their name
Their age
Whether they are a developer (yes or no)
2. Convert Age to a Number

Since user input is received as text, the age is converted into an integer so mathematical comparisons can be performed.

3. Check the User's Age

The first decision is based on age:

If the user is younger than 18, they are automatically assigned:
Tier 3: Guest Access
If the user is 18 or older, the program proceeds to the next check.
4. Check Developer Status

For users who are 18 or older:

If they are a developer, they receive:
Tier 1: Admin Infrastructure Access
If they are not a developer, they receive:
Tier 2: Standard Executive Access
5. Generate Profile Summary

After determining the correct tier, the system creates a personalized summary containing:

Name
Age
Developer status
Assigned clearance tier
6. Display the Result

The completed profile summary is shown to the user.