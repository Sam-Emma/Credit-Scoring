def calculate_credit_score(farm_ownership, farm_size, education_level, marital_status, age, farm_type, income, gender, farm_location):
    score = 0

    # Farm ownership
    if farm_ownership == "Rented":
        score += 3
    elif farm_ownership == "Leased":
        score += 5
    elif farm_ownership == "Owned":
        score += 10

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
    elif farm_type == "Crotypes":
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
    if gender == "Male":
        score += 5
    elif gender == "Female":
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

    return score
