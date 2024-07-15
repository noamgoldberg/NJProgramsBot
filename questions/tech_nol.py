from consts import TECH_BIOTECH_NOL_PROGRAM

TECH_BIOTECH_NOL_QUESTIONS = [
    {
        "question": "Is your company's primary business the provision of a scientific process, product, or service?",
        "type": "radio",
        "key": "nol-1",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    },
    {
        "question": "Does your company own, have filed for, or have a license to use protected, proprietary intellectual property (e.g., a patent or registered copyright)?",
        "type": "radio",
        "key": "nol-2",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    },
    {
        "question": "Has your company had positive net operating income on either of its last two full-year income statements according to GAAP?",
        "type": "radio",
        "key": "nol-3",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "No")]
    },
    {
        "question": "Does your company have no more than 224 and at least one full-time employee working in New Jersey if incorporated or formed less than three years ago?",
        "type": "radio",
        "key": "nol-4",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    },
    {
        "question": "Does your company have no more than 224 and at least five full-time employees working in New Jersey if incorporated or formed more than three years but less than five years ago?",
        "type": "radio",
        "key": "nol-5",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    },
    {
        "question": "Does your company have no more than 224 and at least ten full-time employees working in New Jersey if incorporated or formed more than five years ago?",
        "type": "radio",
        "key": "nol-6",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    },
    {
        "question": "Does your company have financial statements for the two most recent full years of operation compiled, reviewed, or audited by an independent CPA firm and prepared according to US GAAP?",
        "type": "radio",
        "key": "nol-7",
        "options": ["Yes", "No"],
        "depends_on": [("industry", ("Technology", "Biotechnology"))],
        "eligible": [(TECH_BIOTECH_NOL_PROGRAM, "Yes")]
    }
]
