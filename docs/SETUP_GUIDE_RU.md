# Пошаговая подготовка: Kanatbek Nurdos DevOps

## 0. Что важно

ТЗ требует 21 задание: Linux 1–5, Git/GitHub 6–10, Docker 11–15, Jenkins 16–20, интеграция 21. Итоговые материалы: GitHub-репозиторий, PDF со скриншотами, **одно непрерывное видео с голосом 10–20 минут**. В видео необязательно заново вводить каждую команду: надо показать и объяснить результаты.

Работаем в Ubuntu WSL2, каталог `/home/knt/devops/kanatbek_nurdos`. В архиве — готовые исходники; фактическое выполнение команд, скриншоты и успешный Jenkins Pipeline проверяются **на твоём компьютере**. Группа IT2-2310, ID 37253. Не публикуй реальные пароли и токены.

## 1. Распакуй архив в Ubuntu (в пустой проект)

1. Скачай ZIP через браузер в Windows Downloads.
2. Открой Ubuntu, выполни:

```bash
cd ~/devops/kanatbek_nurdos
sudo apt update
sudo apt install -y unzip python3 git
unzip -o /mnt/c/Users/knt/Downloads/kanatbek_nurdos_devops_starter.zip -d .
chmod +x scripts/Kanatbek_Nurdos_system.sh
chmod 600 private.txt
chmod 644 public.txt
pwd && ls -la && ls -R
```

Если ZIP сохранился не в Windows Downloads, уточни реальный путь и замени его в `unzip`. Не распаковывай ZIP внутрь вложенного `kanatbek_nurdos/` — после распаковки `Dockerfile` должен лежать в текущей папке проекта.

## 2. Linux (Task 1–5)

Проверки и команды, которые показываются в видео:

```bash
cd ~/devops/kanatbek_nurdos
pwd; ls; ls -la; ls -R
cat Kanatbek_Nurdos_info.txt
head Kanatbek_Nurdos_info.txt
tail Kanatbek_Nurdos_info.txt
cp Kanatbek_Nurdos_info.txt backup/info_copy.txt
mv backup/info_copy.txt backup/info_renamed.txt
ls backup
rm backup/info_renamed.txt
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
ls -l private.txt public.txt
./scripts/Kanatbek_Nurdos_system.sh
ps; ps aux
ps -p $$ -o pid,user,%cpu,%mem,comm
top
```

После `top` нажми `q`. Счётчик ошибок должен быть 2; `tail -n 5` должен показывать 5 строк. Если файл заканчивается пустой строкой, посмотри `nl -ba logs/application.log`.

## 3. Git (Task 6–10)

**Важно:** после распаковки все файлы существуют, но это не мешает делать осмысленные коммиты: каждый коммит фиксирует **отдельный логический набор реальных файлов**, а не пустые изменения. Порядок ниже не меняй.

```bash
cd ~/devops/kanatbek_nurdos
git init -b main
git config --global user.name "Nurdos Kanatbek"
git config --global user.email "YOUR_REAL_GITHUB_EMAIL"
git status
```

**Укажи свой реальный GitHub email или GitHub noreply вместо `YOUR_REAL_GITHUB_EMAIL`.**

Коммит 1 — структура + правила игнорирования:

```bash
git add README.md .gitignore app/.gitkeep scripts/.gitkeep config/.gitkeep logs/.gitkeep
git commit -m "chore: establish personalized project structure"
```

Коммит 2 — данные студента и публичный demo-файл:

```bash
git add Kanatbek_Nurdos_info.txt public.txt
git commit -m "docs: add personalized student information"
```

Коммит 3 — скрипт:

```bash
git add scripts/Kanatbek_Nurdos_system.sh
git commit -m "feat: add Linux system information script"
```

Коммит 4 — конфигурация, приложение, тесты:

```bash
git add config/app.conf app/main.py tests/test_main.py
git commit -m "feat: implement tested student HTTP application"
```

Коммит 5 — Docker:

```bash
git add Dockerfile docker-compose.yml .dockerignore
git commit -m "build: add Docker image and Compose setup"
```

Коммит 6 — Jenkins и документация:

```bash
git add Jenkinsfile infra/jenkins/Dockerfile docs/
git commit -m "ci: add Jenkins pipeline and lab documentation"
```

Проверь:

```bash
git status
git log --oneline
cat .gitignore
git check-ignore -v logs/application.log backup/.gitkeep .env
```

Ветка `development`: добавим **реальный новый документ** с задачами разработки, закоммитим и сольём:

```bash
git switch -c development
printf '# Development notes\n\nLocal Python tests pass before Docker packaging.\nJenkins automates checkout, build, tests, image build and container run.\n' > docs/DEVELOPMENT_NOTES.md
git add docs/DEVELOPMENT_NOTES.md
git commit -m "docs: document development workflow"
git switch main
git merge --no-ff development -m "merge: integrate development documentation"
git branch
git log --oneline --graph --all
```

