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

#### To find all directory with more info
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
git add <file_name>

#### To track all files
git add .

#### To create snapshot/repository of your changes
git commit (prompts default text editor,you can write multiline comments)
git commit -m "< write your commit message here>"


#### To track changes in tracked files and commit in single steps
git commit -a   (Doesn't work for new files which are not tracked yet,opens in default text editor)
git commit -a -m "<write your commit message>"

#### To see past changes history/commit
git log

#### To see all changes in commit/associated patches
git log -p

#### To see specific changes in a commit
git show <commit_id>(<commit_id> is identifier associated with each commit)

#### To see status of changes/commit
git log --stat


#### To see changes before starting file tracking/staging file
git diff (for all changes)
git diff <file_name> (for specific changes in <file_name> file)


#### To see changes that are staged/tracked but not commited
git diff --staged
