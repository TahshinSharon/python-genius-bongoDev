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