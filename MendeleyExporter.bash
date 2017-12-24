 #!/bin/bash

HERE=$(pwd)

echo $# arguments

if (( $# > 3 )); then
    echo "Illegal number of arguments"
fi

for i in "$@" ; do
    if [[ $i == "-e" ]] ; then
        echo "export option set"
        break
    fi
done

j=1
for i in "$@" ; do
    if [[ $i == "-t" ]] ; then
        echo "tag filtering option is set"
        tpos=$j
        next=$(( $tpos+1 ))
        echo "$tpos"
        echo "$next"
    fi


    if [[ $j == $next ]]; then
      TAG=$i
    fi

    j=$[$j +1]

done

echo "tag is: $TAG"

 # 1 - Check mac or linux
 unameOut="$(uname -s)"
 case "${unameOut}" in
     Linux*)     machine=Linux;;
     Darwin*)    machine=Mac;;
     CYGWIN*)    machine=Cygwin;;
     MINGW*)     machine=MinGw;;
     *)          machine="UNKNOWN:${unameOut}"
 esac
 echo "Machine is ${machine}"

 # 2 - copy bibtex file from Mendeley
 if [ ${machine} = "Linux" ]; then
     echo "Copying bibtex file from mendeley on Linux"

 elif [ ${machine} = "Mac" ]; then
     cd /Users/$USER/Library/Application\ Support/Mendeley\ Desktop
     MendeleyDB=$(ls *www.mendeley.com.sqlite)
     echo "found database $MendeleyDB in /Users/$USER/Library/Application\ Support/Mendeley\ Desktop"
     cd $HERE

 else
     echo "machine not recognized"

 fi

# 2 - Make a copy of the mendeley database to work with
cp /Users/$USER/Library/Application\ Support/Mendeley\ Desktop/$MendeleyDB $HERE/db.sqlite

# 3 - Export all tagged pdf with titles from library
#python3 Pymendsync.py 'MyPubs'
