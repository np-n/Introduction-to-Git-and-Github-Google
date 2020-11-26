## --------------- Week 1 : Into to Version Control --------------------

#### To find difference between two files
`diff <first_file_name.extension> <second_file_name.extension>`<br>
Alternatively<br>
`diff -u <first_file_name.extension> <second_file_name.extension>`
(<.....> indicates file name)

#### To find differnce/compare words in files
`wdiff <first_file_name.extension> <second_file_name.extension>`

#### To save line differences between two files into file
`diff -u <first_file> <second_file> > <diff_file_name.diff>`

#### To apply changes from diff file to old file(where errors occurs/needs to chage)
`patch <file_name.extension> < <diff_file_name.extension>`(All changes are applied to <file_name.extension>)

#### To copy content of file/ to create duplicate file with similar content
`cp <original_file_name.extension> <duplicate_file_name.extension>`

#### To find all directory with more info(with all hidden files and folders)
`ls -la`

#### To get files with .extension
`ls -l .extension/ (example: ls -l .git/)`

#### To copy <file> to subdirectory from directory
`cp ../<file> .  (To do that you must be in subdirectory)`

#### To commit your changes
`git commit ` (It open default text editor where you can write commit message)

#### Any git projects consist of
- Git directory
- working directory
- staging area

#### Git tracks files in following manner
- First files are modified when we changed it
- Then it becomes staged when we mark those changes for tracking
- It will get commited, when we want to store those changes in VCS
 File stage/cycle - modified, staged,committed

#### To see git configuration in git project
`git config --l`

#### To see what changes are done in a file(example a.extension)
`git diff a.extension`(just after modification before adding modified files for tracking)

#### If you are using git first time tell git who you are
```
git config --global user.name ="<your_username>"
git config --global user.email ="<your_email>"
```

#### To initialize git/git working directory
`git init`

#### To stage/Track file
`git add <file_name.extension>`

#### To track all files
`git add .`


#### To untrack/unstage file, which is already staged but not commited
```
git restore --staged <file_name.extension>
git reset HEAD <file_name.extension>
```

#### To restore/unstage all file and folders
`git restore --staged .`

#### To create snapshot/repository of your changes
`git commit`   (prompts default text editor,you can write multiline comments)<br>
`git commit -m "< write your commit message here>"`


## -------------------- Week 2 : Using Git locally ------------------------------

