import stream as st

# Import your credit score calculation functions
from main1 import calculate_farmer_bio_credit_score, calculate_capital_credit_score, calculate_character_credit_score, calculate_collateral_credit_score, calculate_capacity_credit_score

st.title("Farmer Credit Score Assessment")

# Function to calculate total credit score
def calculate_total_credit_score(farm_ownership, farm_size, education_level, marital_status, age, farm_type, income, gender, farm_location, bvn, nin, in_farmers_group, next_of_kin, 
                                 capital, other_income_sources, num_income_contributors, monthly_income, cultivation_cost, loan_amount, farming_experience,
                                 crops_cultivated, fertilization_frequency, airtime_spent_weekly, bank_account_balance, highest_transaction,
                                 living_situation, num_farmlands, household_labour, children_helping, keeping_animals, crop_rotation, uses_machine, machine_ownership, num_machines):

    # Calculate individual scores
    farmer_bio_score = calculate_farmer_bio_credit_score(farm_size, education_level, marital_status, age, farm_type, income, gender, farm_location, bvn, nin, in_farmers_group, next_of_kin)
    capital_score = calculate_capital_credit_score(capital, other_income_sources, num_income_contributors, monthly_income, cultivation_cost, loan_amount, farming_experience)
    character_score = calculate_character_credit_score(crops_cultivated, fertilization_frequency, airtime_spent_weekly, bank_account_balance, highest_transaction)
    collateral_score = calculate_collateral_credit_score(living_situation, num_farmlands, farm_ownership, farm_size)
    capacity_score = calculate_capacity_credit_score(hired_labour, pay_per_labourer, labour_type, household_labour, children_helping, keeping_animals, crop_rotation, education_level, uses_machine, machine_ownership, num_machines)

    # Sum up all scores
    total_score = (farmer_bio_score + capital_score + character_score + collateral_score + capacity_score)/5

    return total_score

# User input fields for farmer bio data
st.header("Farmer Bio Data")
name = st.text_input("Name")
address = st.text_input("Name")
age = st.number_input("Age", min_value=18)
education_level = st.selectbox("Education Level", ["Informal", "Elementary", "College/ High School", "Tertiary"])
marital_status = st.selectbox("Marital Status", ["Single", "Married"])
farm_type = st.selectbox("Farm Type", ["Animaltypes", "Croptypes"])
income = st.number_input("Annual Income", min_value=0)
gender = st.selectbox("Gender", ["Male", "Female"])
farm_location = st.selectbox("Farm Location", ["North West", "North Central", "South West", "South South", "North East", "South East"])
bvn = st.checkbox("Have BVN")
nin = st.checkbox("Have NIN")
in_farmers_group = st.checkbox("In Farmers Group")
next_of_kin = st.checkbox("Have Next of Kin Info")

# User input fields for capital data
st.header("Capital Data")
capital = st.checkbox("Have Capital")
other_income_sources = st.number_input("Other Income Sources", min_value=0)
num_income_contributors = st.number_input("Number of Income Contributors", min_value=0)
monthly_income = st.number_input("Monthly Income After Harvest and Sale", min_value=0)
cultivation_cost = st.number_input("Cost of Cultivation per Season", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
farming_experience = st.number_input("Years of Farming Experience", min_value=0)

# User input fields for character data
st.header("Character Data")
crops_cultivated = st.multiselect("Crops Cultivated", ["Legumes", "Cereals", "Fruits", "Tubers"])
fertilization_frequency = st.number_input("How many times in 12 months do you fertilize your crop?", min_value=0)
airtime_spent_weekly = st.number_input("Average Amount Spent on Airtime Weekly", min_value=0)
bank_account_balance = st.number_input("Average Bank Account Balance", min_value=0)
highest_transaction = st.number_input("Highest Transaction Ever", min_value=0)

# User input fields for collateral data
st.header("Collateral Data")
living_situation = st.selectbox("Living Situation", ["Rented apartment", "House built by you"])
num_farmlands = st.number_input("Number of Farmlands", min_value=0)
farm_ownership = st.selectbox("Farm Ownership", ["Rented", "Leased", "Owned"])
farm_size = st.selectbox("Farm Size", ["0-1ha", "2-3ha", "4-5ha", "6-7ha"])

# User input fields for capacity data
st.header("Capacity Data")
hired_labour = st.number_input("Number of Hired Labour", min_value=0)
pay_per_labourer = st.number_input("How much do you pay each labourer?", min_value=0)
labour_type = st.selectbox("Type of Labor", ["Permanent", "Temporary", "Seasonal"])
household_labour = st.checkbox("Use Household Labour")
children_helping = st.number_input("Number of Children Helping on Farm", min_value=0)
keeping_animals = st.checkbox("Keep Animals")
crop_rotation = st.checkbox("Practice Crop Rotation")
uses_machine = st.checkbox("Uses Machine")
machine_ownership = st.selectbox("Machine Ownership", ["Owned", "Rented"])
num_machines = st.number_input("Number of Machines Owned", min_value=0)

# Calculate button
if st.button("Calculate Credit Score"):
    score = calculate_total_credit_score(
        farm_ownership, farm_size, education_level, marital_status, age, farm_type, income, gender, farm_location, bvn, nin, in_farmers_group, next_of_kin, 
        capital, other_income_sources, num_income_contributors, monthly_income, cultivation_cost, loan_amount, farming_experience,
        crops_cultivated, fertilization_frequency, airtime_spent_weekly, bank_account_balance, highest_transaction,
        living_situation, num_farmlands, household_labour, children_helping, keeping_animals, crop_rotation, uses_machine, machine_ownership, num_machines
    )
    st.write("Your Credit Score:", score)

    # Interpretation of score
    if score >= 70:
        st.write("Grade A. Your credit score is excellent! You will qualify for the best loan options with favorable terms.")
    elif score >= 60:
        st.write("Grade B. Your credit score is good. You should be able to access loans with reasonable interest rates.")
    elif score >= 50:
        st.write("Grade C. Your credit score is fair. You might qualify for some loans but may face higher interest rates.")
    elif score >= 40:
        st.write("Grade D. Your credit score is considered low. You may want to improve factors like farm ownership, education, or income to increase your score.")
    else:
        st.write("Grade F. Your credit score is too low. You may want to improve factors like farm ownership, education, or income to increase your score.")
