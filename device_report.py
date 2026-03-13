# device_report.py
# Simulates a CPE automation script — generates a basic fleet summary report

devices = [
    {"name": "mac-001", "os": "14.4", "status": "compliant"},
    {"name": "mac-002", "os": "13.6", "status": "non-compliant"},
    {"name": "mac-003", "os": "14.4", "status": "compliant"},
]

def generate_report(devices):
    print("=== Fleet Compliance Report ===")
    compliant = [d for d in devices if d["status"] == "compliant"]
    non_compliant = [d for d in devices if d["status"] == "non-compliant"]

    print(f"Total devices: {len(devices)}")
    print(f"Compliant: {len(compliant)}")
    print(f"Non-compliant: {len(non_compliant)}")

    if non_compliant:
        print("\nDevices requiring attention:")
        for d in non_compliant:
            print(f"  - {d['name']} (macOS {d['os']})")

if __name__ == "__main__":
    generate_report(devices)