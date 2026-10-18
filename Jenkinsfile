pipeline {
    agent any
    options { skipDefaultCheckout(true) }
    environment {
        STUDENT_NAME = 'Nurdos'
        STUDENT_SURNAME = 'Kanatbek'
        STUDENT_GROUP = 'IT2-2310'
        STUDENT_ID = '37253'
        DOCKER_IMAGE = 'kanatbek-nurdos-devops:ci'
        CI_CONTAINER = 'kanatbek-nurdos-ci'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
                echo "Group: ${env.STUDENT_GROUP}"
                echo "Student ID: ${env.STUDENT_ID}"
                sh 'git rev-parse --short HEAD'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/main.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t "$DOCKER_IMAGE" .'
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f "$CI_CONTAINER" >/dev/null 2>&1 || true
                    docker run -d --name "$CI_CONTAINER" \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$DOCKER_IMAGE"
                    sleep 2
                    docker exec "$CI_CONTAINER" python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=5).read().decode().strip())"
                    docker logs "$CI_CONTAINER"
                '''
            }
        }
    }
}
