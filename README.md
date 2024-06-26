# Модуль 5. Практики CI/CD. Дополнительное задание

## Цель задания

Изучить набор компонентов для организации хранения кода и совместной работы над ним, а также для автоматического развертывания кода на сервере.
Это дополнительное задание, оценка за него плюсуется к накопленной. При желании вы можете пропустить это задание.

## Задание

Установить локальные клиентские приложения Docker и GitHub. Разместить заготовку кода в GitHub, предварительно создав репозиторий. Создать локальный Docker-образ проекта и отправить его в DockerHub. Настроить автоматическое развертывание кода с использованием GitHub → DockerHub → Server (SSH).

**Что нужно использовать в работе над заданием**

- [x] Клиент GitHub.
- [x] Клиент Docker.
- [x] Терминал ОС.
- [x] Тестовое Python-приложение.

## Выполнение задания

### Этап 1. Создание репозитория GitHub

- [x] **Шаг** 1.1 Скачать клиентское приложение GitHub для своей операционной системы и установить его.
- [x] **Шаг** 1.2 Зарегистрировать новый аккаунт в GitHub.
- [x] **Шаг** 1.3 Создать новый приватный репозиторий(при подготовке к сдаче задания, изменен на публичный репозиторий).
- [x] **Шаг** 1.4 Запустить установленное клиентское приложение GitHub, авторизоваться и скачать ранее созданный репозиторий на компьютер. Тем самым вы создадите локальную копию репозитория.
- [x] **Шаг** 1.5 Переместить код тестового Python-приложения в папку с GIT-репозиторием и отправить коммит в ветку dev, предварительно создав ее; а также запушить его в облако.
- [x] **Шаг** 1.6 Авторизоваться в веб-интерфейсе GitHub, создать Pull Request с учетом отправленного коммита из ветки dev в ветку main. Открыть созданный PR, подтвердить перенос файла. Убедиться, что ветка main содержит файл с кодом тестового Python-приложения.

![alt text](./assets/github-pr01-dev-to-main.png)

### Этап 2. Ручное создание образа Docker

- [x] **Шаг** 2.1 Скачать клиентское приложение Docker для своей операционной системы и установить его.
- [x] **Шаг** 2.2 Создать аккаунт в DockerHub.
- [x] **Шаг** 2.3 Создать новый публичный репозиторий. 
- [x] **Шаг** 2.4 Запустить установленное клиентское приложение Docker и авторизоваться.
- [x] **Шаг** 2.5 Создать отдельную папку на компьютере, в которую поместить файл с тестовым Python-приложением — это будет папка с приложением для создания образа.
- [x] **Шаг** 2.6 Скачать готовый Docker-файл или создать его самостоятельно в папке приложения с названием Dockerfile, без расширения.
- [x] **Шаг** 2.7 Поместить в созданный файл следующий фрагмент текста:

```yaml
# Установка Python из официального базового образа
FROM python:3.9-slim

# Добавляем метаданные
LABEL maintainer="dmkazanskii@yandex.ru"
LABEL version="v3.0"
LABEL description="Port:8180 app2:10 msg break"

# Установка рабочей директории внутри будущего контейнера
WORKDIR /app

# Копирование всех файлов приложения в контейнер
COPY app2.py /app

# Экспорт порта, на котором будет работать приложение
EXPOSE 8180

# Запуск тестового Python-приложения
CMD ["python", "app2.py"]

```

- [x] **Шаг** 2.8 Создать Docker-образ, перейдя в папку с приложением, содержащим созданный ранее Dockerfile, с помощью терминала MacOS или Windows, а затем запустив там команду:

```
docker build -t <docker_hub_username>/<image_name> <path_to_local_app_folder>
<docker_hub_username> — имя пользователя в DockerHub.
<image_name> — имя образа.
<path_to_local_app_folder> — локальный путь до папки с приложением.
```

> Например: `docker build -t dimitrius2kz/cicd_practice:v1 .`

- [x] **Шаг** 2.9 Запустить созданный контейнер с помощью команды в терминале: `docker run -it dimitrius2kz/cicd_practice:v1`
- [x] **Шаг** 2.10 Если образ запустился корректно, то программа будет отправлять в терминал каждые три секунды одну новую строку примерно такого вида: Приложение работает. Повторение №1
- [x] **Шаг** 2.11 Для того чтобы остановить работу контейнера, необходимо нажать на сочетание клавиш: ^+C (на MacOS, Ubuntu, Debian и Linux) или Ctrl+C (на Windows). Также можно просто закрыть терминал.

### Этап 3. Запуск Docker-образа на сервере вручную

