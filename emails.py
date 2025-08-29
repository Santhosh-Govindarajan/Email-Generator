# import pandas as pd
# import os

# class EmailGenerator:
#     def __init__(self, domain="@skct.edu.in"):
#         self.domain = domain

#     # General function to generate emails for any department
#     def generate_emails(self, dept_code, count):
#         emails = []
#         for i in range(1, count + 1):
#             number = str(i).zfill(3)
#             email = f"727822tu{dept_code}{number}{self.domain}"
#             emails.append(email)
#         return emails

#     # Department-wise functions with custom counts
#     def IT(self):
#         return self.generate_emails("it", 400)

#     def ECE(self):
#         return self.generate_emails("ece", 250)

#     def EEE(self):
#         return self.generate_emails("eee", 200)

#     def AIDS(self):
#         return self.generate_emails("ads", 200)

#     def CSE(self):
#         return self.generate_emails("cse", 400)

#     def CIVIL(self):
#         return self.generate_emails("civ", 100)

#     def MECH(self):
#         return self.generate_emails("mec", 100)

#     # Function to save emails to Excel and CSV inside a folder
#     def save_to_files(self, all_emails, folder="output", filename="generated_emails"):
#         # Create folder if it doesn't exist
#         os.makedirs(folder, exist_ok=True)

#         # Full file paths
#         excel_path = os.path.join(folder, f"{filename}.xlsx")
#         csv_path = os.path.join(folder, f"{filename}.csv")

#         df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in all_emails.items()]))

#         # Save as Excel
#         df.to_excel(excel_path, index=False)
#         # Save as CSV
#         df.to_csv(csv_path, index=False)
#         print(f"✅ Emails saved to {excel_path} and {csv_path}")


# # ====== Usage Example ======
# if __name__ == "__main__":
#     generator = EmailGenerator()

#     # Generate emails for all departments
#     emails_dict = {
#         "IT": generator.IT(),
#         "ECE": generator.ECE(),
#         "EEE": generator.EEE(),
#         "AIDS": generator.AIDS(),
#         "CSE": generator.CSE(),
#         "CIVIL": generator.CIVIL(),
#         "MECH": generator.MECH(),
#     }

#     # Save files in "output" folder
#     generator.save_to_files(emails_dict, folder="output")



# import streamlit as st
# import pandas as pd

# # Load colleges from CSV
# college_df = pd.read_csv(r"H:\SanthoshIntern\CODES\Email_generating\ErodeCollegeList.csv")  # Ensure CSV has 'College Name' column

# # Departments and counts
# departments = {
#     "IT":   ("tuit", 400),
#     "ECE":  ("tuece", 250),
#     "EEE":  ("tueee", 200),
#     "AIDS": ("tuads", 200),
#     "CSE":  ("tucse", 400),
#     "CIVIL":("tuciv", 100),
#     "MECH": ("tumec", 100),
# }

# st.title("College Email Generator")

# # Dropdown for college name
# college_name = st.selectbox("Select College Name:", options=college_df['College Name'].unique())

# # Text box for joining year
# year = st.text_input("Enter Joining Year (e.g., 22, 23, 24):")

# # Text box for domain
# domain = st.text_input("Enter College Domain (e.g., skct.edu.in):")

# if st.button("Generate Emails"):
#     if year and domain:
#         # Generate emails
#         email_data = []
#         for dept, (prefix, count) in departments.items():
#             for i in range(1, count + 1):
#                 email = f"{year}{prefix}{str(i).zfill(3)}@{domain}"
#                 email_data.append([college_name, dept, email])
#         df = pd.DataFrame(email_data, columns=["College Name", "Department", "Email"])
#         st.write(df)
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="Download as CSV",
#             data=csv,
#             file_name=f"{college_name}_{year}_emails.csv",
#             mime="text/csv"
#         )
#     else:
#         st.warning("Please fill in both year and domain.")




###############################For Erode
# import streamlit as st
# import pandas as pd