#### To track changes in tracked files and commit in single steps
`git commit -a`  (Doesn't work for new files which are not tracked yet,opens in default text editor)<br>
`git commit -a -m "<write your commit message>"`

#### To see past changes history/commit
`git log`

### To see n latest commit/log
`git log -n`

#### To see all changes in commit/associated patches
`git log -p`

#### To see all patches in n commits
`git log -p -n`

#### To see specific changes in a commit
`git show <commit_id>`  (<commit_id> is identifier associated with each commit)

#### To see status of changes/commit
`git log --stat`

#### To see commit as graph
`git log --graph`

####  TO display a summarized view of the commit history for a repo, showing one line per commit
`git log --graph --oneline`

#### To see changes before starting file tracking/staging file
`git diff ` (for all changes)<br>
`git diff <file_name> ` (for specific changes in <file_name> file)

#### To see changes that are staged/tracked but not commited
`git diff --staged`

#### To delete file from repository
`git rm <filename.extension> `  (file <filename.extension> will be deleted from your repository)

#### To rename files in the repository
`git mv <a.extension> <b.extension> `(<a.extension> file name is renamed as <b.extension>)<br>
(Note: mv command is also used to move files/folder in linux)

#### To escape or avoid file in ropository
write file name  inside .gitignore file<br>
Example<br>
To ignore readme.txt file<br>
`echo readme.txt > .gitignore`

#### To discard changes in the working directory/file, if file is not tracked yet
`git checkout <file_name.extension> `(old approach)<br>
`git restore <file_name.extension> `(new approach)<br>
(Restore file to last staged/tradked state)

#### TO change commit message
`git commit --amend`

### How to fix staged/unstage changes, how to fix the commit that was incomplete
`git add <file_name.extension>`  (add or unstage file )<br>
or<br>
`git add .`<br>
Fillowed by<br>
`git commit --amend `  (can change commit in editor)

#### To revert/go back to last snapshot/repository, because current changes in repo produce error
`git revert HEAD `  (creates new commit with inverse changes, add reason for rollback in commit)

#### To rollback to specific snapshot
`git revert <commit_id_for_snapshot>`


### Branch
#### To see available branch
`git branch `  (current branch is indicated by *)

#### To create new branch
`git branch <new_branch_name>`

#### To enter into branch
`git checkout <new_branch_name>`<br>
Note: Before you checkout branch you need to save/commit your changes

#### To create and enter new  branch into single command
`git checkout -b <new_branch_name>`

#### To delete git branch
`git branch -d <branch_name>`<br>
Note: to delete branch you must be in master branch

#### To delete git branch forcefully  without merging/saving changes in branch
`git branch -D <branch_name>`

#### To merge branch
`git merge <merging_branch_name> `
Note: to merge you must be in your destination branch

#### Two type of git merging algorithms:
- fast forward merge
- three way merge

#### To abort/cancel merge
`git merge --abort`


## --------------------- Week3 : Working with Remotes ----------------------

Basic Interaction with Github:
1. Create new github repository
- Create your account and login to it,
- click on create repository link or plus sign,
- Name repository,
- Add description to repo and is optional,
- Select visibility for repo that is either private or public,
- initialize repo with README,
- Then click on create repository

2.
i. Clone repo make changes and again push to remote
- open your terminal and enter command
`git clone <REPO_HTTPS_URL>`
- Enter username and password for your github account
- Directory with repository name is created in your local computer
- README.md file is present inside your repo folder
- Edit file
- Stage changes and commit changes
`git commit -a -m 'your commit message'`
- Then push your modified local repo to github using  
`git push`or`git push -u origin main` or `git push origin main`

ii. If you want to push your local repository to existing repository
- To initialize git working directory use `git init`
- If you have README.md file in remote repository then create that file on local repo too using `touch README.md` or
<br> `echo "# <your_repo_name> " >> README.md`
- To track/stage file `git add <file_name>` for single file <br>
or `git add .` for all files
- To make snapshot/version of your changes use `git commit -m '<commit_message>'`<br>
or `git commit ` enter good commit from default text editor
- To stage and commit use `git commit -a -m` or `git commit -a`
- To add remote url as origin use `git add remote origin <REPO_URL>`
- To push your repo to github main branch use `git push -u origin main`
- To push your repo to github <branch_name> branch use `git push -u origin <branch_name>`

3. To avoid repeated username and password entry:
- Use SSH Key-pair or,
- Use Credential Helper
`git config --global credential.helper cache`
Note : You need to enter your credential one more time  and your credentials are cached for next 15 minutes
<br>
4.  retrieve new changes from remote and merge to local repository using  
`git pull ``  

5. To see status of the remote repository
`git status` ( we have clone remote repo, thus `git status` shows status of remote repository)

#### To see remote configuration(url associated with origin remote) of your repository
`git remote -v`

#### To get more information about remote
`git remote show origin`

#### To see remote branches that git repo is currently tracking
`git branch -r`

#### To download and review the changes/commits happens in the remote repository(to local)
`git fetch`

#### To see the log/history of the remote changes
`git log origin/<branch_name>`(exanple: `git log origin/main` ,`git log origin/master`)

#### To merge the remote changes in branch to local branch
`git merge origin/<branch_name>`

#### To fetch current repository from remote branch and merge it to local branch
`git pull`

#### To see any changes in files in n commit
`git log -p -n`

#### To see if your local repository is up to date with remote
`git status`

#### To see all branches information about Remotes
`git remote show origin`

#### If there was any branch added in remote repository
`git checkout <branch_name>` (This will create copy of remote branch to local)

#### To add file and see changes in file
`git add -p`

#### To see all the commits in oneline
`git log --graph --online --all`

### Merge conflicts
- If same line or same section of the file is already changed and committed in both remote branch and
local branch,And then if you will try to push the local branch on the remote branch where file is already changed
<br>Then it will throw merge conflict.
- To solve merge conflict:<br>
- first pull your remote repository to merge remote changes to local
`git pull`
- It will throw merge conflict message , for file which has been changed from  both remote and local
- This merge is tree way merge, because file are changed in both repo (if file is changed in only one repo, then merge will be fast forward merge)
- Open file in text editor in which merge conflict arises
- Where you can find <<<<<<<, =======, and >>>>>>> conflict markers
- Remove all of the conflict markers and only leave the code as it should be after the merge and save it.
- Then stage that file using `git add .` or `git add <file_name>`
- Then commit changes using `git commit` where commit is already written, if you wish all more explanation.
- Then push your local merged version to remote using `git push`


#### To create new repository, add changes and push to Remote
- git checkout -b <branch_name>(creates branch <branch_name> and switched to <branch_name>)
- Do changes as your requirements
- Stage your changes and commit changes Using `git add .` followed by `git commit -m 'your commit message'`
- Do step 3 as per your requirements
- Finally push your branch <branch_name> to remote repository before merging
`git push -u origin <branch_name>`


#### Git rebase to make history linear(Alternative of three way merge)
1. This method addresses changes in single branch only(example remote master branch and local mater branch)
- If same line or same section of the file is already changed and committed in both remote branch and
local branch,And then if you will try to push the local branch on the remote branch where file is already changed
<br>Then it will throw merge conflict and rebase come to action,it avoids three way merge and make history linear.
- first fetch your remote repository
`git fetch`
- To rebase local commit against remote use `git rebase origin/main`
- Then it pop up merge conflicts, to solve merge conflict: <br>
- Open file in text editor in which merge conflict arises
- Where you can find <<<<<<<, =======, and >>>>>>> conflict markers
- Remove all of the conflict markers and only leave the code as it should be after the merge and save it.
- Then stage that file using `git add .` or `git add <file_name>`
- Then continue rebase `git rebase --continue`
- Then see your log, where you can see that commit message are linear i.e local branch commit message rebase remote message(local commit history becomes last history and remote history becomes second last history)
- Then push your local rebased final version to remote using `git push`

To learn more about rebase changes  [click here](https://www.coursera.org/learn/introduction-git-github/lecture/cEqbt/rebasing-your-changes)



