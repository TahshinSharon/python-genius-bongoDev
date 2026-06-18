cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": [
        "10.0.1.15",
        "10.0.1.16",
        "10.0.1.17",
        "10.0.1.18",
        "10.0.1.19"
    ]
}

def calculate_capacity(config):
    active_count=0
    
    for node in config["active_nodes"]:
        active_count+=1
        utilization=(active_count/config["total_max_slots"])*100

    # Print summary report
    print(f"""
Cluster Audit Report
--------------------
Cluster Name: {config['cluster_name']}
Total Max Slots: {config['total_max_slots']}
Active Nodes: {active_count}
Utilization: {utilization:.2f}%
""")

# Execute the function
calculate_capacity(cluster_config)