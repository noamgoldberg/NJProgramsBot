from consts import FILM_TAX_CREDIT_PROGRAM, DIGITAL_MEDIA_TAX_CREDIT_PROGRAM

FILM_MEDIA_QUESTIONS = [
    {
        "question": "Is your project a feature film, television series, or television show of 22 minutes or more in length intended for a national or regional audience?",
        "type": "radio",
        "key": "film-1",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Does your project exclude productions featuring news, current events, weather, and market reports or public programming, sports events, solicitations for funds, obscene material, or primarily private, industrial, corporate, or institutional purposes?",
        "type": "radio",
        "key": "film-2",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Is your project a reality show?",
        "type": "radio",
        "key": "film-3",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "No")]
    },
    {
        "question": "If a reality show, has your production company invested \$2 million in capital investment in a 20,000+ sqft studio facility located in a UEZ Municipality and has site control of the facility for at least 2 years?",
        "type": "radio",
        "key": "film-4",
        "options": ["Yes", "No"],
        "depends_on": [("film-3", "Yes")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Do 60 percent of the total film production expenses (exclusive of post-production costs) incur for services and goods purchased through vendors authorized to do business in New Jersey?",
        "type": "radio",
        "key": "film-5",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Do qualified film production expenses exceed \$1 million per production?",
        "type": "radio",
        "key": "film-6",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Do the end credits of your project include the 'Filmed in New Jersey' statement or logo?",
        "type": "radio",
        "key": "film-7",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Will the principal photography of your project commence within 180 days of application?",
        "type": "radio",
        "key": "film-8",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(FILM_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Do at least \$2 million of the total digital media production expenses incur for services performed and goods purchased through vendors authorized to do business in New Jersey?",
        "type": "radio",
        "key": "film-9",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(DIGITAL_MEDIA_TAX_CREDIT_PROGRAM, "Yes")]
    },
    {
        "question": "Are at least 50 percent of the qualified digital media content production expenses for wages and salaries paid to full-time employees in New Jersey?",
        "type": "radio",
        "key": "film-10",
        "options": ["Yes", "No"],
        "depends_on": [("q-2", "Film and Media")],
        "eligible_for": [(DIGITAL_MEDIA_TAX_CREDIT_PROGRAM, "Yes")]
    }
]
