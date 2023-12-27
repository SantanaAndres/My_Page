from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
bootstrap = Bootstrap5(app)

page  = requests.get("https://github.com/shewart16")

soup = BeautifulSoup(page.content, "html.parser")


@app.route("/")
def home():
    projects_links = [project.text.lstrip() for project in soup.find_all(class_="repo")]
    projects_links.pop(0)
    projects_images = ["https://media.wired.com/photos/641e1a1b43ffd37beea02cdf/master/w_2560%2Cc_limit/Best%2520Password%2520Managers%2520Gear%2520GettyImages-1408198405.png",
                       "https://www.astera.com/wp-content/uploads/2020/01/rest.png"]
    return render_template("index.html", projects=projects_links, images=projects_images)

if __name__ == "__main__":
    app.run(debug=True)

