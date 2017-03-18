from flask import Flask
from github import Github
import sys
import base64


app = Flask(__name__)

@app.route("/v1/<filename>")
def hello(filename):
    
    inputurl = sys.argv[1]
    spliturl = inputurl.rsplit("/",1)
    splitusr = spliturl[0].rsplit("/",1)
    usrname = splitusr[1]
    reponame = spliturl[1]
    g=Github()
    try:
        r = g.get_user(usrname).get_repo(reponame)
        p = r.get_file_contents(filename).content
        return base64.b64decode(p)
    except:
        return 'ERROR : Enter a valid Repository :%s' % reponame
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    
