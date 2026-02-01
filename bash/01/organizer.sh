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

[ ! -d "$file_destination_path" ] && mkdir "$file_destination_path" && echo "[info] Criando diretório de backup"

for file in "$file_origin_path"*
do
    if [[ ("$file" =~ $pattern1 || ("$file" =~ $pattern2)) && -f "$file" ]]; then
        file_name="${file#./}"
        file_name_raw="${file_name%.*}"
        extension=".${file##*.}"
        current_date="_$(date +%Y-%m-%d)"

        final_path="$file_destination_path$file_name_raw$current_date$extension"

        mv "$file" "$final_path"
        moved_files_number=$((moved_files_number + 1))

        [[ -f "$final_path" ]] && echo "[OK] movendo $file_name -> $final_path"
    fi
done

if [ $moved_files_number -eq 0 ]; then
    echo "nenhum arquivo encontrado!"
else
    echo "--------------------------------"
    echo "Limpeza concluída! $moved_files_number arquivo(s) movidos para o backup."
fi

exit 0