На втором этапе должен был быть создан публичный Docker-репозиторий.

- [x] **Шаг** 3.1 Нужно отправить образ в DockerHub с помощью установленного настольного приложения или последовательно используя команды:

```    
docker login — далее, если ранее была авторизация в приложении Docker, то авторизация в DockerHub-аккаунте произойдет автоматически, иначе потребуется ввести логин и пароль от аккаунта.
docker push <docker_hub_username>/<image_name>:<tag>
<docker_hub_username> — имя пользователя в DockerHub.
<image_name> — имя образа (например, netology-lesson).
<tag> — тег образа (например, latest).
Например:
docker push dimitrius2kz/cicd_practice:v1
```
![alt text](./assets/docker-push.png)

- [x] **Шаг** 3.2 Убедиться, что Docker-образ успешно загружен в DockerHub. Для этого требуется авторизоваться под своим профилем в DockerHub и убедиться, что в списке появился целевой образ.

![alt text](./assets/docker-hub-review.png)

- [x] **Шаг** 3.3 Авторизоваться на сервере по SSH. Необходимо установить SSH-соединения с сервером, используя консоль на локальном компьютере. Процесс настройки SSH может отличаться от сервера к серверу, поэтому необходимо опираться на документацию каждого конкретного сервера индивидуально.

```
Примерно процедура настройки SSH выглядит так:
Создание SSH-ключей на локальном компьютере — например, с помощью команды в консоли:
ssh-keygen -t rsa -b 4096 -C “your_email@example.com”
После выполнения этой команды будет предложено ввести имя файла, в котором будет сохранен ваш ключ. По умолчанию это будет id_rsa для закрытого ключа и id_rsa.pub для открытого ключа.
Открытый ключ (id_rsa.pub) необходимо скопировать на сервер в файл ~/.ssh/authorized_keys, чтобы разрешить подключение к этому серверу.
```

- [x] **Шаг** 3.4 Установить Docker на сервер, последовательно выполнив следующие команды в терминале по инструкции: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [x] **Шаг** 3.5 Скачать Docker-образ на сервер, используя команду:

```
sudo docker pull <dockerhub_username>/<image_name>

<dockerhub_username> — ваш логин на DockerHub.
<image_name> — имя образа (например, netology-lesson).
Например:
sudo docker pull dimitrius2kz/cicd_practice:v3
Если команда сработала успешно, то начнется загрузка образа из DockerHub на сервер.
```

- [x] **Шаг** 3.6 После скачивания образа необходимо запустить его с помощью команды: `docker run -it dimitrius2kz/cicd_practice:v3`

![alt text](./assets/docker-run-it-server.png)

- [x] **Шаг** 3.7 Если образ запустился корректно, то программа будет отправлять в терминал каждые три секунды одну новую строку примерно такого вида: Приложение работает. Повторение №4
- [x] **Шаг** 3.8 Для того чтобы остановить работу контейнера, необходимо нажать на сочетание клавиш: ^+C (на MacOS, Ubuntu, Debian и Linux) или Ctrl+C (на Windows).

### Этап 4. Настройка CD GitHub → Docker → Server (SSH)

На третьем этапе должен быть настроен Docker-клиент на сервере, а также должен быть пройден этап ручного скачивания образа из DockerHub и запуск контейнера на сервере.
- [x] **Шаг** 4.1 Для настройки CD необходимо авторизоваться в GitHub под аккаунтом, который является владельцем ранее созданного репозитория. Создать коммит на перемещение ранее созданного Docker-файла в ветку main.
- [x] **Шаг** 4.2 Перейти к ранее созданному репозиторию, выбрав его в списке:
- [x] **Шаг** 4.3 Перейти к разделу Actions:
- [x] **Шаг** 4.5 В поиске ввести Docker image и нажать на кнопку Configure:
- [x] **Шаг** 4.6 В появившемся окне добавить фрагмент YAML-кода из файла:

```yaml
name: deploy

on:
  push:
    branches: [ main ]

  workflow_dispatch:

jobs:
  build_and_push_to_docker_hub:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    steps:
    - name: Check out the repo
      uses: actions/checkout@v2
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1
    - name: Login to Docker
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
    - name: Push to Docker Hub
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: dimitrius2kz/cicd_practice:latest

  deploy:
    name: Deploy the app
    runs-on: ubuntu-latest
    needs: build_and_push_to_docker_hub
    steps:
    - name: Execute remote ssh commands to deploy
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USER }}
        key: ${{ secrets.SSH_KEY }}
        script: |
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker stop main_container
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker system prune -a -f
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker pull dimitrius2kz/cicd_practice:latest
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S nohup docker run --name main_container -d dimitrius2kz/cicd_practice:latest

```

