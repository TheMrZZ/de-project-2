pipeline {
  agent any

  stages {
    stage('Pull Data') {
      steps {
        bat '''
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://infallible-boyd-e34277.netlify.app/model_file_complicated_no_stopwords', 'backend/model_file')""
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://infallible-boyd-e34277.netlify.app/tweets.csv', 'backend/tweets.csv')""
'''
      }
    }

    stage('Archive data') {
      steps {
        archiveArtifacts 'backend/model_file'
        archiveArtifacts 'backend/tweets.csv'
      }
    }

    stage('Run integration & unit tests') {
      when {
        branch 'feature/*'
      }
      steps {
        bat 'python backend/test_integration.py'
      }
    }

  }
}