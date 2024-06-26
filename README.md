
# Генератор билетов для экзамена по алгебре

Welcome to генератор билетов для колока по алгебре. Билеты включают стейтменты, дефинишены и пруфы, которые прислал Трушин.

## Требования

- Python 3.6 или выше
- ReportLab
- PyPDF2

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/maykorablina/algebra_ticket_generator
   cd algebra_exam_ticket_generator
   ```

2. Создайте виртуальное окружение:
   ```sh
   python -m venv .venv
   ```

3. Активируйте виртуальное окружение:
   - На Windows:
     ```sh
     .venv/Scripts/activate
     ```
   - На macOS и Linux:
     ```sh
     source .venv/bin/activate
     ```

4. Установите необходимые пакеты:
   ```sh
   pip install -r requirements.txt
   ```

## Использование

1. Запустите скрипт для генерации экзаменационного билета:
   ```sh
   python main.py
   ```

2. Сгенерированный PDF файл с экзаменационным билетом будет сохранен как `exam_ticket.pdf` в директории проекта.

## Структура файлов

- `main.py`: Основной скрипт для генерации экзаменационных билетов.
- `definitions_list.pdf`: PDF файл с дефинишенами и стейтментами.
- `question_list.pdf`: PDF файл с пруфами.
- `requirements.txt`: Список необходимых библиотек.
- `README.md`: Документация проекта.

## Example Output

An example exam ticket format:

```
Exam Ticket

• Give four definitions, 0.5 each:
    An invertible element of a ring
    Classification of cyclic groups
    A field
    The image of a homomorphism of groups

• Formulate two statements without proof, 1.5 each:
    Ideals of the ring Zn
    Prove that a reduction process in a polynomial ring in several variables terminates

• Prove a simple statement, 2 points:
    Subgroups of the group Zn

• Prove an interesting statement, 3 points:
    Equivalent definitions of a normal subgroup
```