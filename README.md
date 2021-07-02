# sagira
A simple matchmaking API for Destiny 2 PvP scrims.

## Hosting the api
The Docker image can be launched with
```
docker-compose up
```

The API responds to `POST` requests made to `/`, with the request containing a list of players with their identifier
and Elo score. In the response, near-optimal teams of players are returned, balanced with respect to average Elo score
within teams.

Example request:
```text
curl -X 'POST' \
  'http://0.0.0.0:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
      {"id": "Retsam", "elo": 1330},
      {"id": "Thandrise", "elo": 1237},
      {"id": "Nayan", "elo": 1237},
      {"id": "Chr1s", "elo": 1801},
      {"id": "pepta", "elo": 1979},
      {"id": "Drakkay", "elo": 1804}
]'
```

Example response:
```json
[
  {
    "players": [
      {
        "id": "Chr1s",
        "elo": 1801
      },
      {
        "id": "Nayan",
        "elo": 1237
      },
      {
        "id": "Drakkay",
        "elo": 1804
      }
    ]
  },
  {
    "players": [
      {
        "id": "Retsam",
        "elo": 1330
      },
      {
        "id": "pepta",
        "elo": 1979
      },
      {
        "id": "Thandrise",
        "elo": 1237
      }
    ]
  }
]
```

After launch, the Swagger UI can be found at `http://0.0.0.0:8000/docs`. 
