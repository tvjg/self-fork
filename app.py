import requests

from flask import Flask, Markup, render_template, redirect, request, flash

app = Flask(__name__)

app.config.from_prefixed_env()


# Singular route handler for our application.
#
# GET serves the page.
# POST makes a fork request, pushes result to flash, and redirects.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response = fork_repo()
        if response["status_code"] == 202:
            name = response["body"]["full_name"]
            url = response["body"]["html_url"]
            message = Markup(
                f'Fork request acknowledged. Find your fork at <a href="{url}">{name}</a>.'
            )
            flash(message, "success")
        elif response["status_code"] >= 400:
            error_message = response["body"]["message"]
            message = f"An error has occurred. Github says: {error_message}."
            flash(message, "danger")
        else:
            message = f"An unexpected error has occurred."
            flash(message, "danger")
        return redirect("/")
    else:
        return render_template("index.html", repo_name=app.config["GITHUB_FORK_REPO"])


# Make a fork request to Github API. In a larger application, consider a full
# featured client library and/or moving this to injectable service.
#
# https://docs.github.com/en/rest/repos/forks?apiVersion=2022-11-28#create-a-fork
def fork_repo():
    api_base_url = "https://api.github.com"
    username = app.config["GITHUB_USERNAME"]
    token = app.config["GITHUB_TOKEN"]
    owner = app.config["GITHUB_FORK_OWNER"]
    repo = app.config["GITHUB_FORK_REPO"]
    headers = {
        "accept": "application/vnd.github+json",
        "x-github-api-version": "2022-11-28",
    }
    r = requests.post(
        f"{api_base_url}/repos/{owner}/{repo}/forks",
        auth=(username, token),
        headers=headers,
    )

    return {"status_code": r.status_code, "body": r.json()}
