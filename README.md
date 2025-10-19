
## Kerge
Программа для записи bin файлов в микроконтроллер.

### Основные команды
**Версия программы**
```bash
uv run kerge.py -v
uv run kerge.py --version
```
**Записываем бинарный файл**
```bash
uv run kerge.py -w <file>
uv run kerge.py --write <file>
```
**Baudrate**
```bash
uv run kerge.py -b 
uv run kerge.py -b 15000000
uv run kerge.py --baud 
uv run kerge.py --baud 15000000
```
**Информация о порте**
```bash
uv run kerge.py -p <port>
uv run kerge.py --port <port>
```
**Список портов**
```bash
uv run kerge.py -l
uv run kerge.py --list
```
**Стереть память на микроконтроллере**
```bash
uv run kerge.py -f <port>
uv run kerge.py --flash <port>
```

### Roadmap

1. git репозиторий для готовых прошивок esp плат
2. добавить в pypi
3. адаптировать решение под несколько esp плат
4. написать веб-версию на `bottlepy`

### Первый запуск
1. Проверить, установлена ли последняя версия
2. вывести список доступных портов
3. настроить baudrate (default: `kerge -b 1500000`)
4. стереть память на микроконтроллере
5. записать прошивку в память
6. пользоваться платой
