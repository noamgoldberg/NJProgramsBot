from consts import ASPIRE_PROGRAM

ASPIRE_QUESTIONS = [
    {
        "question": "Can you demonstrate through NJEDA analysis that without the incentive award, the redevelopment project is not economically feasible?",
        "type": "radio",
        "key": "aspire-1",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Real Estate")],
        "eligible": [(ASPIRE_PROGRAM, "Yes")]
    },
    {
        "question": "Can you demonstrate that a project financing gap exists and/or the redevelopment project will generate a below market rate of return?",
        "type": "radio",
        "key": "aspire-2",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Real Estate")],
        "eligible": [(ASPIRE_PROGRAM, "Yes")]
    },
    {
        "question": "Does the developer have an equity participation of at least 20 percent of the total cost?",
        "type": "radio",
        "key": "aspire-3",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Real Estate")],
        "eligible": [(ASPIRE_PROGRAM, "Yes")]
    },
    {
        "question": "Will the project result in a net positive benefit to the State?",
        "type": "radio",
        "key": "aspire-4",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Real Estate")],
        "eligible": [(ASPIRE_PROGRAM, "Yes")]
    },
    {
        "question": "Does the project meet specific cost thresholds, depending on where it is located?",
        "type": "radio",
        "key": "aspire-5",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Real Estate")],
        "eligible": [(ASPIRE_PROGRAM, "Yes")]
    }
]
