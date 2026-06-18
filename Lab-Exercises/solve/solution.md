# Python Exercises - Solution Flows

This document contains the flow descriptions for Exercises 1–5. Each section explains the logic used in the solution and provides a flow diagram to visualize the execution process.

---

## Exercise 1: User Access Tier Classification

### Description

This program determines a user's access tier based on their age and whether they are a developer.

- Users under 18 are assigned **Tier 3: Guest**.
- Adult developers are assigned **Tier 1: Admin**.
- Adult non-developers are assigned **Tier 2: Standard**.

### Solution Flow

```text
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
            ┌─────┴─────┐
           Yes          No
            │            │
            ▼            ▼
      Tier 3: Guest  Is Developer?
            │       ┌─────┴─────┐
            │      Yes          No
            │       │            │
            │       ▼            ▼
            │  Tier 1: Admin  Tier 2: Standard
            │       │            │
            └───────┴────────────┘
                    │
                    ▼
              Print Summary
                    │
                    ▼
                   End
```

---

## Exercise 2: Cluster Utilization Audit

### Description

This program reads cluster information, counts active nodes, and calculates the percentage of resource utilization.

### Solution Flow

```text
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
   ┌──────────┼──────────┐
   │          │          │
Node +1    Node +1   ... Node +1
   │          │          │
   └──────────┼──────────┘
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
```

---

## Exercise 3: Deployment Budget Optimizer

### Description

This program estimates monthly deployment costs and determines whether the cost is within the specified budget.

- If the cost exceeds the budget, deployment is **rejected**.
- Otherwise, deployment is **approved**.

### Solution Flow

```text
                    Start
                      │
                      ▼
  Receive instance_count, hourly_rate, budget_cap
                      │
                      ▼
  Calculate total_cost = instance_count × hourly_rate × 720
                      │
                      ▼
            Is total_cost > budget_cap?
              ┌────────┴────────┐
             Yes                No
              │                  │
              ▼                  ▼
     Calculate exceeded     Return "APPROVED:
          amount            Total Estimated
              │             Cost is $X."
              ▼                  │
     Return "REJECTED:           │
     Budget Exceeded             │
     by $X!"                     │
              │                  │
              └────────┬─────────┘
                       ▼
                      End
```

---

## Exercise 4: Profile Text Normalization Pipeline

### Description

This program cleans survey data by:

- Removing leading and trailing spaces.
- Converting all text to lowercase.
- Storing cleaned values into a new list.

### Solution Flow

```text
                Start
                  │
                  ▼
       Create raw_survey_inputs
                  │
                  ▼
  Create empty list sanitized_records = []
                  │
                  ▼
   For each string in raw_survey_inputs
                  │
                  ▼
   Remove leading/trailing spaces (.strip())
                  │
                  ▼
       Convert to lowercase (.lower())
                  │
                  ▼
   Append cleaned string to sanitized_records
                  │
                  ▼
    Repeat until all elements are processed
                  │
                  ▼
        Print raw_survey_inputs
                  │
                  ▼
        Print sanitized_records
                  │
                  ▼
                 End
```

---

## Exercise 5: System Alert Flag Evaluator

### Description

This program evaluates system health and decides whether an emergency alert should be triggered.

An alert is raised if:

- The server is inactive, **OR**
- CPU usage exceeds 90% **AND** the environment is production.

### Solution Flow

```text
                Start
                  │
                  ▼
            Initialize:
          is_active = True
         cpu_percent = 94.5
        is_production = True
                  │
                  ▼
              Evaluate:
            (not is_active)
                  OR
   (cpu_percent > 90.0 and is_production)
                  │
                  ▼
        False OR (True AND True)
                  │
                  ▼
            False OR True
                  │
                  ▼
         should_alert = True
                  │
                  ▼
           if should_alert?
            ┌─────┴─────┐
           Yes          No
            │            │
            ▼            ▼
      Print [ALERT]  Print [OK]
            │            │
            └─────┬──────┘
                  ▼
                 End
```

---

## Summary

| Exercise   | Topic                          |
| ---------- | ------------------------------ |
| Exercise 1 | Conditional Statements         |
| Exercise 2 | Loops and Arithmetic           |
| Exercise 3 | Functions and Return Values    |
| Exercise 4 | Strings, Lists, and Loops      |
| Exercise 5 | Boolean Logic and Conditionals |

These exercises demonstrate fundamental Python concepts commonly used in real-world software and automation workflows.
