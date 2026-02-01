#!/usr/bin/env bash
#-------------------------------------------------------------------------
# Script_name: Organizador de Workspace.
# Description: Um script que organiza arquivos .log e .tmp no diretório.
# Author: Henrique Verissimo
# Version: 0.1.0
# Date: 01/02/2026
# License: GPL (No Warranty)
# Contact:
#   - henriqueverissimocontato@gmail.com
#   - https://github.com/HenryVerissimo
#   - https://www.linkedin.com/in/henrique-verissimo
#-------------------------------------------------------------------------
# Usage: ./organizer.sh ou bash organizer.sh
#-------------------------------------------------------------------------
# Variables:
file_origin_path="./"
file_destination_path=./backup/
pattern1="\.log$"
pattern2="\.tmp$"
moved_files_number=0
#-------------------------------------------------------------------------
# Script:

[ ! -d $file_destination_path ] && mkdir "$file_destination_path"

for file in "$file_origin_path"*
do
    if [[ ($file =~ $pattern1 || ($file =~ $pattern2)) ]]; then
        file_name="${file#./}"
        file_name="${file_name%.*}"
        extension=".${file##*.}"
        date="_$(date +%Y-%m-%d)"

        mv $file "$file_destination_path$file_name$date$extension"
        moved_files_number+=1
    fi

done