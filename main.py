from flask import Flask, request, render_template
from itertools import combinations


app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")

#Returns answers to the decisions posed in the assignment
@app.route('/info', methods =['GET'])
def app_info():
    from appInfo import return_info
    app_info = return_info()

    return app_info

#Accepts key/value pairs submitted as a POST request
#Will evaluate more than 2 sets of sample data submitted simultaniously 
@app.route('/textsimilarity', methods=['POST'])
def text_similarity():
    from textComps import comp_samples

    data = request.json
    ls = []
    for key in data:
        ls.append(key)
    samples = [i for i in combinations(ls,2)]
    
    sample_comps = {}
    for i in samples:
        comparison = comp_samples(data[i[0]],data[i[1]]) 
        sample_comps[i[0]+" vs "+i[1]] = comparison
    
    return sample_comps



if __name__ == '__main__':
    app.run(debug=True)