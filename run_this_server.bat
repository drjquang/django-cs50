@echo off
start cmd.exe /k manage.py runserver 0.0.0.0:9876
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://192.168.1.106:9876/products"
