pipeline {
  agent any
  stages {
    stage('Pull Data') {
      steps {
        sh '''wget -O backend/model_file https://infallible-boyd-e34277.netlify.app/model_file_complicated_no_stopwords
wget -O backend/tweets.csv https://infallible-boyd-e34277.netlify.app/tweets.csv'''
      }
    }

  }
}