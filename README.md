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
