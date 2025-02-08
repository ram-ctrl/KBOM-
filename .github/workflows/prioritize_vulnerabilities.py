import json
import csv

# Load Trivy scan report
with open("vulnerability-report.json", "r") as file:
    trivy_data = json.load(file)

# Load CISA KEV list
with open("cisa_kev_cves.txt", "r") as file:
    cisa_kev_cves = {line.strip() for line in file}

# Load EPSS scores
epss_scores = {}
with open("epss_scores.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        cve, epss_score = row[0], float(row[2])
        epss_scores[cve] = epss_score

# Classify vulnerabilities
prioritized_vulnerabilities = {"HIGH": [], "MEDIUM": [], "LOW": []}

for result in trivy_data["Results"]:
    for vuln in result.get("Vulnerabilities", []):
        cve_id = vuln["VulnerabilityID"]
        
        if cve_id in cisa_kev_cves:
            priority = "HIGH"
        elif epss_scores.get(cve_id, 0) > 0.75:
            priority = "MEDIUM"
        else:
            priority = "LOW"
        
        vuln["Priority"] = priority
        prioritized_vulnerabilities[priority].append(vuln)

# Save results
with open("prioritized_vulnerabilities.json", "w") as file:
    json.dump(prioritized_vulnerabilities, file, indent=4)

print("✅ Prioritization complete! Check 'prioritized_vulnerabilities.json'")
