## Readme for content organizer script

- This will start off as a set of notes on what I want this script to do

1. Script is running all the time or maybe every 5-10 minutes on a schedule

2. It's monitoring a specific folder and waiting for certain filetypes

3. Conditionally, I would like this script to move things to my ZFS pool 

4. Based on the file extension, it should get sorted to a specific folder

5. It get's more complicated than that though. In the case where it is an mkv/mp4, we want to scan the file for information. Based on this information, we decide to either put it in an existing folder on target that is the correct season in the correct tv show folder.  
    - use cases: tv show with seasons... check if there is a folder on the other side for the season, if not, then based on the naming scheme (S01, s01, s1, S1, season1 etc...)
    - movie, we want to have it in a folder with the movie's year (this might be too much to ask, but maybe we search a movied db with our movie name? and retrieve a year)
    - .... pdfs, audiobooks, music we can have functionality for each.  

6. We setup an rsync function that get's triggered here or something like this for python and then log to a file so we know what's been transferred successfully



