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

    stage('Push on release') {
      when {
        branch 'develop'
      }

      steps {
        powershell 'git config --global user.email "florianernst59@gmail.com"'
        powershell 'git config --global user.name "Florian ERNST"'
        powershell 'git fetch --all'
        powershell 'git checkout -B develop'
        powershell 'git pull origin develop'
        powershell 'git checkout -B release'
        powershell 'git pull origin release'
        powershell 'git merge develop'

        withCredentials([usernamePassword(credentialsId: 'My-Jenkins-App-DE-2', passwordVariable: 'pass', usernameVariable: 'user')]) {
          withEnv(["USER=$user", "PASS=$pass"]) {
            powershell 'git remote remove origin'
            powershell 'git remote add origin "https://TheMrZZ:$env:PASS@github.com/TheMrZZ/de-project-2.git"'
          }
        }

        powershell 'git push --set-upstream origin release'
      }
    }

    stage('Push on main') {
      when {
        branch 'release'
      }

      steps {
        input 'Put in production?'

        powershell 'git config --global user.email "florianernst59@gmail.com"'
        powershell 'git config --global user.name "Florian ERNST"'
        powershell 'git fetch --all'
        powershell 'git checkout -B release'
        powershell 'git pull origin release'
        powershell 'git checkout -B main'
        powershell 'git pull origin main'
        powershell 'git merge release'

        withCredentials([usernamePassword(credentialsId: 'My-Jenkins-App-DE-2', passwordVariable: 'pass', usernameVariable: 'user')]) {
          withEnv(["USER=$user", "PASS=$pass"]) {
            powershell 'git remote remove origin'
            powershell 'git remote add origin "https://TheMrZZ:$env:PASS@github.com/TheMrZZ/de-project-2.git"'
          }
        }

        powershell 'git push --set-upstream origin main'

        withCredentials([usernamePassword(credentialsId: 'docker', passwordVariable: 'pass', usernameVariable: 'user')]) {
          withEnv(["USER=$user", "PASS=$pass"]) {
            powershell 'docker login --username $env:USER --password $env:PASS'
          }
        }

        powershell 'docker build -t "themrzz/de-project-2:latest" .'
        powershell 'docker push themrzz/de-project-2:latest'

        echo "The application is now in production."
      }
    }
  }
}