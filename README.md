# Election_Analysis

## Project Overview
I was assigned the task of auditing an election that was held for the U.S. House District 1 candidate of Colorado. The following specifications were required to be fulfilled

1. Calculate the total amount of votes that were cast for this election.
2. Determine how many candidates ran in the election and to list their names.
3. Calculate the total amount of votes for each candidate.
4. Calculate the percentage of total votes each candidate received.
5. Determine the winner of the election based on the calculated data.
6. Display all this information in a text file.

## Election-Audit Results

![Challenge3_Analysis_Results](https://user-images.githubusercontent.com/78178900/112743278-72750680-8f5b-11eb-8eb0-f8461e9da66e.png)

The total amount of votes that were cast in the congressional election was 369,711.

### County Voting Analysis
There are three total counties that are in district 1 of Colorado. Arapahoe county, Denver county, and Jefferson county. Here is each county total voter turnout and what their percentage of overall vote was:

  - Arapahoe county
  	- Voter turnout was 24,801
  	- Percent of total vote was 6.7%
  - Denver county
  	- Voter turnout was 306,055
  	- Percent of total vote was 82.8%
  - Jefferson county
  	- Voter turnout was 38,855
  	- Percent of total vote was 10.5%

From this we can clearly see that the county with the largest number of votes was Denver county.

### Candidate Voting Analysis

Just as there were three counties in the district, there were three congressional candidates running in the election. Here are their names, total votes, and what percent their total votes were of the overall votes cast.

  - Charles Casper Stockham
  	- Received 85,213 votes.
  	- Percent of total vote was 23.0%
  - Diana DeGette
  	- Received 272,892 votes.
  	- Percent of total vote was 73.8%
  - Raymon Anthony Doane
  	- Received 11,606 votes.
  	- Percent of total vote was 3.1%

The winner of the election was:
  - Diana DeGette who received 73.8% of the total votes cast with 272,892 votes and winning the race by 187,679 votes: more than tripling the number of votes from the runner up.

## Election-Audit Summary

We can clearly see who the winner of the election is, and which county had the largest voter turnout. This can also be valuable to future candidates who want to run for this position because it is an indicator that you may want to focus your campaigning on the Denver county since they are the county with the largest voter turnout. 

The script that was written to perform analysis on this election is also quite handy because it can be used for future election auditing. With a few minor adjustments you can use this for similar datasets in the future. If next election, you have the same data sheet, but the data are in different columns you only need to change the index values for counting the "candidate_name" on row 50 of the code and for counting the "county_name" on line 53 of the code. With the proper index values, it should output the same results as we received here, only with the new election data.

Even if the data included another column that you may not care about such as, polling station votes that are located inside of the county, you can still use the code by making certain the index values mentioned above are attributed correctly. Remember that python counts starting from zero and left to right. So, if the candidate names are in the first column of the new election data then you would need to change the index value on line 50 from "2" to "0". 

Similarly, if you wanted to use this script to audit a national election of the United States and see how many states there were and who had the most voter turnout then you would want to change any variable with the word "county" to "state". Making these minor adjustments to the script can make your life easier next time you want to audit a different data set for an election.

One last note is that you would want to change the file path on line 10 to align with the correct file in your working directory so it is not still trying to reference the csv file from this election audit. Then one final note is that since our code on line 12 is creating a text file to be saved inside of the "analysis" folder, you will want to make certain that you always create an "analysis" folder OR create a new folder with a different name and ensure you change the code on line 12 from "analysis" to the name of your new folder. This way, python will know where to create that text file for you. Otherwise, you will get an error code because it is looking for the "analysis" folder inside your working directory to create and save a text file to.

#### Resources
  - [election_results.zip](https://github.com/K-Beadle/Election_Analysis/files/6216768/election_results.zip)
  - Python Version 3.7.6 and Version 3.8.5 through Visual Studio Code terminal
  - Visual Studio Code version 1.54.3
