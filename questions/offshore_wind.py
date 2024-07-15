from consts import OFFSHORE_WIND_PROGRAM

OFFSHORE_WIND_QUESTIONS = [
    {
        "question": "Is your business making or acquiring a minimum \$50 million capital investment in a qualified wind energy facility located in New Jersey?",
        "type": "radio",
        "key": "offshorewind-1",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "As a tenant, are you occupying space in a qualified wind energy facility in New Jersey where the owner has made or acquired a minimum \$50 million capital investment in the facility, with your tenant-occupied space representing at least \$17.5 million of the capital investment?",
        "type": "radio",
        "key": "offshorewind-2",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business employ a minimum number of new, full-time employees during the five eligibility years following application for the tax credit as specified?",
        "type": "radio",
        "key": "offshorewind-3",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business employ at least 100 new, full-time employees in the first year?",
        "type": "radio",
        "key": "offshorewind-4",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business employ at least 150 new, full-time employees in the second year?",
        "type": "radio",
        "key": "offshorewind-5",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business employ at least 200 new, full-time employees in the third year?",
        "type": "radio",
        "key": "offshorewind-6",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business employ at least 300 new, full-time employees in the fourth and fifth years?",
        "type": "radio",
        "key": "offshorewind-7",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will your business, if having between 150 and 300 new, full-time employees, receive an award based on the prorated formula?",
        "type": "radio",
        "key": "offshorewind-8",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will the calculation of new full-time employees include new employees resulting from supply coordination agreements with an equipment manufacturer, supplier, installer, or operator that supports a qualified offshore wind project?",
        "type": "radio",
        "key": "offshorewind-9",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will the new full-time jobs be counted if the employee’s primary office is at the qualified wind energy facility and they spend at least 80% of their time at the facility?",
        "type": "radio",
        "key": "offshorewind-10",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    },
    {
        "question": "Will the new full-time jobs be counted if they result from a supply coordination agreement and the employee spends at least 80% of their time in New Jersey?",
        "type": "radio",
        "key": "offshorewind-11",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Any")],
        "eligible_for": [(OFFSHORE_WIND_PROGRAM, "Yes")]
    }
]
