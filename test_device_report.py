# test_device_report.py
from device_report import generate_report

def test_report_runs_without_errors():
    devices = [
        {"name": "mac-001", "os": "14.4", "status": "compliant"},
        {"name": "mac-002", "os": "13.6", "status": "non-compliant"},
    ]
    # If this throws an exception, the test fails
    generate_report(devices)

def test_compliant_count():
    devices = [
        {"name": "mac-001", "os": "14.4", "status": "compliant"},
        {"name": "mac-002", "os": "14.4", "status": "compliant"},
        {"name": "mac-003", "os": "13.6", "status": "non-compliant"},
    ]
    compliant = [d for d in devices if d["status"] == "compliant"]
    assert len(compliant) == 2

def test_non_compliant_flagged():
    devices = [
        {"name": "mac-001", "os": "13.6", "status": "non-compliant"},
    ]
    non_compliant = [d for d in devices if d["status"] == "non-compliant"]
    assert len(non_compliant) == 1