# Напишите скрипт который дает студенту 3 секунды чтобы ответить на вопрос "ФИО преподавателя"
# Если он не успевает выводится "Вы отчислены"

#!/bin/bash

echo "Кто является вашим преподавателем по данному предмету?"
read -t 3 answer

if [ -z "$answer" ]; then
    echo "Вы отчислены"
else
    echo "Ответ принят"
fi