# # Page config for wider layout and page title
# st.set_page_config(page_title="Erode College Email Generator", layout="wide")

# # Load college names from CSV (ensure 'College Name' column exists in this file)
# college_df = pd.read_csv("ErodeCollegeList.csv")

# departments_dict = {
#     "IT":   "tuit",
#     "ECE":  "tuece",
#     "EEE":  "tueee",
#     "AIDS": "tuads",
#     "CSE":  "tucse",
#     "CIVIL":"tuciv",
#     "MECH": "tumec",
# }

# # Sidebar for inputs
# with st.sidebar:
#     st.header("Enter Your Details")
#     college_name = st.selectbox("Select College Name:", options=college_df['College Name'].unique())
#     year = st.text_input("Enter Joining Year (e.g., 22, 23, 24):")
#     domain = st.text_input("Enter College Domain (e.g., skct.edu.in):")
#     selected_departments = st.multiselect(
#         "Select Departments:",
#         options=list(departments_dict.keys())
#     )
#     dept_counts = {}
#     if selected_departments:
#         st.write("Number of Emails Per Department:")
#         for dept in selected_departments:
#             dept_counts[dept] = st.number_input(
#                 f"{dept}:",
#                 min_value=1, max_value=500, value=10, step=1
#             )

# st.title("📧 Erode College Email Generator")
# #st.markdown("Generate student emails dynamically by selecting college, year, domain, and departments.")

# if st.sidebar.button("Generate Emails"):
#     if not (year and domain and selected_departments):
#         st.warning("Please enter year, domain, and select at least one department.")
#     else:
#         emails = []
#         for dept in selected_departments:
#             prefix = departments_dict[dept]
#             count = dept_counts.get(dept, 0)
#             for i in range(1, int(count) + 1):
#                 email = f"{year}{prefix}{str(i).zfill(3)}@{domain}"
#                 emails.append([college_name, dept, email])
#         df = pd.DataFrame(emails, columns=["College Name", "Department", "Email"])
#         st.success(f"Generated {len(df)} email(s) for {college_name}!")
#         st.dataframe(df, use_container_width=True)
#         csv = df.to_csv(index=False)
#         st.download_button(
#             label="⬇️ Download Emails CSV",
#             data=csv,
#             file_name=f"{college_name}_{year}_emails.csv",
#             mime="text/csv",
#         )

########################################outline code
# import streamlit as st
# import pandas as pd

# # Load Excel into DataFrame
# @st.cache_data
# def load_data():
#     return pd.read_excel("ErodeCollegeData.xlsx")

# df = load_data()

# st.title("📧 Erode College Email ID Generator")

# # Filter inputs in order
# state_list = sorted(df["State"].unique())
# selected_state = st.selectbox("Select State:", options=state_list)

# filtered_city_df = df[df["State"] == selected_state]
# city_list = sorted(filtered_city_df["City"].unique())
# selected_city = st.selectbox("Select City:", options=city_list)

# filtered_year_df = filtered_city_df[filtered_city_df["City"] == selected_city]
# year_list = sorted(filtered_year_df["Year"].unique())
# selected_year = st.selectbox("Select Year:", options=year_list)

# filtered_college_df = filtered_year_df[filtered_year_df["Year"] == selected_year]
# college_list = sorted(filtered_college_df["College Name"].unique())
# selected_college = st.selectbox("Select College Name:", options=college_list)

# filtered_dept_df = filtered_college_df[filtered_college_df["College Name"] == selected_college]
# dept_list = sorted(filtered_dept_df["Department Name"].unique())
# selected_dept = st.selectbox("Select Department Name:", options=dept_list)

# num_emails = st.number_input("Number of emails to generate:", min_value=1, max_value=500, value=10)

# # Extract required data for email generation
# info_row = df[
#     (df["State"] == selected_state) &
#     (df["City"] == selected_city) &
#     (df["Year"] == selected_year) &
#     (df["College Name"] == selected_college) &
#     (df["Department Name"] == selected_dept)
# ].iloc[0]

