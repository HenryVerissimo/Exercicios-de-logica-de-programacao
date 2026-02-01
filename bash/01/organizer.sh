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