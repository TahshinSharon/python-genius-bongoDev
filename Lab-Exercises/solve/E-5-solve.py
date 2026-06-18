
is_active = False
cpu_percent = 94.5
is_production = False

should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")