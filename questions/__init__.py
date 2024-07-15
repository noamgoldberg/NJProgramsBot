from typing import List, Dict

from questions.film_media import FILM_MEDIA_QUESTIONS
from questions.evergeen_fund import EVERGREEN_FUND_QUESTIONS
from questions.nj_rise import NJ_RISE_QUESTIONS
from questions.aspire import ASPIRE_QUESTIONS
from questions.tech_nol import TECH_BIOTECH_NOL_QUESTIONS
from questions.emerge import EMERGE_QUESTIONS
from questions.brownfield import BROWNFIELD_QUESTIONS
from questions.offshore_wind import OFFSHORE_WIND_QUESTIONS


QUESTIONS: List[Dict[str, str]] = [
    {
        "question": "Is your project located in an eligible incentive area as defined by NJEDA? Click " + \
            "[here](https://njeda.maps.arcgis.com/apps/webappviewer/index.html?id=8fed69ed4a664ec6b76f2a6ab633444c) " + \
            "for an interactive map of qualified incentive areas in NJ.",
        "type": "selectbox",
        "key": "q-1",
        "options": ["Yes", "No"]
    },
    {
        "question": "What industry is your project in?",
        "type": "selectbox",
        "key": "q-2",
        "options": [
            "Technology",
            "Biotechnology",
            "Film and Media",
            "Renewable Energy",
            "Real Estate",
            "Venture Capital",
            "Other"
        ],
        "depends_on": [("q-1", "Yes")]
    },
]
QUESTIONS += (
    FILM_MEDIA_QUESTIONS +
    EVERGREEN_FUND_QUESTIONS +
    NJ_RISE_QUESTIONS +
    ASPIRE_QUESTIONS +
    TECH_BIOTECH_NOL_QUESTIONS +
    EMERGE_QUESTIONS +
    BROWNFIELD_QUESTIONS +
    OFFSHORE_WIND_QUESTIONS
)