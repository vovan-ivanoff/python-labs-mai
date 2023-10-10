#/bin/bash

for NAME in a b c d e f g h i j k l m n o p q r s t
do
touch ./task_$NAME.py
echo "def task_$NAME():
    \"\"\"задание $NAME\"\"\"


if __name__ == '__main__':
    task_$NAME()" > ./task_$NAME.py
done
