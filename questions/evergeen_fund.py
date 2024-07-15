from consts import EVERGREEN_PROGRAM_NAME

EVERGREEN_FUND_QUESTIONS = [
    {
        "question": "Does your firm have a minimum of \$10 million assets under management at the time of certification?",
        "type": "radio",
        "key": "evergreen-1",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Does your firm have at least two principals or persons employed full-time to direct qualified investment of capital, with at least five years of money management experience?",
        "type": "radio",
        "key": "evergreen-2",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Does your firm demonstrate satisfactory diversity, equity, and inclusion (DE&I) policies and track records in achieving their stated DE&I goals?",
        "type": "radio",
        "key": "evergreen-3",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Is the business you plan to invest in registered to do business in New Jersey?",
        "type": "radio",
        "key": "evergreen-4",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Does the business have its principal operations located in New Jersey and intend to maintain them there after receiving a qualified investment?",
        "type": "radio",
        "key": "evergreen-5",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Is the business a high-growth company engaged in a targeted industry?",
        "type": "radio",
        "key": "evergreen-6",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    },
    {
        "question": "Does the business employ fewer than 250 persons?",
        "type": "radio",
        "key": "evergreen-7",
        "options": ["Yes", "No"],
        "depends_on": [("industry", "Venture Capital")],
        "eligible": [(EVERGREEN_PROGRAM_NAME, "Yes")]
    }
]
