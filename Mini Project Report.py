#!/usr/bin/env python
# coding: utf-8

# <img src="uia logo.png" alt="Logo" width="800" style="display: block; margin-left: auto; margin-right: auto;"/>
# 
# 
# <h3 align="center"><strong>KULLIYYAH OF SCIENCE</strong></h3>
# 
# ---
# 
# <h3 align="center">INTRODUCTION TO DATA ANALYTICS (BSMS 1306)</h3>
# 
# <h1 align="center">Dataset: Students' Social Media Addiction</h1>
# 
# ---
# 
# <h4 align="center"><strong>Group Members</strong></h4>
# 
# <div align="center">
# 
# <table>
#   <tr>
#     <th>Name</th>
#     <th>Matric Number</th>
#     <th>Section</th>
#   </tr>
#   <tr>
#     <td>Nur Aleya Nasywa Binti Hasbuna Ridzuan</td>
#     <td>2418402</td>
#     <td>02</td>
#   </tr>
#   <tr>
#     <td>Nik Nur Alia Syazni Binti Nik Mazri</td>
#     <td>2413956</td>
#     <td>02</td>
#   </tr>
# </table>
# 
# </div>
# 
# ---
# 
# <h4 align="center"><strong>Lecturer’s Name</strong>: Asst. Prof. Dr. Nor Raihan Binti Mohamad Asimoni</h4>  
# <h4 align="center"><strong>Date of Submission</strong>: 8th of June 2025</h4>

# ## INTRODUCTION

# Social media has become deeply embedded in student life, influencing their routines, mental well-being, and academic performance. This project aims to analyze patterns of social media usage among students and assess its impact through key indicators such as addiction score, mental health status, sleep hours, and platform preference. An interactive dashboard was developed using Streamlit to visualize trends and relationships across different demographics, enabling a clearer understanding of how digital behavior may shape students’ daily lives.

# ## OBJECTIVE

# 1. To examine the relationship between social media addiction level and their mental health status
# 2. To understand the daily usage pattern of social media among students
# 3. To compare addiction levels across genders
# 4. To identify the most preferred social media platforms among students
# 5. To determine how daily social media use impacts sleep hours
# 6. To examine the academic impact of different social media platforms 
# 
# To support a more detailed analysis, all objectives are explored using filterable data by **gender**, **academic level**, and **relationship status**. These filters are available in the sidebar of the interactive Streamlit dashboard, allowing users to view results specific to different subgroups.

# In[26]:


import pandas as pd
data = pd.read_csv('Students Social Media Addiction.csv')
data.head()


# In[27]:


data


# ## DATA PREPARATION

# In[28]:


data.info() #to show the info for this data. able to find null and determine data type


# In[29]:


data.isnull().sum() #show the number of missing values in each column


# ## DISCUSSION

# In[30]:


# Calculate KPIs
avg_addiction_score = data['Addicted_Score'].mean()
avg_daily_usage = data['Avg_Daily_Usage_Hours'].mean()
avg_mental_health = data['Mental_Health_Score'].mean()
total_students = len(data)

# Print KPIs
print("📊 Key Performance Indicators (KPIs)")
print("------------------------------------")
print(f"📱 Average Addiction Score     : {avg_addiction_score:.2f}")
print(f"⏰ Average Daily Usage (hours): {avg_daily_usage:.2f}")
print(f"🧠 Mental Health Score         : {avg_mental_health:.2f}")
print(f"👥 Total Students Surveyed     : {total_students}")


# In[31]:


import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.io as pio
pio.renderers.default = 'notebook'


# In[32]:


# bar chart (not shown in final dashboard)
gender_counts = data['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']  # rename for clarity

fig = px.bar(gender_counts, x='Gender', y='Count',
             title='Number of Students by Gender',
             color='Gender',
             color_discrete_map={
        "Female": "#FADADD",  # Light pastel pink
        "Male": "#B0E0E6"     # Light pastel blue
    },
    template='plotly_white'
) # optional: color by gender

fig.show()


# The chart shows that there is a slightly higher number of female students compared to male students in the survey just a difference by 1. This gender imbalance should be considered when interpreting results, as it may influence patterns observed in usage, addiction, and other behavior-related metrics. This chart not shown in final chart but it helps to understand the demographic distribution of the dataset.

# In[33]:


