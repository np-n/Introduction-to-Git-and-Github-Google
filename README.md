#### To find difference between two files
diff <first_file_name.extension> <second_file_name.extension>

Alternatively

diff -u <first_file_name.extension> <second_file_name.extension>
(<.....> indicates file name)

#### To find differnce/compare words in files
wdiff <first_file_name.extension> <second_file_name.extension>

#### To save line differences between two files into file
diff -u <first_file> <second_file> > <diff_file_name.diff>


#### To apply changes from diff file to old file(where errors occurs/needs to chage)
patch <file_name.extension> < <diff_file_name.extension>
(All changes are applied to <file_name.extension>)


#### To copy content of file/ to create duplicate file with similar content
cp <original_file_name.extension> <duplicate_file_name.extension>

#### To find all directory with more info(with all hidden files and folders)
ls -la

#### To get files with .extension
ls -l .extension/ (example: ls -l .git/)


#### To copy <file> to subdirectory from directory
cp ../<file> .  (To do that you must be in subdirectory)


#### To commit your changes
git commit  (It open default text editor where you can write commit message)


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
git config --l


#### To see what changes are done in a file(example a.extension)
git diff a.extension(just after modification before adding modified files for tracking)


#### If you are using git first time tell git who you are
git config --global user.name ="<your_username>"
git config --global user.email ="<your_email>"


#### To initialize git/git working directory
git init

#### To stage/Track file
git add <file_name.extension>

#### To track all files
git add .


#### To untrack/unstage file, which is already staged but not commited
git restore --staged <file_name.extension>
git reset HEAD <file_name.extension>
#### To restore/unstage all file and folders
git restore --staged .
#### To create snapshot/repository of your changes
git commit (prompts default text editor,you can write multiline comments)
git commit -m "< write your commit message here>"


#### To track changes in tracked files and commit in single steps
git commit -a   (Doesn't work for new files which are not tracked yet,opens in default text editor)
git commit -a -m "<write your commit message>"

#### To see past changes history/commit
git log

### To see n latest commit/log
git log -n
#### To see all changes in commit/associated patches
git log -p
#### To see all patches in n commits
git log -p -n
#### To see specific changes in a commit
git show <commit_id>(<commit_id> is identifier associated with each commit)

#### To see status of changes/commit
git log --stat

#### To see commit as graph
git log --graph

#### To see all commit,single line for a single  commit
git log --graph --oneline
#### To see changes before starting file tracking/staging file
git diff (for all changes)
git diff <file_name> (for specific changes in <file_name> file)


#### To see changes that are staged/tracked but not commited
git diff --staged


#### To delete file from repository
git rm <filename.extension> (file <filename.extension> will be deleted from your repository)

#### To rename files in the repository 
git mv <a.extension> <b.extension> (<a.extension> file name is renamed as <b.extension>)
(Note: mv command is also used to move files/folder in linux)


#### To escape or avoid file in ropository
write file name  inside .gitignore file
Example
To ignore readme.txt file
echo readme.txt > .gitignore


#### To discard changes in the working directory/file, if file is not tracked yet
git checkout <file_name.extension> (old approach)
git restore <file_name.extension> (new approach)
(Restore file to last staged/tradked state)


#### TO change commit message
git commit --amend

### How to fix staged/unstage changes, how to fix the commit that was incomplete
git add <file_name.extension>(add or unstage file )
or
git add .

git commit --amend(can change commit in editor)


#### To revert/go back to last snapshot/repository, because current changes in repo produce error
git revert HEAD (creates new commit with inverse changes, add reason for rollback in commit) 

#### To rollback to specific snapshot
git revert <commit_id_for_snapshot>


### Branch
#### To see available branch
git branch (current branch is indicated by *)

#### To create new branch
git branch <new_branch_name>


#### To enter into branch
git checkout <new_branch_name>
(Note: Before you checkout branch you need to save/commit your changes)
#### To create and enter new  branch into single command
git checkout -b <new_branch_name>


#### To delete git branch
git branch -d <branch_name> (Note: to delete branch you must be in master branch)
#### To delete git branch forcefully  without merging/saving changes in branch
git branch -D <branch_name>


#### To merge branch
git merge <merging_branch_name> (note: to merge you must be in your destination branch)
#### Two type of git merging algorithms:
- fast forward merge
- three way merge 
