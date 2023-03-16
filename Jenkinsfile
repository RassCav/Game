pipeline {
    agent any
    environment {
      registry = 'rascav/dicesApp'
      registryCredential = 'dockerhub_id'
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
         stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
          }
        stage('Build Docker Image') {
            steps {
               sh 'docker build -t dices:0.1 .'
            }
        }
        
    }
    post {
        always {
                slackSend channel: 'dices', message: "Hello HAMZA SIAD  your project status is ${currentBuild.currentResult}"
                }
        }
}
