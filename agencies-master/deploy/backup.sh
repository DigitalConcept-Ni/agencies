#!/bin/bash

export FECHA=`date +%d_%m_%Y_%H_%M_%S`
export NAME=bisb_${FECHA}.dump
export DIR=/home/mateo/backup/
USER_DB=postgres
NAME_DB=bisb
cd $DIR
> ${NAME}
export PGPASSWORD=123
chmod 777 ${NAME}
echo "procesando la copia de la base de datos"
pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
echo "backup terminado"