# domain = info_row["College Domain Name"]
# year_str = str(info_row["Year"])
# college_name = info_row["College Name"]
# dept_email_prefix = info_row["Department name in email id"]

# # Generate emails on button click
# if st.button("Generate Emails"):
#     emails = []
#     for i in range(1, num_emails + 1):
#         email = f"{year_str}{dept_email_prefix}{str(i).zfill(3)}@{domain}"
#         emails.append(email)

#     # Create DataFrame for emails
#     df_emails = pd.DataFrame({
#         "College Name": [college_name] * num_emails,
#         "Department Name": [selected_dept] * num_emails,
#         "Email": emails
#     })

#     st.success(f"Generated {num_emails} emails!")
#     st.dataframe(df_emails)

#     # CSV download
#     csv_data = df_emails.to_csv(index=False)
#     st.download_button(
#         label="⬇️ Download Emails as CSV",
#         data=csv_data,
#         file_name=f"{college_name}_{selected_dept}_{year_str}_emails.csv",
#         mime="text/csv"
#     )

import streamlit as st
import pandas as pd

# Load Excel into DataFrame
@st.cache_data
def load_data():
    return pd.read_excel(r"H:\SanthoshIntern\CODES\Email_generating\Colleges_list.xlsx")

df = load_data()

st.title("📧 College Email ID Generator")

# ========== Hierarchy Filters ==========
# 1. District
district_list = sorted(df["District"].dropna().unique())
selected_district = st.selectbox("🏙 Select District:", options=district_list)

# 2. College based on District
filtered_college_df = df[df["District"] == selected_district]
college_list = sorted(filtered_college_df["College Name"].dropna().unique())
selected_college = st.selectbox("🎓 Select College:", options=college_list)

# 3. Year based on College (if available)
if "Year" in df.columns:
    filtered_year_df = filtered_college_df[filtered_college_df["College Name"] == selected_college]
    year_list = sorted(filtered_year_df["Year"].dropna().unique())
    selected_year = st.selectbox("📅 Select Joining Year:", options=year_list)
else:
    selected_year = st.number_input("📅 Enter Joining Year:", min_value=2000, max_value=2030, value=2025)

# 4. Department based on College (if available)
if "Department Name" in df.columns:
    filtered_dept_df = filtered_college_df[filtered_college_df["College Name"] == selected_college]
    dept_list = sorted(filtered_dept_df["Department Name"].dropna().unique())
    selected_dept = st.selectbox("🏢 Select Department:", options=dept_list)
else:
    selected_dept = st.text_input("🏢 Enter Department Name:", "CSE")

# Extract domain & email prefix if available
domain = df[df["College Name"] == selected_college]["College Domain Name"].values[0] if "College Domain Name" in df.columns else "example.com"
dept_email_prefix = df[df["College Name"] == selected_college]["Department name in email id"].values[0] if "Department name in email id" in df.columns else "dept"

# 5. Email count input
num_emails = st.number_input("🔢 Number of emails to generate:", min_value=1, max_value=500, value=10)

# ========= Email Generator =========
if st.button("🚀 Generate Emails"):
    emails = []
    for i in range(1, num_emails + 1):
        email = f"{str(selected_year)}{dept_email_prefix}{str(i).zfill(3)}@{domain}"
        emails.append(email)

    df_emails = pd.DataFrame({
        "District": [selected_district] * num_emails,
        "College Name": [selected_college] * num_emails,
        "Year": [selected_year] * num_emails,
        "Department Name": [selected_dept] * num_emails,
        "Email": emails
    })

    st.success(f"✅ Generated {num_emails} emails for {selected_college}, {selected_dept}!")
    st.dataframe(df_emails, use_container_width=True)

    # CSV download
    csv_data = df_emails.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Emails as CSV",
        data=csv_data,
        file_name=f"{selected_college}_{selected_dept}_{selected_year}_emails.csv",
        mime="text/csv"
    )


