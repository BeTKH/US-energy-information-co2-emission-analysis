# This code file should contain API calls required to get the statewide CO2 emissions for 2019.
# The problem should be able to run by the instructor using 'python ingestREST.py' (with their own API key).
# Store your key in a file with a .config appendix to avoid accidental check-in (.gitignore is setup to ignore .config)

# Assignment problems:
#   1a) [DONE] Code the REST API to get the 2019 state level total CO2 emissions from https://www.eia.gov/.
#       Hint:  Use https://www.eia.gov/opendata/browser/ to develop your query.
#       Hint:  You'll want to set the sectorID to 'TT' (Total carbon dioxide emissions from all sectors)
#               and the fuel ID to 'TO' (All fuels)
#   1b) [DONE] Save the data to a CSV file to 'data\CO2\TotalEmissionsByState2019.csv'.
#
#
#   2a) Code the REST API to get the 2019 state level total CO2 emissions for Coal.
#   2b) Save the data to a CSV file to 'data\CO2\CoalEmissionsByState2019.csv'.
#
#   3) Answer the questions shown below by replacing YourAnswer and executing the code to save the file.

# Points for this file:
#   - Part 1:  12 points
#   - Part 2:  12 points
#   - Part 3:  6 points

print("IngestREST problem")

# Questions - replace YourAnswer with your answer for each question.
with open("Data/CO2/EvaluateND.CSV", "w") as file:
    header = "Question | Answer"
    file.write(header + "\n")

    # Question 1
    q1 = "What is the ND state rank in total emissions (high to low)? | " + \
        "YourAnswer"
    file.write(q1 + "\n")

    # Question 2
    q2 = "What is the ND state rank in coal emissons (high to low)? | " + \
        "YourAnswer"
    file.write(q2 + "\n")

    # Question 3
    q3 = "What is your perpective on how ND is doing with respect to CO2 emissions given the data above along with other insight you might have? | " + "YourAnswer"
    file.write(q3 + "\n")
