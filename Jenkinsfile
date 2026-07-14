pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-demo .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-demo || true'
                sh 'docker rm flask-demo || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name flask-demo -p 5000:5000 flask-demo'
            }
        }
    }
}