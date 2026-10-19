# Сценарий итоговой видеозащиты (примерно 16–19 минут)

> ТЗ требует **одно непрерывное видео 10–20 минут** с твоим экраном и голосом. Эта памятка не должна зачитываться монотонно: выполняй команды и объясняй результаты своими словами. Установку Ubuntu и создание всех файлов повторять не нужно. До записи проверь, что Jenkins успешно отработал, Docker Desktop включён и GitHub доступен.

## 0:00–0:35 — Представление

**Скажи:** «Здравствуйте! Я Нурдос Канатбек, группа IT2-2310, ID 37253. Показываю индивидуальную лабораторную по DevOps. Я использовал Ubuntu через WSL2, Git и GitHub для версионирования, Docker для контейнеризации и Jenkins для автоматизации сборки и тестирования».

**Покажи:** Ubuntu Terminal, команду `cd ~/devops/kanatbek_nurdos && pwd`.

## 0:35–4:10 — Part A, Linux

**Task 1 — структура и команды (1:00).**

```bash
pwd; ls -la; ls -R
mkdir -p backup/video_demo_dir
touch backup/video_demo_dir/test.txt
ls backup/video_demo_dir
rm backup/video_demo_dir/test.txt
rmdir backup/video_demo_dir
cat Kanatbek_Nurdos_info.txt
head Kanatbek_Nurdos_info.txt
tail Kanatbek_Nurdos_info.txt
cp Kanatbek_Nurdos_info.txt backup/video_copy.txt
mv backup/video_copy.txt backup/video_renamed.txt
rm backup/video_renamed.txt
```

**Скажи:** «Я создаю временную папку командой mkdir и файл командой touch, затем удаляю их. Папки app, scripts, config, logs, backup разделяют части проекта. pwd показывает текущую папку; ls — файлы; cat, head и tail — содержимое, начало и конец файла. cp копирует, mv перемещает или переименовывает, rm удаляет».

**Task 2 — логи (0:40).**

```bash
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
```

**Скажи:** «Логи нужны для диагностики приложения. find находит журнал, grep ищет сообщения, -c считает ошибки; здесь две ERROR. tail -n 5 показывает последние пять строк».

**Task 3 — права (0:30).**

```bash
ls -l private.txt public.txt
```

**Скажи:** «Файл private.txt имеет права 600: читать и писать может только владелец. public.txt — 644: другие могут читать, но не менять. В Linux r — read, w — write, x — execute. Права разделяются на owner, group, others».

**Task 4 — Bash (0:45).**

```bash
ls -l scripts/Kanatbek_Nurdos_system.sh
./scripts/Kanatbek_Nurdos_system.sh
```

**Скажи:** «Bash-скрипт проверяет существование файла студента, выводит сведения о системе: whoami, hostname, date, uname, df и free. chmod +x сделал файл исполняемым».

**Task 5 — процессы (0:40).**

```bash
ps
ps aux
ps -p $$ -o pid,user,%cpu,%mem,comm
top
```

Нажми `q` для выхода. **Скажи:** «Процесс — выполняемая программа. PID — идентификатор процесса. ps показывает состояние на один момент; top обновляет использование CPU и памяти в реальном времени».

## 4:10–7:45 — Part B, Git/GitHub

```bash
git status
git config --global user.name
git config --global user.email
git log --oneline --graph --all
git branch
git remote -v
cat .gitignore
git check-ignore -v logs/application.log backup/.gitkeep .env
```

**Скажи:** «Git отслеживает изменения исходников. git init создал локальный репозиторий, а пять и более реальных коммитов фиксируют создание структуры, студенческих данных, Bash-скрипта, приложения, Docker и Jenkins. .gitignore исключает logs, backup и .env. Ветка development нужна для изолированных изменений. После проверки я объединил её с main через merge. GitHub хранит удалённую копию репозитория, откуда Jenkins получает проект».