GitHub: создаём **пустой публичный репозиторий** `kanatbek-nurdos-devops` в своём аккаунте (не создавать удалённый README). Если имя аккаунта всё ещё `to1enbekov`, то:

```bash
git remote add origin https://github.com/to1enbekov/kanatbek-nurdos-devops.git
git remote -v
git push -u origin main
git push -u origin development
```

GitHub может потребовать вход через credential manager или PAT — **пароль от GitHub в командную строку не вставляй**. Если username другой, замени его в URL.

## 4. Docker (Task 11–15)

Перед этим запусти **Docker Desktop**. В Settings → Resources → WSL Integration включи Ubuntu. Из Ubuntu убедись, что `docker version` показывает и Client, и Server:

```bash
docker version
docker compose version
python3 -m unittest discover -s tests -v
docker build -t kanatbek-nurdos-devops .
docker images
docker run -d --name kanatbek-nurdos-container -p 8000:8000 \
 -e STUDENT_NAME=Nurdos -e STUDENT_SURNAME=Kanatbek \
 -e STUDENT_GROUP=IT2-2310 -e STUDENT_ID=37253 kanatbek-nurdos-devops
docker ps
docker ps -a
docker logs kanatbek-nurdos-container
curl http://localhost:8000/
curl http://localhost:8000/health
docker exec kanatbek-nurdos-container python -c 'import os; print(os.getenv("STUDENT_GROUP"))'
docker stop kanatbek-nurdos-container
docker start kanatbek-nurdos-container
docker rm -f kanatbek-nurdos-container
```

Теперь Compose, поскольку порт 8000 свободен:

```bash
docker compose up -d --build
docker compose ps
docker compose logs --tail 20
curl http://localhost:8000/health
docker compose down
```

Docker image — шаблон, Docker container — запущенный экземпляр. `-e` передаёт переменные окружения во время запуска, поэтому настройки не надо встраивать в Docker image. Не встраивай секреты в Dockerfile.

## 5. Jenkins (Task 16–20)

Для простой локальной лабораторной запускаем Jenkins в отдельном Docker-контейнере; `infra/jenkins/Dockerfile` добавляет Python и Docker CLI для Pipeline.

**Внимание:** монтирование `/var/run/docker.sock` и запуск Jenkins от `root` предоставляют Jenkins административный доступ к Docker-хосту. Используй только для учебной локальной среды, не открывай порт Jenkins наружу в Интернет, не сохраняй в нём реальные секреты.

```bash
# Выполняется в Ubuntu из корня проекта.
docker build -t kanatbek-nurdos-jenkins:local -f infra/jenkins/Dockerfile .
docker volume create kanatbek-nurdos-jenkins-home
docker run -d --name kanatbek-nurdos-jenkins \
  --user root \
  -p 127.0.0.1:8080:8080 -p 127.0.0.1:50000:50000 \
  -v kanatbek-nurdos-jenkins-home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  kanatbek-nurdos-jenkins:local
```

Проверь:

```bash
docker logs --tail 40 kanatbek-nurdos-jenkins
docker exec kanatbek-nurdos-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Открой `http://localhost:8080`, введи начальный пароль, установи рекомендуемые плагины и создай администратора. Не публикуй пароль на видео. На локальном Jenkins: **New Item → Pipeline → название точно `Kanatbek_Nurdos_DevOps` → Pipeline → Definition `Pipeline script from SCM` → SCM `Git` → URL твоего публичного GitHub repo → Branch `*/main` → Script Path `Jenkinsfile` → Save → Build Now**.

Покажи Dashboard, стадии, Console Output, `Finished: SUCCESS`, commit SHA, `docker images`, `docker ps -a`, `docker logs kanatbek-nurdos-ci`. Jenkins использует GitHub как источник истины. Успех проверяется **только по настоящему выполненному Pipeline**, а не по наличию Jenkinsfile.

### Возможные проблемы

- `docker: command not found` в WSL — проверь Docker Desktop и WSL Integration.
- `permission denied /var/run/docker.sock` в Jenkins — проверь, что контейнер лабораторного Jenkins действительно запущен с `--user root` и сокет смонтирован.
- `port is already allocated` — перед Compose освободи порт 8000, перед Jenkins — 8080.
- `Git checkout` ошибается — проверь, что ветка main уже загружена на GitHub и URL верный.
- `git push` не прошёл — проверь вход в GitHub; пароль от учётной записи не используется вместо токена.

## 6. Итоговая сдача (Task 21)

Схема: Ubuntu/Linux → локальный проект → Git → GitHub → Jenkins Checkout → Build → Test → Docker Build → Docker Run → SUCCESS.

Для отчёта нужны **настоящие скриншоты**: структура папок, log/grep, права, Bash, `top`, Git log/branch/remote/GitHub, Dockerfile/image/container/env/logs/Compose, Jenkins Job/pipeline/console SUCCESS/commit. Файл `docs/REPORT_TEMPLATE_RU.md` задаёт разделы отчёта. Видео записывай одним непрерывным роликом **после** проверки всех инструментов, со своим экраном и голосом.
