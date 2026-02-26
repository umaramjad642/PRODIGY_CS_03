Password Complexity Checker

Prodigy InfoTech - Cyber Security Internship | Task 03

A Python-based security tool designed to assess the strength of passwords using pattern matching. This application helps users understand password entropy and ensures credentials meet modern security standards to mitigate brute-force risks.

🚀 Key Features
* Strict Length Validation: Enforces a secure policy requiring passwords to be between 8 and 16 characters.
  
* Complexity Analysis: Uses Regular Expressions (RegEx) to detect the presence of:
  *  Uppercase letters (A-Z)
  *   Lowercase letters (a-z)
  *  Nmerical digits (0-9)
  *  Special characters (e.g., !, @, #, $)
* Dynamic Feedback: Provides instant ratings (Weak, Medium, Strong) based on character variety.
* Interactive CLI: Includes a continuous loop for testing multiple passwords and error handling for invalid inputs.

🛠️ How It Works

The tool evaluates passwords by checking for four distinct character "types." A higher variety of types results in a higher complexity score.
📝 Usage Examples| Input Password | Strength | Reason |
| Input Password | Strength | Reason |
| :--- | :--- | :--- |
| `p@ss1` | **Invalid** | Too short (under 8 characters). |
| `Secure!2026` | **Strong** | Meets all criteria. |


📋 Quick Start
* Clone or Copy: Save the script as password_checker.py.
* Run: Execute the script using:
 ### 🚀 How to Run
To run this tool on your local machine, use the following commands:

```bash
# Bash
python password_checker.py
```
* Evaluate: Follow the on-screen prompts to test your password strength.

🛡️ Cybersecurity RelevanceIn my role as a SOC Analyst and as a BSCS student, I recognize that weak credentials are a primary vector for unauthorized access. This tool simulates the backend security logic used by enterprises to enforce robust Identity and Access Management (IAM) policies.
