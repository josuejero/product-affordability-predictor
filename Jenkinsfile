pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-django-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Deploy to Staging') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
        stage('Deploy to Production') {
            steps {
                input "Deploy to production?"
                sh 'kubectl apply -f deployment-production.yaml'
                sh 'kubectl apply -f service-production.yaml'
            }
        }
    }
}
