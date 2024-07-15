from consts import EMERGE_PROGRAM, ASPIRE_PROGRAM

INCENTIVE_AREA_QUESTIONS = [
    {
        "question": "Is your project located in an eligible incentive area as defined by NJEDA? Click " + \
            "[here](https://njeda.maps.arcgis.com/apps/webappviewer/index.html?id=8fed69ed4a664ec6b76f2a6ab633444c) " + \
            "for an interactive map of qualified incentive areas in NJ.",
        "type": "radio",
        "key": "incentive_area",
        "options": ["Yes", "No"],
        "depends_on": [("emerge-1", "Yes"), ("aspire-1", "Yes")],
        "dependency_type": "OR",
        "eligible": [(EMERGE_PROGRAM, "Yes"), (ASPIRE_PROGRAM, "Yes"), ]
    },
]