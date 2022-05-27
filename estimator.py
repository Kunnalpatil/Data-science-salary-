import streamlit as st
import pickle
import pandas as pd


st.set_page_config(page_title="Salary Estimator", page_icon=":moneybag:", layout="wide")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("This is a salary estimator for data science roles")
        st.subheader("Project Overview")
        st.write("Created a salary Estimator for data science job roles using data from glassdoor.")
        st.write(""" Engineered features from the text of each job description to quantify the salaries
                  companies put on python, excel, aws, and spark.""")
        st.write(" Optimized Lasso Regession and RandomForestRegressors using RandomsearchCV to reach the best model.")

        st.markdown(":link:[**Github Repository**](https://github.com/Kunnalpatil/Data-science-salary-)")
    with right_column:
        st.empty()
        # st.write("##")
        # st.subheader("Below are the features it uses to estimate the salary")
        # st.write("""
        #        - Size
        #        - Type of ownership
        #        - Job role
        #        - seniority
        #        - age of company
        #        **SKILLS:**
        #        - R
        #        - python
        #        - excel
        #        - aws
        #        - spark
        #             """)

st.write('----')
st.subheader("Enter values to estimate the salary")
with st.container():
    left_col,mid_col,right_col = st.columns(3)
    with left_col:
        st.subheader("Chose the size of company")
        num_of_employes = st.selectbox("Number of employes",['Unknown', '10000+ employees',
          '5001 to 10000 employees',
           '1001 to 5000 employees','501 to 1000 employees',
           '201 to 500 employees','51 to 200 employees',
           '1 to 50 employees'],index = 0)

    with mid_col:
         st.subheader("Chose the Type of ownership")
         company_type = st.selectbox("Type of company",['Unknown','Private',
                         'Other Organization', 'Government',
                       'Public', 'Hospital', 'Subsidiary or Business Segment',
                       'Nonprofit Organization','College/University',
                       'School/School District'], index = 0)

    with right_col:
         st.subheader("chose job role")
         job_role = st.selectbox("Job role",['data scientist', 'na',
          'data analyst', 'data engineer', 'data science director',
          'data science manager', 'machine learning engineer'])

with st.container():
    left_column,mid_column,right_column = st.columns(3)
    with left_column:
        st.subheader("Chose the level you are offered")
        seniority = st.selectbox("Level",['na', 'senior', 'jr'])

    with mid_column:
         st.subheader("How old is the company")
         age = st.slider("Years",min_value = 1,max_value=100,value = 10,step = 2)

    with right_column:
        st.subheader("Chose your skills")
        skills = st.multiselect("Skills(can select multiple skills)",["python","R","spark","aws","excel"])

#---------------- Backend --------------------------

#----- code For skills----------
k = [0,0,0,0,0] #["python","R","spark","aws","excel"]
for i in skills:
    if i == "python":
        k[0]=1
    if i == "R":
        k[1]=1
    if i == "spark":
        k[2]=1
    if i == "aws":
        k[3]=1
    if i == "excel":
        k[4]=1


#------------code for company size-------------------
comp_size = [0,0,0,0,0,0,0,0,0]
def employe_count(num_of_employes):
    ''' function for modifying  comp_size'''
    if num_of_employes == 'Unknown':
        comp_size[0]=1
    elif num_of_employes == '10000+ employees':
        comp_size[1]=1
    elif num_of_employes == '5001 to 10000 employees':
        comp_size[2]=1
    elif num_of_employes == '1001 to 5000 employees':

        comp_size[3]=1
    elif num_of_employes == '501 to 1000 employees':
        comp_size[4]=1
    elif num_of_employes == '201 to 500 employees':
        comp_size[5]=1
    elif num_of_employes == '51 to 200 employees':
        comp_size[6]=1
    elif num_of_employes == '1 to 50 employees':
        comp_size[7]=1
    return comp_size

employe_count(num_of_employes)



#------------code for Type of ownership-------------------

ownership=[0,0,0,0,0,0,0,0,0,0,0]
def ownership_type(company_type):
    if company_type =='Unknown':
        ownership[0]=1
    elif company_type =='Private':
        ownership[1]=1
    elif company_type =='Other Organization':
        ownership[2]=1
    elif company_type =='Government':
        ownership[3]=1
    elif company_type =='Public':
        ownership[4]=1
    elif company_type =='Hospital':
        ownership[5]=1
    elif company_type =='Subsidiary or Business Segment':
        ownership[6]=1
    elif company_type =='Nonprofit Organization':
        ownership[7]=1
    elif company_type =='College / University':
        ownership[8]=1
    elif company_type =='School / School District':
        ownership[9]=1

ownership_type(company_type)

#-------------job role------------------

# ['data scientist', 'na',
#  'data analyst', 'data engineer', 'data science director',
#  'data science manager', 'machine learning engineer'])

role = [0,0,0,0,0,0,0]

if job_role=='data scientist':
    role[0]=1
elif job_role=='na':
    role[1]=1
elif job_role=='data analyst':
    role[2]=1
elif job_role=='data engineer':
    role[3]=1
elif job_role=='data science director':
    role[4]=1
elif job_role=='data science manager':
    role[5]=1
elif job_role=='machine learning engineer':
    role[6]=1


#-------------seniority------------------

#seniority = st.selectbox("Level",['na', 'senior', 'jr'])
level =[0,0,0]
if seniority=='na':
    level[0]=1
elif seniority=='senior':
    level[1]=1
elif seniority=='jr':
    level[2]=1



#---------------------data for prediction

data =[[age,k[0],k[1],k[2],k[3],k[4],
comp_size[0],comp_size[1],comp_size[2],comp_size[3],comp_size[4],
comp_size[5],comp_size[6],comp_size[7],comp_size[8],
ownership[0],ownership[1],ownership[2],ownership[3],ownership[4],
ownership[5],ownership[6],ownership[7],ownership[8],ownership[9],ownership[10],
role[0],role[1],role[2],role[3],role[4],role[5],role[6],
level[0],level[1],level[2]
]]


#------ importing model-------------
model = pickle.load(open('Salary_predictions.pkl', 'rb'))
if st.button("Predict"):
    pred = model.predict(data)[0]
    st.success(f"The estimated salary is ${round(pred,2)}")
