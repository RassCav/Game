pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    triggers {
      pollSCM 'H/2 * * * *'
    }
    options {
        timeout(time: 10, unit: 'MINUTES') 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RassCav/Game.git']])
            }
        }
        stage('Build') {
            steps {
              sh 'pip install -r requirements.txt'
              sh 'python dices.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build('my-docker-image:latest', '-f Dockerfile .')
                }
            }
        }
        
    }
    post {
        always {
                slackSend channel: 'dices', message: "Hello HAMZA SIAD  your project status is ${currentBuild.currentResult}"
                }
        }
}
