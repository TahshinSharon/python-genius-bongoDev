#Solution For  Exercises-1

Start
  │
  ▼
Get Name
  │
  ▼
Get Age
  │
  ▼
Get Developer Status
  │
  ▼
Is Age < 18?
  │
 ├── Yes → Tier 3: Guest
 │
 └── No
        │
        ▼
   Is Developer?
        │
    ├── Yes → Tier 1: Admin
    │
    └── No  → Tier 2: Standard
        │
        ▼
    Print Summary
        │
        ▼
       End

#Solution For Excercises-2

Start
  │
  ▼
Read Cluster Configuration
  │
  ▼
Get Active Nodes List
  │
  ▼
Initialize Counter = 0
  │
  ▼
Loop Through Active Nodes
  │
  ├── Node Found → Counter + 1
  ├── Node Found → Counter + 1
  ├── Node Found → Counter + 1
  ├── Node Found → Counter + 1
  └── Node Found → Counter + 1
  │
  ▼
Active Node Count = 5
  │
  ▼
Calculate Utilization
(5 / 8) × 100
  │
  ▼
62.5%
  │
  ▼
Print Audit Report
  │
  ▼
End

#Solution For Excercise-3

Start
  ↓
Receive instance_count, hourly_rate, budget_cap
  ↓
Calculate total_cost = instance_count × hourly_rate × 720
  ↓
Is total_cost > budget_cap?
       / \
     Yes  No
      |    |
Calculate   Return
exceeded    "APPROVED:
amount      Total Estimated Cost is $X."
      |
Return
"REJECTED:
Budget Exceeded by $X!"
      ↓
End

#Solution for Excercises-4:
Start
  ↓
Create raw_survey_inputs
  ↓
Create empty list sanitized_records = []
  ↓
For each string in raw_survey_inputs
  ↓
Remove leading/trailing spaces (.strip())
  ↓
Convert to lowercase (.lower())
  ↓
Append cleaned string to sanitized_records
  ↓
Repeat until all elements are processed
  ↓
Print raw_survey_inputs
  ↓
Print sanitized_records
  ↓
End
#Solution For Excercises-5
Start
  ↓
Initialize:
is_active = True
cpu_percent = 94.5
is_production = True
  ↓
Evaluate:
(not is_active)
      OR
(cpu_percent > 90.0 and is_production)
  ↓
False OR (True AND True)
  ↓
False OR True
  ↓
should_alert = True
  ↓
if should_alert?
   /      \
 Yes       No
  |         |
Print      Print
[ALERT]    [OK]
  ↓
 End