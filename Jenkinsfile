pipeline {
  agent any

  stages {
    stage('Pull Data') {
      steps {
        powershell '''
Invoke-WebRequest 'https://infallible-boyd-e34277.netlify.app/model_file_complicated_no_stopwords' -OutFile './backend/model_file'
Invoke-WebRequest 'https://infallible-boyd-e34277.netlify.app/tweets.csv' -OutFile './backend/tweets.csv'
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
        powershell '''
pip install -r requirements.txt
python backend/test_integration.py
'''
      }
    }

  }
}