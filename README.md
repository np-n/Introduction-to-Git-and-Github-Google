## To find difference between two files
diff <first_file_name.extension> <second_file_name.extension>

Alternatively

diff -u <first_file_name.extension> <second_file_name.extension>
(<.....> indicates file name)

## To find differnce/compare words in files
wdiff <first_file_name.extension> <second_file_name.extension>

## To save line differences between two files into file
diff -u <first_file> <second_file> > <diff_file_name.diff>



## To apply changes from diff file to old file(where errors occurs/needs to chage)
patch <file_name.extension> < <diff_file_name.extension>
(All changes are applied to <file_name.extension>)


## To copy content of file/ to create duplicate file with similar content
cp <original_file_name.extension> <duplicate_file_name.extension>
