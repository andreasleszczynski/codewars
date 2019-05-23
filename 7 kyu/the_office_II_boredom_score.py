""" The Office II - Boredom Score  - 7 kyu Kata Fundamentals
Every now and then people in the office moves teams or departments.
Depending what people are doing with their time they can become more or less
boring. Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys,
and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1
finance = 2
canteen = 10
regulation = 3
trading = 6
change = 6
IS = 8
retail = 5
cleaning = 4
pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'
"""
def boredom(staff):
    score = 0
    assessment_score = { "accounts": 1,
    "finance": 2,
    "canteen": 10,
    "regulation": 3,
    "trading": 6,
    "change": 6,
    "IS": 8,
    "retail": 5,
    "cleaning": 4,
    "pissing about": 25}

    for element in staff.values():
        score += assessment_score.get(element)

    if score <= 80:
        return 'kill me now'
    elif score < 100:
        return 'i can handle this'
    return 'party time!!'


print(boredom({"tim": "change", "jim": "accounts",
  "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
  "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
  "mr": "finance" })) # "kill me now"

print(boredom({ "tim": "IS", "jim": "finance",
  "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
  "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
  "alex": "regulation", "john": "accounts", "mr": "canteen" })) # "i can handle this"

print(boredom({ "tim": "accounts", "jim": "accounts",
  "randy": "pissing about", "sandy": "finance", "andy": "change",
  "katie": "IS", "laura": "IS", "saajid": "canteen", "alex": "pissing about",
  "john": "retail", "mr": "pissing about" })) # "party time!!"
