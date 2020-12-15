pipeline {
  agent any

  stages {
    stage('Pull Data') {
      steps {
        powershell '''
cp C:/Users/Florian/Documents/de-project-2/backend/model_file_complicated_no_stopwords ./backend/model_file
cp C:/Users/Florian/Documents/de-project-2/backend/tweets.csv ./backend/tweets.csv
'''
      }
    }

    stage('Install requirements') {
      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe -m pip install -r requirements.txt'
      }
    }

    stage('Run integration & unit tests') {
      when {
        branch 'feature*'
      }
      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_integration.py'
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_unit.py'
      }
    }

    stage('Run stress test') {
      when {
        branch 'develop'
      }

      steps {
        powershell 'C:/Users/Florian/AppData/Local/Programs/Python/Python38/python.exe backend/test_stress.py'
      }
    }

    stage('Push on main') {
      when {
        branch 'develop'
      }

      steps {
        powershell 'git fetch --all'
        powershell 'git checkout develop'
        powershell 'git pull'
        powershell 'git checkout release'
        powershell 'git pull'
        powershell 'git merge origin/develop'

        git branch: 'release', credentialsId: 'My-Jenkins-App-DE-2', url: 'https://github.com/TheMrZZ/de-project-2.git'
        powershell 'git push --set-upstream origin release'
      }
    }
  }
}