- [x] **Шаг** 4.7 Сохранить файл, нажав на кнопку Start commit, а затем нажав на кнопку Commit changes:
- [x] **Шаг** 4.8 В результате предыдущих шагов каждый раз, когда какой-либо код будет вливаться в ветку main, будет запускаться автоматическая задача на публикацию измененного образа в DockerHub, а затем его скачивание и запуск на сервер. На данный момент сценарий не отработает корректно, т. к. не были указаны все объявленные в файле переменные, а именно:

```bash
# переменные окружения
DOCKER_USERNAME # логин пользователя в DockerHub;
DOCKER_PASSWORD # пароль пользователя в DockerHub;
HOST # IP-адрес сервера, на котором требуется разворачивать образ;
USER # имя пользователя, под которым будет открываться SSH-соединение;
SUDO_PASSWORD # пароль пользователя для выполнения команд sudo;
SSH_KEY # приватный ключ для создания безопасного соединения между GitHub и сервером;
```

- [x] **Шаг** 4.9 Из перечисленных в предыдущем шаге параметров известно все, за исключением SSH_KEY — его нужно сгенерировать на сервере аналогично тому, как это делалось на локальном компьютере для настройки SSH-соединения с сервером. После подключения по SSH к серверу необходимо выполнить команду: `ssh-keygen -t rsa -b 4096 -C “your_email@example.com”`
После выполнения этой команды будет предложено ввести имя файла, в котором будет сохранен ваш ключ. По умолчанию это будет id_rsa для закрытого ключа и id_rsa.pub для открытого ключа.
Содержимое файла id_rsa (приватного ключа) необходимо вывести в консоль с помощью команды: `sudo cat id_rsa`
В результате выполнения команды выше в консоль будет выведен приватный ключ, который нужно скопировать, — это и будет значением нашей переменной `SSH_KEY`.
- [x] **Шаг** 4.10 Нужно последовательно добавить переменные и их значения в GitHub, перейдя в панель с настройками репозитория: Репозиторий → Settings → Secrets and veriables → Actions, нажимая на кнопку New repository secret каждый раз при добавлении новой переменной и ее значения.
После перехода к созданию новой переменной будет открыто специальное окно, где необходимо указать название переменной точь-в-точь то, что используется в ранее созданном файле с описанием сценария выкатки `(DOCKER_USERNAME, DOCKER_PASSWORD, HOST, USER, SUDO_PASSWORD, SSH_KEY)`, а также значение; и нажать на кнопку Add secret.
- [x] **Шаг** 4.11.1 Сделать новый коммит и подтвердить пул-реквест в репозиторий GitHub, чтобы проверить работоспособность сценария и всех указанных переменных. В случае успеха в разделе Actions в GitHub должен быть виден соответствующий статус у задания на перенос кода на сервер:

![alt text](./assets/actions-success.png)


- [x] **Шаг** 4.11.2 Авторизоваться по SSH на сервере и сделать вывод контейнера видным с помощью команд:

```bash
docker logs main_container > output.log
cat output.log
```

![alt text](./assets/cat-output-log.png)



На этом процедура настройки CD с помощью GitHub → Docker → Server (SSH) завершена.


## Формат сдачи задания

- [x] Выслать публичные ссылки на репозиторий в GitHub и DockerHub: [ссылка на GitHub](https://github.com/dimitrius2kz/cicd_practice), [ссылка на DockerHub](https://hub.docker.com/r/dimitrius2kz/cicd_practice/tags);
- [x] Выслать скриншот консоли с работающим на сервере приложением:

![](./assets/docker-run-it-server.png)

- [x] Прикрепить рецепт публикации приложения, созданный в разделе Action в GitHub:

```yml
name: deploy

on:
  push:
    branches: [ main ]

  workflow_dispatch:

jobs:
  build_and_push_to_docker_hub:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    steps:
    - name: Check out the repo
      uses: actions/checkout@v2
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1
    - name: Login to Docker
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
    - name: Push to Docker Hub
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: dimitrius2kz/cicd_practice:latest

  deploy:
    name: Deploy the app
    runs-on: ubuntu-latest
    needs: build_and_push_to_docker_hub
    steps:
    - name: Execute remote ssh commands to deploy
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USER }}
        key: ${{ secrets.SSH_KEY }}
        script: |
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker stop main_container
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker system prune -a -f
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S docker pull dimitrius2kz/cicd_practice:latest
          echo "${{ secrets.SUDO_PASSWORD }}" | sudo -S nohup docker run --name main_container -d dimitrius2kz/cicd_practice:latest

```




