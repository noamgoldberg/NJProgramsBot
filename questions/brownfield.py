from consts import BROWNFIELD_PROGRAM

BROWNFIELD_QUESTIONS = [
    {
        "question": "Is the project site a brownfield (a former or current commercial or industrial site that is currently vacant or underutilized and on which there has been, or is suspected to have been, a discharge of a contaminant, or on which there is contaminated building material)?",
        "type": "radio",
        "key": "brownfield-1",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Has the project received a letter of support from the governing body?",
        "type": "radio",
        "key": "brownfield-2",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Can you demonstrate that the project is not economically feasible without the tax credit award?",
        "type": "radio",
        "key": "brownfield-3",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Can you prove that a project financing gap exists, and the tax credit being considered for the project is equal to or less than the project financing gap?",
        "type": "radio",
        "key": "brownfield-4",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Will the project meet prevailing wage requirements for all remediation and construction work for the redevelopment project and subsequent redevelopment project, including 10 years for building services?",
        "type": "radio",
        "key": "brownfield-5",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Has the developer/affiliates not started remediation activities (other than environmental assessment and investigation activities) unless the applicant certifies that they could not have reasonably known the full extent of contamination prior to starting the cleanup?",
        "type": "radio",
        "key": "brownfield-6",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Can you demonstrate that remediation costs are reasonable and appropriate?",
        "type": "radio",
        "key": "brownfield-7",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Is the project in good standing with NJ Department of Environmental Protection, NJ Department of Labor and Workforce Development, and NJ Department of the Treasury?",
        "type": "radio",
        "key": "brownfield-8",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Does the developer have an equity contribution of 20% of the total cost of remediation (10% in Government Restricted Municipalities and Qualified Incentive Tracts)?",
        "type": "radio",
        "key": "brownfield-9",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Does the project have site access to perform the remediation?",
        "type": "radio",
        "key": "brownfield-10",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    },
    {
        "question": "Does the project meet Green Remediation/Green Building Standards?",
        "type": "radio",
        "key": "brownfield-11",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(BROWNFIELD_PROGRAM, "Yes")]
    }
]
