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
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
            }

        stage('run') {
            steps {
                sh 'bash run.sh'
            }
        }
    }
}