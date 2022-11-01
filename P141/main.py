from flask import Flask, jsonify, request
import csv
all_articles=[]
with open(r"C:\Users\gauri\OneDrive\Desktop\C and P 136\P141\MAIN.csv",encoding="utf-8") as f:
    data=list(csv.reader(f))
    all_articles=data[1:]
liked_articles=[]
not_liked_articles=[]
app=Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"SUCCESS"
    })
@app.route("/liked-article",methods=["POST"])
def liked_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"SUCCESS"
    }),200
@app.route("/not-liked-article",methods=["POST"])
def not_liked_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"SUCCESS"
    }),200
if __name__=="__main__":
    app.run()
