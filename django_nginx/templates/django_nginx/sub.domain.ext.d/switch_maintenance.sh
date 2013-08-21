#!/bin/bash
cd $(dirname $0)
maint_en="extra/en.maintenance.conf"
maint_dis="extra/di.maintenance.conf"
if [ "$1" = "maintenance" ]
then 
  if [ -f "$maint_dis" ]
  then 
    echo mise en maintenance
    mv "$maint_dis" "$maint_en"
  else
    echo "demande impossible : le fichier $maint_en n'existe pas"
  fi
fi

if [ "$1" = "production" ]
 
then 
  if [ -f "$maint_en" ]
  then 
    mv "$maint_en" "$maint_dis"
    echo mise en prod
  else
    echo "demande impossible : le fichier $maint_dis n'existe pas"
  fi
fi
