import stream as st
from main import calculate_credit_score

st.title("Farmer Credit Score Assessment")
score = 0
# Input fields for user data
# Geopolitical zones dictionary
geo_zones = {
  "Abia": "South East",
  "Adamawa": "North East",
  "Akwa Ibom": "South South",
  "Anambra": "South East",
  "Bauchi": "North East",
  "Bayelsa": "South South",
  "Benue": "North Central",
  "Borno": "North East",
  "Cross River": "South South",
  "Delta": "South South",
  "Ebonyi": "South East",
  "Edo": "South South",
  "Ekiti": "South West",
  "Enugu": "South East",
  "Gombe": "North East",
  "Imo": "South East",
  "Jigawa": "North West",
  "Kaduna": "North West",
  "Kano": "North West",
  "Katsina": "North West",
  "Kebbi": "North West",
  "Kogi": "North Central",
  "Kwara": "North Central",
  "Lagos": "South West",
  "Nasarawa": "North Central",
  "Niger": "North Central",
  "Ogun": "South West",
  "Ondo": "South West",
  "Osun": "South West",
  "Oyo": "South West",
  "Plateau": "North Central",
  "Rivers": "South South",
  "Sokoto": "North West",
  "Taraba": "North East",
  "Yobe": "North East",
  "Zamfara": "North West",
  "FCT": "North Central"  # Abuja Federal Capital Territory 
}

# User input fields for user data
farm_ownership = st.selectbox("Farm Ownership", ["Rented", "Leased", "Owned"])
farm_size = st.selectbox("Farm Size", ["0-1ha", "2-3ha", "4-5ha", "6-7ha"])
education_level = st.selectbox("Education Level", ["Informal", "Elementary", "College/ High School", "Tertiary"])
marital_status = st.selectbox("Marital Status", ["Single", "Married"])
age = st.number_input("Age", min_value=18)
farm_type = st.selectbox("Farm Type", ["Animaltypes", "Crotypes"])
income = st.number_input("Annual Income", min_value=0)
gender = st.selectbox("Gender", ["Male", "Female"])
state_location = st.selectbox("Farm Location", list(geo_zones.keys()))  # Use state names as options

# Convert state to geo zone for function call
geo_zone = geo_zones[state_location]

# Calculate button
if st.button("Calculate Credit Score"):
  score = calculate_credit_score(farm_ownership, farm_size, education_level, marital_status, age, farm_type, income, gender, geo_zone)
  st.write("Your Credit Score:", score)

# Interpretation of score (optional)

if score > 0:
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