**Покажи:** страницу репозитория GitHub в браузере и видимые коммиты. Объясни `git push` — отправляет коммиты на GitHub, `git pull` — получает изменения.

## 7:45–11:55 — Part C, Docker

```bash
cat Dockerfile
docker build -t kanatbek-nurdos-devops .
docker images
docker run -d --name kanatbek-nurdos-container -p 8000:8000 \
 -e STUDENT_NAME=Nurdos -e STUDENT_SURNAME=Kanatbek \
 -e STUDENT_GROUP=IT2-2310 -e STUDENT_ID=37253 kanatbek-nurdos-devops
docker ps; docker ps -a
docker logs kanatbek-nurdos-container
curl http://localhost:8000/health
docker exec kanatbek-nurdos-container python -c 'import os; print(os.getenv("STUDENT_GROUP"))'
docker stop kanatbek-nurdos-container
docker start kanatbek-nurdos-container
docker rm -f kanatbek-nurdos-container
docker compose up -d --build
docker compose ps
docker compose down
```

**Скажи:** «Dockerfile описывает сборку образа. FROM выбирает базовую систему; WORKDIR рабочую директорию; COPY переносит файлы; RUN выполняет команду во время сборки; EXPOSE документирует порт; CMD запускает приложение. Образ — неизменяемый шаблон; контейнер — работающий экземпляр образа. Переменные STUDENT_* передаются через -e и позволяют настраивать приложение без изменения образа. docker logs показывает вывод приложения, stop/start управляют запуском, rm удаляет контейнер. Docker Compose позволяет запускать сервис по YAML-конфигурации одной командой».

## 11:55–16:55 — Part D, Jenkins

**Покажи в браузере:** `http://localhost:8080`, Dashboard и Job `Kanatbek_Nurdos_DevOps`, настройки Pipeline from SCM. Запусти `Build Now` (или покажи успешно завершённый запуск, если повторный займёт слишком много времени).

**Скажи:** «Jenkins — сервер CI. Он скачивает проект из GitHub, собирает программу, выполняет Python-тесты, создаёт Docker image и запускает Docker container. Эти шаги описаны в Jenkinsfile: Checkout, Build, Test, Docker Build, Docker Run. Переменные STUDENT_NAME, SURNAME, GROUP, ID выводятся в Console Output. Если любой этап завершается ошибкой, Pipeline не получает статус SUCCESS и следующие обычные стадии не выполняются. Сейчас видим Finished: SUCCESS».

**Покажи:** стадии, Console Output и git commit SHA, при необходимости `docker images` и `docker ps -a` в терминале. Не показывай пароль Jenkins.

## 16:55–18:15 — Part E, весь DevOps-процесс и финал

**Скажи:** «Рабочая цепочка выглядит так: Linux — исходный проект; Git — контроль версий; GitHub — удалённый репозиторий; Jenkins — автоматический запуск действий; Build и Test — проверка кода; Docker Build и Docker Run — упаковка и запуск приложения; результат SUCCESS. Такой подход делает сборку воспроизводимой и уменьшает количество ошибок при ручных действиях. Спасибо!».

## Мини-шпаргалка по вопросам преподавателя

| Вопрос | Ответ |
|---|---|
| `chmod 755`? | Владелец rwx, группа r-x, остальные r-x. |
| `git push` vs `git pull`? | Отправить локальные изменения / получить и интегрировать удалённые. |
| Image vs container? | Образ — шаблон, контейнер — его экземпляр. |
| `WORKDIR`? | Устанавливает рабочую директорию в Dockerfile. |
| `.gitignore`? | Не позволяет Git добавлять заданные файлы при обычном git add. |
| Что если Docker Build падает? | Jenkins показывает ошибку; последующая стадия Docker Run не выполняется. |
| Environment variable? | Значение, передаваемое процессу через окружение без изменения кода. |
| `find` и `grep`? | find ищет файлы; grep ищет строки в содержимом. |
| Зачем Jenkins GitHub? | Чтобы забирать версионированный код для повторяемого Pipeline. |
