# Load required library
library(readr)

# Set the URL for the data file
url <- "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

# Download the CSV file from the Internet
data <- read_csv(url)

# View initial lines of the data to understand its structure
head(data)

# Generate descriptive statistics for each column
summary(data)

# For thorough analysis we will use  package's  function
# It provides more descriptive stats compared to summary function

# load the library
library(psych)

# generate rich descriptive statistics
rich_desc = describe(data)

# print the result
print(rich_desc)

