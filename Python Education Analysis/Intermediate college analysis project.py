import pandas as pd

# Load the dataset
file_path = 'D:\All the Intermediate Colleges in Pakistan.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataset
df.info()

# Display the first few rows of the dataset
df.head()
# Fill missing values in 'Location' and 'Sector' with 'Unknown'
df['Location'].fillna('Unknown', inplace=True)
df['Sector'].fillna('Unknown', inplace=True)

# Drop rows where 'Affiliation' is missing
df.dropna(subset=['Affiliation'], inplace=True)

# Convert 'Rating' to numerical
df['Rating'] = df['Rating'].str.extract('(\d+)').astype(float)

# Display the cleaned dataset information
df.info()

# Display the first few rows of the cleaned dataset
df.head()
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Plot the distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=10, kde=True)
plt.title('Distribution of College Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot the distribution of Colleges by Sector
plt.figure(figsize=(10, 6))
sns.countplot(x='Sector', data=df)
plt.title('Distribution of Colleges by Sector')
plt.xlabel('Sector')
plt.ylabel('Count')
plt.show()

# Extract the city from the Location for regional analysis
df['City'] = df['Location'].apply(lambda x: x.split(',')[0])

# Plot the distribution of Colleges by City
plt.figure(figsize=(15, 8))
top_cities = df['City'].value_counts().head(10).index
sns.countplot(y='City', data=df[df['City'].isin(top_cities)], order=top_cities)
plt.title('Top 10 Cities with the Most Colleges')
plt.xlabel('Count')
plt.ylabel('City')
plt.show()

# Plot the distribution of Study Programs
plt.figure(figsize=(15, 8))
study_programs = df['Study Program'].str.split(expand=True).stack().value_counts().head(10)
sns.barplot(x=study_programs.values, y=study_programs.index)
plt.title('Top 10 Study Programs Offered')
plt.xlabel('Count')
plt.ylabel('Study Program')
plt.show()
