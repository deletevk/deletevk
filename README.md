# deletevk
Скрипт чтобы удалить все записи со стены ВКонтакте

В текст скрипта нужно вставить ваш логин и пароль, для редактирования лучше использовать Блокнот, но не microsoft office. 
Свой логин нужно вписать на 5 строчке после 
login = 
в кавычках, без пробелов, например: 

login = "+79998887766"

Пароль от аккаунта ВКонтакте нужно вписать в 6-ю строку
passw =
также в кавычках, например: 

passw = "password"

Логин и пароль нужно вписать от того аккаунта, который вы хотите очистить. 

Для использования скриптов нужно установить на свой компьютер python, рекомендую использовать версию 3.5, т.к. на новых версиях могут быть проблемы с нужными библиотеками.
Установочный файл питона для Виндовс с официального сайта:
https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe

Чтобы установить библиотеку для API ВКонтакте откройте командную строку, для этого откройте меня Пуск и напишите в поиск cmd.exe, откройте программу. 
Откроется чёрное окно с белым текстом, напишите команду:  

pip3 install vk_api

или, если будет ошибка: 

C:\Python35\Tools\Scripts\pip3.exe install vk_api

Для запуска скрипта: 

C:\Python35\Tools\Scripts\pip3.exe путь_к_скрипту
