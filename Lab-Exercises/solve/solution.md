#Solution For  Exercises-1

Collect User Information
        │
        ▼
     Check Age
        │
   Age < 18 ?
        │
   ├── Yes → Tier 3: Guest
   │
   └── No
         │
         ▼
  Check Developer Status
         │
   Developer?
         │
   ├── Yes → Tier 1: Admin Infrastructure Access
   │
   └── No  → Tier 2: Standard Executive Access
         │
         ▼
   Generate Summary
         │
         ▼
    Display Result

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