#1
fig = px.scatter(data, 
                 x="Addicted_Score", 
                 y="Mental_Health_Score",
                 color="Gender",  
                 title="Addiction Score vs Mental Health Score",
                 labels={"Addicted_Score": "Addiction Score", "Mental_Health_Score": "Mental Health Score"
                        },
    color_discrete_map={
        "Female": "#FADADD",  
        "Male": "#B0E0E6" },    
    template='plotly_white' )
fig.show()


# The scatter plot shows a negative correlation between adiction score and Mental Health Score. As students addiction to social media increases, their mental health scores tend to decrease. This indicates that higher social media addiction may be linked to poorer mental well-being. Thus, the objective examine the relationship between students social media addiction levels and mental health is achieved.

# In[34]:


#2
fig = px.histogram(data, 
                   x='Avg_Daily_Usage_Hours',  # Use the correct column name here
                   title='Distribution of Average Hours on Social Media',
                   nbins=10,
                   template='plotly_white',
        color_discrete_sequence=['#FFDDEE'])
fig.show()


# The histogram shows how many students spend different amounts of time on social media each day. Most students use social media between 4 to 6 hours daily, indicating high usage is common. Very few students use it less that 2 or more than 8 hours daily. The objective to understand the daily usage pattern of social media among students is successfully achieved.

# In[35]:


# pie chart (not used in final dashboard)
academic_counts = data['Academic_Level'].value_counts().reset_index()
academic_counts.columns = ['Academic_Level', 'Count']

pastel_colors = [
    "#FFD1DC", "#AEC6CF", "#FFB347", "#B39EB5",
    "#AAF0D1", "#ACE1AF", "#CBAACB", "#FF6961"
]

# Create the pie chart
fig = px.pie(academic_counts, 
             values='Count', 
             names='Academic_Level', 
             title='Academic Level Distribution',
             color_discrete_sequence=pastel_colors,
    template='plotly_white')


# Show the interactive chart
fig.show()


# The pie chart displays the distribution of students by academic level, showing that undergraduate students make up the largest portion, followed by graduate and high school students.
# This indicates that the findings of the analysis are most representative of the undergraduate population, which should be considered when interpreting overall trends. However, this pie chart not included in in final dashboard.

# In[36]:


# donut chart (not used in final dashboard)
donut_data = data['Addicted_Score'].value_counts().reset_index()
donut_data.columns = ['Addicted_Score', 'Count']

pastel_colors = [
    "#FFD1DC", "#AEC6CF", "#FFB347", "#B39EB5",
    "#AAF0D1", "#ACE1AF", "#CBAACB", "#FF6961"
]

fig = px.pie(donut_data, values='Count', names='Addicted_Score',
             title='Addiction Level Distribution',
             hole=0.4,
             template='plotly_white',
    color_discrete_sequence=pastel_colors)
fig.show()


# The chart shows that moderate to high addiction scores (particularly scores between 6 and 9) are the most common, indicating that a significant number of students experience notable levels of social media dependency. This donut chart, although not used in the final dashboard, provides insight into the overall distribution of social media addiction levels among students.

# In[37]:


#3
fig = px.histogram(data, 
                   x='Addicted_Score',  # Correct column name
                   color='Gender',
                   barmode='group',
                   title='Addiction Level by Gender',
                   color_discrete_map={
        "Female": "#FADADD",  # Light pastel pink
        "Male": "#B0E0E6"     # Light pastel blue
    },
    template='plotly_white'
)
fig.show()


# The grouped histogram shows the distribution of Addicted Scores by Gender. Both males and females have a wide range of addiction levels, but higher scores (7-9) are more common. This suggests that social media addiction is prevalent among students of both genders, with slightly in variations. The objective to compare addiction levels across gender is attained.

# In[38]:


#4
platform_counts = data['Most_Used_Platform'].value_counts().reset_index()
platform_counts.columns = ['Platform', 'Count']

# Pastel color palette
pastel_colors = [
    "#FFD1DC", "#AEC6CF", "#FFB347", "#B39EB5",
    "#AAF0D1", "#ACE1AF", "#CBAACB", "#FF6961"
]

# Create pie chart
fig = px.pie(
    platform_counts,
    names='Platform',
    values='Count',
    title='📌 Most Used Social Media Platforms',
    template='plotly_white',
    color_discrete_sequence=pastel_colors
)

# Display in Jupyter
fig.show()


# This pie chart shows the most popular social media platforms among students. Instagram and Tiktok appear as the top choices, followed by platform like Youtube, Facebook and Twitter. This indicates that visual and short-form content platforms are the most preferred by students. Thus, the objective to identify the most preferred social media platfroms among student is achieved.

