pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'bash build.sh'
            }
        }
        stage('test') {
            steps {
                sh 'bash test.sh'
            }
        }
        stage('run') {
            steps {
                sh 'bash run.sh'
            }
        }
    }
}