# Scrapping project (Flask variant)

Mikroserwis pobierający zdjęcia i tekst ze stron www.
Funkcjonalność
- Zlecenie pobrania tekstu z danej strony internetowej i zapis jej w systemie.
- Zlecenie pobrania wszystkich obrazków z danej strony i zapis ich w systemie.
- Sprawdzenie statusu zleconego zadania.
- Możliwość pobrania stworzonych zasobów (tekstu i obrazków)

## Getting Started

Aplikacja dostaje zapytania poprzez RESTowe API wystawione przez jeden z serwisów.
Serwis z API wysyła zadanie pobrania zasobów konkretnej strony internetowej do 
kolejki opartej o Redisa.
Zadania są kolejkowane i workery w miare możliwosci
 pobierają kolejne zadania (liczba wykonywanych zadań zależy odilości workerów (domyślnie 1)).
 
### Prerequisites

To run a service you need docker and docker-compose.
To run service locally and run tests you will need:
- python3 + pyenv/venv + requirements
- redis

## Deployment

Docker images are build using Dockerfile.
To build the image run:

`docker build . -t scrap_flask`

And run the stack with command:

`docker-compose up`

## Running the tests

Having requirements installed:

`cd app`

`python -m pytest tests`

## Built With

* Python
* Docker
* Redis
* Flask, RQ, BS4

## Authors

* **Stankiewicz Mateusz** - https://www.linkedin.com/in/mateusz-stankiewicz-3b04a2108/

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

