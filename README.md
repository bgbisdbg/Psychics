# Экстрасенсы

## Тестирование экстрасенсов

Это веб-приложение на Django, которое моделирует тестирование экстрасенсов. Пользователь загадывает двухзначное число, а экстрасенсы пытаются угадать его. Приложение отслеживает достоверность каждого экстрасенса и отображает историю догадок и введенных пользователем чисел.

## Функциональность

- Пользователь загадывает двухзначное число.
- Пользователь подтверждает, что загадал число.
- Приложение запрашивает догадки от нескольких экстрасенсов.
- Пользователь вводит загаданное число.
- Приложение обновляет достоверность экстрасенсов.
- Пользователю предлагается заново загадать число.
- На странице отображается история догадок экстрасенсов, введенных чисел и текущая достоверность каждого экстрасенса.

## Технологии

- Django
- Python
- Docker

## Установка и запуск

### Локальный запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourusername/psychic-test.git
   cd Экстрасенс
   ```
   
2. Запускаем Docker и в комндной консоли


Сборка

```bash
docker build -t psychic_test_image .
 ```


 Для сборке образа

 и

Запуск

 ```bash
docker run -d -p 8000:8000 --name psychic_test_container psychic_test_image
  ```


