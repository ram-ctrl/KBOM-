import psycopg2
import json

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="kbom_db",
    user="your_username",
    password="your_password",
    host="localhost",  # or your DB host
    port="5432"  # default PostgreSQL port
)
cursor = conn.cursor()

# Load KBOM JSON data (in practice, this could be fetched from a file or API)
kbom_data = '''{
  "image": {
    "name": "my-app:latest",
    "digest": "sha256:d8f7c3b881db42b9c1df7c634ecb2d34f2b3aeb87cc4a19fa00d62f0bd52f73d",
    "tag": "latest"
  },
  "components": [
    {
      "name": "flask",
      "version": "2.0.3",
      "license": "BSD-3-Clause",
      "cve": [
        {
          "id": "CVE-2021-12345",
          "severity": "high",
          "description": "Remote code execution vulnerability in flask",
          "recommended_fix": "Upgrade flask to 2.0.4"
        }
      ]
    },
    {
      "name": "nginx",
      "version": "1.19",
      "license": "GPL-2.0",
      "cve": [
        {
          "id": "CVE-2021-6789",
          "severity": "critical",
          "description": "Memory leak vulnerability in nginx",
          "recommended_fix": "Upgrade nginx to 1.19.1"
        }
      ]
    }
  ],
  "vulnerabilities": [
    {
      "cve_id": "CVE-2021-12345",
      "severity": "high",
      "component": "flask",
      "fix": "Upgrade flask to version 2.0.4"
    },
    {
      "cve_id": "CVE-2021-6789",
      "severity": "critical",
      "component": "nginx",
      "fix": "Upgrade nginx to version 1.19.1"
    }
  ]
}'''

# Parse the KBOM data
kbom = json.loads(kbom_data)

# Insert image data
image_data = kbom["image"]
cursor.execute("""
    INSERT INTO images (name, digest, tag) 
    VALUES (%s, %s, %s) RETURNING id;
""", (image_data["name"], image_data["digest"], image_data["tag"]))
image_id = cursor.fetchone()[0]

# Insert components and their CVEs
for component in kbom["components"]:
    cursor.execute("""
        INSERT INTO components (name, version, license)
        VALUES (%s, %s, %s) RETURNING id;
    """, (component["name"], component["version"], component["license"]))
    component_id = cursor.fetchone()[0]
    
    for cve in component["cve"]:
        cursor.execute("""
            INSERT INTO cves (cve_id, severity, description, recommended_fix, component_id)
            VALUES (%s, %s, %s, %s, %s);
        """, (cve["id"], cve["severity"], cve["description"], cve["recommended_fix"], component_id))

# Insert vulnerabilities
for vulnerability in kbom["vulnerabilities"]:
    cursor.execute("""
        INSERT INTO vulnerabilities (cve_id, severity, component, fix)
        VALUES (%s, %s, %s, %s);
    """, (vulnerability["cve_id"], vulnerability["severity"], vulnerability["component"], vulnerability["fix"]))

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()
