# Kubernetes Bill of Materials (KBOM) Project

## 1. Introduction & Understanding KBOM
- What is KBOM (Kubernetes Bill of Materials), and why is it important?  
- How does KBOM help in vulnerability management for Kubernetes environments?  
- What are the key components of a KBOM report?  

## 2. Tools Overview
- What are the features and functionalities of Trivy, Syft, and OWASP Dependency-Track?  
- How does each tool contribute to the KBOM generation process?  
- How do these tools integrate to create a comprehensive vulnerability and dependency report?  

## 3. KBOM Schema & Structure
- What is the KBOM schema as defined by Rad Security?  
- What are the key fields in a KBOM schema (e.g., component name, version, CPE, dependencies, vulnerabilities)?  
- How should the KBOM schema be structured in JSON or YAML format?  

## 4. KBOM Generation Process
- How to generate an SBOM using Syft?  
  - What command should be used to generate an SBOM in different formats (JSON, CycloneDX)?  
  - How can Syft output be enhanced with metadata and dependency relationships?  

- How to scan images using Trivy?  
  - What command should be used to scan for vulnerabilities in Kubernetes container images?  
  - How to export vulnerability data in JSON format for further processing?  

- How to integrate SBOM and vulnerability data into OWASP Dependency-Track?  
  - What are the steps to set up OWASP Dependency-Track?  
  - How to use its API to import SBOMs and vulnerability reports?  

## 5. Vulnerability Analysis & Prioritization
- How to filter vulnerabilities using CISA KEV (Known Exploited Vulnerabilities)?  
- How to evaluate vulnerabilities based on the Exploit Prediction Scoring System (EPSS)?  
- How to define the prioritization logic using CISA KEV and EPSS scores?  

## 6. Enhancing KBOM with CPE Information
- What is Common Platform Enumeration (CPE), and how does it help in vulnerability tracking?  
- How to extract and associate CPE identifiers with each component?  
- How to enhance the KBOM output with CPE details?  

## 7. Dependency Mapping & Relationship Visualization
- How to structure dependencies in a tree format?  
- How to represent component relationships in KBOM output?  
- What tools can be used to visualize dependency trees (e.g., Graphviz, D3.js)?  
- How to highlight vulnerable components and their associated CVEs in a visual format?  

## 8. Sample Output & JSON Structure
- What should the final KBOM output look like in JSON format?  
- How to combine:  
  - Component details (name, version, CPE)  
  - Vulnerability details (CVE, severity, exploitability, KEV, EPSS score)  
  - Dependency relationships  
- How to ensure the output is structured and easy to analyze?  

## 9. Automation & Integration
- How to automate the KBOM generation process in a CI/CD pipeline?  
- How to schedule regular vulnerability scans using these tools?  
- How to integrate KBOM with security dashboards for continuous monitoring?

- # KBOM Security Pipeline 🚀

This repository automates Software Bill of Materials (SBOM) generation, vulnerability scanning, and security tracking for containerized applications.

## 📌 Features
✅ Generates **SBOM** using Syft  
✅ Scans vulnerabilities using **Trivy**  
✅ Uploads reports to **OWASP Dependency-Track**  
✅ Integrates with **GitHub Actions**  

## 📌 How to Run Locally?
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/kbom-security-pipeline.git
   cd kbom-security-pipeline


