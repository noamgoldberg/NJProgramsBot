from consts import EMERGE_PROGRAM

EMERGE_QUESTIONS = [
    {
        "question": "Will the project create at least 35 new, full-time jobs?",
        "type": "radio",
        "key": "emerge-1",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Does the project meet minimum capital investment requirements?",
        "type": "radio",
        "key": "emerge-2",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Will the Emerge tax credits yield a minimum net positive economic benefit to the state of 200 percent to 400 percent depending on project location?",
        "type": "radio",
        "key": "emerge-3",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Will at least 80 percent of incented employees’ work time be spent in New Jersey and 80 percent of the withholdings of new or retained full-time jobs be subject to the ‘New Jersey Gross Income Tax Act’?",
        "type": "radio",
        "key": "emerge-4",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Can the Qualified Business Facility accommodate at least 50 percent of incented jobs?",
        "type": "radio",
        "key": "emerge-5",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Will the project commit to staying at the Qualified Business Facility for 1.5 times the eligibility period?",
        "type": "radio",
        "key": "emerge-6",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    },
    {
        "question": "Can you demonstrate that the award of the tax credit is a “material factor” in the decision to create or retain at least the minimum number of full-time jobs?",
        "type": "radio",
        "key": "emerge-7",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Any")],
        "eligible": [(EMERGE_PROGRAM, "Yes")]
    }
]
