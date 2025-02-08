import json

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def merge_data(kbom_file, vuln_file):
    kbom_data = load_json(kbom_file)
    vuln_data = load_json(vuln_file)

    for component in kbom_data.get("artifacts", []):
        component_name = component.get("name", "Unknown")
        component["vulnerabilities"] = [
            vuln for vuln in vuln_data.get("Results", [])
            if component_name in vuln.get("Target", "")
        ]
    return kbom_data

backend_data = merge_data("backend-kbom.json", "backend-vulnerabilities.json")
frontend_data = merge_data("frontend-kbom.json", "frontend-vulnerabilities.json")

final_kbom = {
    "backend": backend_data,
    "frontend": frontend_data
}

with open("kbom.json", "w") as output_file:
    json.dump(final_kbom, output_file, indent=4)

print("Merged KBOM saved to kbom.json")
