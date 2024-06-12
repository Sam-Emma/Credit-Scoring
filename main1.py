def calculate_farmer_bio_credit_score(farm_size, education_level, marital_status, age, farm_type, income, gender, farm_location, bvn, nin, in_farmers_group, next_of_kin):
    score = 0

#     # Farm ownership
#     if farm_ownership == "Rented":
#         score += 3
#     elif farm_ownership == "Leased":
#         score += 5
#     elif farm_ownership == "Owned":
#         score += 10

    # Farm size
    if farm_size == "0-1ha":
        score += 4
    elif farm_size == "2-3ha":
        score += 6
    elif farm_size == "4-5ha":
        score += 8
    elif farm_size == "6-7ha":
        score += 10

    # Education level
    if education_level == "Informal":
        score += 2
    elif education_level == "Elementary":
        score += 3
    elif education_level == "College/ High School":
        score += 4
    elif education_level == "Tertiary":
        score += 5

    # Marital status
    if marital_status == "Single":
        score += 3
    elif marital_status == "Married":
        score += 5

    # Age
    if age >= 0 and age <= 17:
        score += 4
    elif age >= 18 and age <= 35:
        score += 10
    elif age >= 36 and age <= 50:
        score += 8
    elif age > 50:
        score += 6

    # Farm type
    if farm_type == "Animaltypes":
        score += 10
    elif farm_type == "Croptypes":
        score += 15

    # Income
    if income <= 100000:
        score += 5
    elif income <= 250000:
        score += 10
    elif income <= 500000:
        score += 15
    elif income <= 1000000:
        score += 25
    else:
        score += 30

    # Gender
    score += 5

    # Farm location
    if farm_location == "North West":
        score += 10
    elif farm_location == "North Central":
        score += 7
    elif farm_location == "South West":
        score += 7
    elif farm_location == "South South":
        score += 2
    elif farm_location == "North East":
        score += 5
    elif farm_location == "South East":
        score += 5

    # BVN
    if bvn:
        score += 5

    # NIN
    if nin:
        score += 5

    # Farmers Group
    if in_farmers_group:
        score += 5

    # Next of Kin Info
    if next_of_kin:
        score += 5

    return score


def calculate_capital_credit_score(capital, other_income_sources, num_income_contributors, monthly_income, cultivation_cost, loan_amount, farming_experience):
    score = 0

    # Capital
    if capital:
        score += 5

    # Other Income Sources
    score += other_income_sources * 2

    # Number of Persons Contributing to Income
    score += num_income_contributors * 2

    # Monthly Income After Harvest and Sale
    if monthly_income <= 10000:
        score += 1
    elif monthly_income <= 20000:
        score += 2
    elif monthly_income <= 50000:
        score += 3
    elif monthly_income <= 100000:
        score += 4
    else:
        score += 5

    # Cost of Cultivation per Season
    if cultivation_cost <= 50000:
        score += 0
    elif cultivation_cost <= 100000:
        score -= 5
    elif cultivation_cost <= 200000:
        score -= 10
    else:
        score -= 15

    # Loan Amount
    if loan_amount <= 100000:
        score += 0
    elif loan_amount <= 200000:
        score -= 5
    elif loan_amount <= 500000:
        score -= 10
    else:
        score -= 15

    # Years of Farming Experience
    if farming_experience <= 1:
        score += 1
    elif farming_experience <= 3:
        score += 3
    elif farming_experience <= 5:
        score += 5
    elif farming_experience <= 10:
        score += 7
    else:
        score += 10

    return score

def calculate_character_credit_score(crops_cultivated, fertilization_frequency, airtime_spent_weekly, bank_account_balance, highest_transaction):
    score = 0

    # Crops Cultivated
    crops_points = {
        "Legumes": 10,
        "Cereals": 8,
        "Fruits": 6,
        "Tubers": 4
    }
    for crop in crops_cultivated:
        if crop in crops_points:
            score += crops_points[crop]

    # Frequency of Fertilization
    if fertilization_frequency <= 2:
        score += 2
    elif fertilization_frequency <= 4:
        score += 4
    elif fertilization_frequency <= 6:
        score += 6
    else:
        score += 8

    # Average Amount Spent on Airtime Weekly
    if airtime_spent_weekly <= 500:
        score += 1
    elif airtime_spent_weekly <= 1000:
        score += 2
    elif airtime_spent_weekly <= 2000:
        score += 3
    else:
        score += 4

    # Average Bank Account Balance
    if bank_account_balance <= 5000:
        score += 1
    elif bank_account_balance <= 10000:
        score += 2
    elif bank_account_balance <= 20000:
        score += 3
    else:
        score += 4

    # Highest Transaction Ever
    if highest_transaction <= 10000:
        score += 1
    elif highest_transaction <= 50000:
        score += 2
    elif highest_transaction <= 100000:
        score += 3
    else:
        score += 4

    return score


def calculate_collateral_credit_score(living_situation, num_farmlands, farm_ownership, farm_size):
    score = 0

    # Living Situation
    if living_situation == "Rented apartment":
        score += 2
    elif living_situation == "House built by you":
        score += 5

    # Number of Farmlands
    if num_farmlands == 1:
        score += 2
    elif num_farmlands == 2:
        score += 4
    elif num_farmlands >= 3:
        score += 6

    # Farm Ownership
    if farm_ownership == "Rented":
        score += 3
    elif farm_ownership == "Leased":
        score += 5
    elif farm_ownership == "Owned":
        score += 10

    # Farm Size (in hectares)
    if farm_size == "0-1 ha":
        score += 4
    elif farm_size == "2-3 ha":
        score += 6
    elif farm_size == "4-5 ha":
        score += 8
    elif farm_size == "6-7 ha":
        score += 10

    return score


def calculate_capacity_credit_score(hired_labour, pay_per_labourer, labour_type, household_labour, children_helping, keeping_animals, crop_rotation, educational_level, uses_machine, machine_ownership, num_machines):
    score = 0

    # Number of Hired Labour
    if hired_labour <= 2:
        score += 2
    elif hired_labour <= 5:
        score += 4
    elif hired_labour <= 10:
        score += 6
    else:
        score += 8

    # Pay Per Labourer
    if pay_per_labourer <= 1000:
        score += 1
    elif pay_per_labourer <= 2000:
        score += 2
    elif pay_per_labourer <= 3000:
        score += 3
    else:
        score += 4

    # Type of Labor
    if labour_type == "Permanent":
        score += 5
    elif labour_type == "Temporary":
        score += 3
    elif labour_type == "Seasonal":
        score += 2

    # Household Labor
    if household_labour:
        score += 3

    # Children Helping on Farm
    if children_helping <= 1:
        score += 1
    elif children_helping <= 3:
        score += 2
    elif children_helping <= 5:
        score += 3
    else:
        score += 4

    # Keeping Animals
    if keeping_animals:
        score += 5

    # Practicing Crop Rotation
    if crop_rotation:
        score += 5

    # Educational Level
    if educational_level == "Informal":
        score += 1
    elif educational_level == "Elementary":
        score += 2
    elif educational_level == "College/High School":
        score += 3
    elif educational_level == "Tertiary":
        score += 5

    # Uses Machine
    if uses_machine:
        score += 5

    # Machine Ownership
    if machine_ownership == "Owned":
        score += 5
    elif machine_ownership == "Rented":
        score += 2

    # Number of Machines Owned
    if num_machines == 0:
        score += 0
    elif num_machines <= 2:
        score += 2
    elif num_machines <= 4:
        score += 4
    else:
        score += 6

    return score