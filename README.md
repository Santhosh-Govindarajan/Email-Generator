# Email Generator

## Project Overview
The **Email Generator** project automates the creation of email IDs for students in a precise and organized manner. The project has evolved from being a college-specific solution to a nationwide system capable of generating emails based on structured data.

---

## **Step 1: College-Specific Email Generation**
Initially, the project was implemented for a **specified college**. Using the available student email data, a **dynamic Python script** was created to generate email IDs efficiently. This allowed the automation of email generation for all students within that college.

---

## **Step 2: Nationwide Email Generation**
The project has now been scaled to work for **the entire country**. To achieve this:

1. **Data Collection:** College details across the country are collected, including:
   - Country
   - State
   - District
   - City
   - College Name
   - Department Name
   - Department abbreviation in email ID
   - Domain name
   - Academic Year

2. **Excel File Creation:** All the collected details are organized into an **Excel file**. This file acts as the input for the Python code, enabling filtered and precise email generation.

3. **Dynamic Filtering:** 
   - The Python script allows filtering by country, state, city, college, department, and year.
   - Users can also specify the **number of email IDs** required from each department.

---

## **Features**
- Dynamic and scalable Python code for email generation.
- Filter emails based on country, state, city, college, department, and year.
- Ability to generate a specified number of email IDs per department.
- Organized Excel-based data management for easy updates and scalability.

---

## **Technologies Used**
- **Python** for dynamic email generation
- **Pandas** for Excel data handling
- **Excel** as the structured data input
- **Streamlit** for Visualizing the site

## **Future Scope**
- The generated email IDs can be **stored in a database**, allowing:
  - Bulk emailing to students simultaneously.
  - Integration with mailing systems for announcements or notifications.
- The dataset can be used in **Data Science projects** for:
  - Predicting email patterns.
  - Analyzing student distribution across colleges, departments, and regions.
  - Generating insights like department size, college popularity.
  - Machine Learning models for automating email ID suggestions and duplicate detection.
- Can be extended to build a **student communication platform** or **analytics dashboard**.


