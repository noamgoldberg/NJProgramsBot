from typing import List, Dict

from questions.incentive_area import INCENTIVE_AREA_QUESTIONS
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
        "question": "What industry is your project in?",
        "type": "selectbox",
        "key": "industry",
        "options": [
            "Technology",
            "Biotechnology",
            "Film and Media",
            "Renewable Energy",
            "Real Estate",
            "Venture Capital",
            "Other"
        ],
    },
]
QUESTIONS += (
    ASPIRE_QUESTIONS +
    EMERGE_QUESTIONS +
    INCENTIVE_AREA_QUESTIONS +
    FILM_MEDIA_QUESTIONS +
    EVERGREEN_FUND_QUESTIONS +
    NJ_RISE_QUESTIONS +
    TECH_BIOTECH_NOL_QUESTIONS +
    BROWNFIELD_QUESTIONS +
    OFFSHORE_WIND_QUESTIONS
)