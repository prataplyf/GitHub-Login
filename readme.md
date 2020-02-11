<h1>GitHub - Login</h1>
To get api key and secret key from github follow these steps:
1: go to github setting
2: select Developer Setting
3: select OAUTH Apps
4: create new OAUTH App
  Enter 
      : Application Name
      : Homepage URL (http://127.0.0.1:5000)
      : Application description
      : Authorization callback URL (http://127.0.0.1:5000/github_login/github/authorized)
      -- github_login : function created in the program

Then you'll get 
              Client ID : 9bb305f241b9a27bd26b
              Client Secret : 0e6901ae9db82af18a2bd62459b8d9d20c65a666
