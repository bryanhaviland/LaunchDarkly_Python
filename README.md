# LaunchDarkly_Python
Sample Python script with LaunchDarkly toggles

This script will take 5 files from an "Old" directory and rename and move them to a "New" directory.  The feature flag that is being used will change the "New" path from being a hard plugged destination to opening a Windows Explorer menu for the use to select where to save the files.  The feature has been activated, but if you toggle the feature to off (which I am hoping you have access to) you can see it will revert back to using the hard plugged path.  

Build Instructions 

1. Download the "Old" directory - it has sample files to show the program is working.  Additionally, please also create a new empty Directory entiled "New"

2. Run pip install requirements.txt

3. In rename_files.py add the location of the directories you have created for both the "Old" and "New" directories. (The only comments in the script are at fields that should be edited by user).

4. For tracking purposes please edit the user's first name, last name, and email 

5. Run rename_files.py - the feature flag is active so a window will open to select the directory to save the new files in


Reset to Test Again 

1. Re-download the Test Files from GitHub to the previously created "Old" directory

2. If using the same directory for "New" please delete the previously created new files.  Any files not removed will not create/overwrite the previous

3. Turn the feature flag off at LaunchDarkly- the code will now use your hard plugged path to save the files

4. Run rename_files.py