# In[39]:


#5
fig = px.scatter(data, 
                 x="Avg_Daily_Usage_Hours", 
                 y="Sleep_Hours_Per_Night",
                color="Gender",
                 size='Addicted_Score',
                 title="Daily Social Media Usage vs Sleep Duration",
                 labels={
                     "Avg_Daily_Usage_Hours": "Average Daily Social Media Usage (Hours)",
                     "Sleep_Hours_Per_Night": "Sleep Duration per Night (Hours)"
                 },
    color_discrete_map={
        "Female": "#FADADD",  
        "Male": "#B0E0E6"     
    },
    template='plotly_white'  
)
fig.show()


# The scatter plot shows a negative relationship between average daily social media usage and sleep hours for both female and male students. As students spend more time on social media, they tend to sleep less hours. This pattern suggests that excessive social media use may interfere with students sleep routines, potentially affecting their overall health and academic performance. Thus, The objective to determine how daily social media use impacts sleep hours is achieved.

# In[40]:


#6
academic_data = pd.crosstab(
    data['Most_Used_Platform'],
    data['Affects_Academic_Performance']
).reset_index()

melted = academic_data.melt(
    id_vars='Most_Used_Platform',
    var_name='Impact',
    value_name='Count'
)

fig = px.bar(
    melted,
    x="Most_Used_Platform",
    y="Count",
    color="Impact",
    barmode="stack",
    title="🎓 Academic Performance Impact by Platform",
    template='plotly_white',
    color_discrete_map={
        'Yes': '#FFA6A6',  
        'No': '#FFFDD0'    
    },
    hover_data=melted.columns
)

fig.update_layout(xaxis_tickangle=-45)

fig.show()


# The stacked bar chart shows how many students using each platform report an impact on their academic performance. TikTok and Instagram users have a higher proportion reporting that social media affects their academics, while YouTube and Facebook users show a more even or lower impact. This indicates that high-engagement platforms may be more disruptive to academic focus. Thus,the objective to examine the academic impact of different social media platforms is successfully achieved.

# In[41]:


#box plot (not used in dashboard)
fig = px.box(data, x='Avg_Daily_Usage_Hours', y='Gender',
             title='Social Media Usage by Gender',)
fig.show()


# The chart shows the distribution of daily usage hours for male and female students.
# Both genders have similar usage patterns, but the median usage for females appears slightly higher, with a wider spread. This shows that female students on average, spend slightly more time on social media, though the difference is not drastic. This chart is not used in my final dashboard.

# In[42]:


correlation_data = data[[
    'Addicted_Score', 
    'Mental_Health_Score', 
    'Avg_Daily_Usage_Hours', 
    'Sleep_Hours_Per_Night', 
    'Conflicts_Over_Social_Media']]

corr_matrix = correlation_data.corr().round(2)

corr_long = corr_matrix.reset_index().melt(id_vars='index')
corr_long.columns = ['Metric 1', 'Metric 2', 'Correlation']

fig = px.imshow(
    corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.index,
    color_continuous_scale='purples',
    text_auto=True,
    aspect='auto',
    title='Correlation Between Key Metrics')

fig.update_layout(
    width=700,
    height=500)

fig.show()


# The analysis shows a strong negative correlation between Addicted Score and Mental Health Score (−0.95), indicating that students with higher social media addiction levels tend to give lower mental health. There is also a strong positive correlation between Addicted Score and Conflicts Over Social Media (0.93), suggesting that higher addiction is associated with more frequent social conflicts. Additionally, daily usage hours positively correlate with Addicted Score (0.83) and negatively with Sleep Hours (−0.79), highlighting that students who spend more time on social media tend to sleep less. These patterns reinforce the conclusion that excessive social media use may negatively impact both mental health and sleep habits among students.

# ## Streamlit Python source code 

# https://miniproject-nasywadannik.streamlit.app/

# ## CONCLUSION

# This project successfully achieved all its objectives by analyzing students social media usage and its impact. The findings show that higher addiction levels are linked to lower mental health scores and reduced sleep duration. Platforms like TikTok and Instagram are more associated with negative academic effects. Most students reported using social media for 4 to 6 hours daily. Although some charts were not included in the final dashboard, they helped support deeper understanding. Overall, the analysis highlights how excessive social media use can affect students well-being and academic performance. An interactive Streamlit dashboard was developed to present these insights clearly and allow users to explode patternd through filters and visualizations.
