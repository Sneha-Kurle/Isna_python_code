# Isna_python_code
#Working with Git
#Pushing code from local machine to Git
1. Create a folder to store the python files of the code in VS code, write and run the code.
2. Create an empty repository in remote Git. (Git Profile->Your repositories->New)
3. To push the code from local machine to remote git, create an local git file in vs code
                   **>> git init**     #Innitialise the git file in local
4. Selecting a files of code which needs to be push
                   **>> git add .**   #Add all modified and new files (in the current directory and all subdirectories) to the staging area( contains the files that needs to be committed) and . represent all fiels in current directory
5.Commit the changes.
 Commit is taking a snapshot of the staged files so that Git can remember what they looked like at that point in time.
 Finalising..
                   **>> git commit -am "Your message here"**
6. Connect your local Git repository to a remote repository
                   **>> git remote add origin https://github.com/user/repo.git**
   git – the Git command-line tool
   remote – refers to remote repositories (ones not on your local machine)
   add – tells Git you want to add a new remote connection
   origin – this is the name you give the remote (usually "origin" by default)
   https://github.com/user/repo.git – this is the URL of the remote repository

7. Pushing the code
   Upload your local commits to the remote repository, specifically to the main branch of the remote named **origin**.
                   **>> git push origin main**
  
