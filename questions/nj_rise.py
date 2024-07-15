from consts import NJ_RISE_PROGRAM

NJ_RISE_QUESTIONS = [
    {
        "question": "Does the business have 25 or more U.S. Full-Time Employees?",
        "type": "radio",
        "key": "njrise-1",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    },
    {
        "question": "Will the business submit a completed application to the EDA on or before July 1, 2028?",
        "type": "radio",
        "key": "njrise-2",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    },
    {
        "question": "Is the business principally located in another state that uses the convenience of the employer income taxation rule (e.g., Delaware, Nebraska, New York)?",
        "type": "radio",
        "key": "njrise-3",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    },
    {
        "question": "Is the business in substantial good standing with the New Jersey Department of Labor and Workforce Development (LWD) and the New Jersey Department of Environmental Protections (DEP)?",
        "type": "radio",
        "key": "njrise-4",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    },
    {
        "question": "Will re-assigned employees include full-time and part-time employees, but not independent contractors or individuals working on a consulting basis for the business?",
        "type": "radio",
        "key": "njrise-5",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    },
    {
        "question": "Will a current tax clearance be provided at application and maintained through disbursement to demonstrate the applicant is properly registered to do business in New Jersey and in substantial good standing with the New Jersey Division of Taxation?",
        "type": "radio",
        "key": "njrise-6",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(NJ_RISE_PROGRAM, "Yes")]
    }
]
