# self-fork

Presents a form to fork itself to an authenticated Github user.

## Rationale

Simple as possible to cover the brief. Flask brings together minimal routing, templating, and static file serving with minimal ceremony. If this were to expand to a larger app, `app.py` could be decomposed into a [package][application as package] with external services extracted and test coverage. [Pico CSS][picocss] is used to normalize styles and add some baseline typography and form style. Docker provides a nearly universal way to reproduce a local deployment in a self-documenting way that can grow into differentiated paths for development and production.

[application as package]: https://flask.palletsprojects.com/en/2.2.x/patterns/packages/
[picocss]: https://picocss.com/

## Setup

This service relies on being authenticated to Github. To keep integration requirements simple, it uses a Personal Access token to authenticate REST API requests. Github provides [documentation for creating a token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). If using the new fine-grained permissions, be sure to set Administration to "Read and write" access, so that the new forked repository can be created.

### Docker 

Copy sample env file for customization

```sh
cp docker.env.sample docker.env
```

Update `docker.env` and override `FLASK_GITHUB_TOKEN` with a valid personal access token and `FLASK_GITHUB_USERNAME` with the corresponding user.

```sh
docker build -t self-fork:latest .
docker run -it --rm -p 8080:8080 --env-file docker.env self-fork:latest
```

Build/run the Docker container and visit [localhost:8080](http://localhost:8080).
