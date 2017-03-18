from flask import Flask
from github import Github
import sys
import base64


app = Flask(__name__)

@app.route("/v1/<filename>")
def hello(filename):
    inputurl= sys.argv[1]
    g=Github("SachinWaghmode","GHE@ta91")
    r=g.get_user().get_repo('cmpe273-assignment1')
    
    p= r.get_file_contents(filename).content
    
    return base64.b64decode(p)


    
    #return base64.b64decode(g.get_user().get_repo().get_file_contents())
    #return "Hello from Dockerized Flask App!!"



#inputurl ="https://github.com/SachinWaghmode/cmpe273-assignment1"
#path1='README.md'
#path2='cmpe273-assignment1'





#for r in g.get_user().get_repos():
 #   print r.name
#get_file_content(path,ref="")
#print sys.argv

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    #app.run()
