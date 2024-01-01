# Liturgical Colour App

A simple app to display the current liturgical colour of the Church of England.

It is based on the [Liturgical Colour](https://github.com/djjudas21/liturgical-colour)
library with a simple UI written with [Flask](https://pypi.org/project/Flask/)
and [Bootstrap](https://getbootstrap.com/).

## Develop

The app can be run locally for testing with

```sh
flask run
```

PRs are welcome, but should pass the Pylint tests.

[Issues](https://github.com/djjudas21/liturgical-colour-app/issues) should
be logged against this project for problems with the UI only.
Problems relating to the calculations of dates, colours and the calendar of
feasts should be logged against the
[Liturgical Colour](https://github.com/djjudas21/liturgical-colour/issues) library.

## Build

This project can be built as a Docker image with

```sh
docker build -t liturgical-colour:dev .
```

## Run

A [Helm chart](https://artifacthub.io/packages/helm/djjudas21/liturgical-colour)
is available for deploying on Kubernetes.
