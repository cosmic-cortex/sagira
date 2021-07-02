import pytest


from starlette.testclient import TestClient
from starlette import status


def test_matchmake(test_client: TestClient):
    data = [
      {"id": "Retsam", "elo": 1330},
      {"id": "Thandrise", "elo": 1237},
      {"id": "Nayan", "elo": 1237},
      {"id": "Chr1s", "elo": 1801},
      {"id": "pepta", "elo": 1979},
      {"id": "Drakkay", "elo": 1804},
      {"id": "Omicron", "elo": 1620},
      {"id": "Wasted", "elo": 2546},
      {"id": "Linnmon", "elo": 1552},
      {"id": "H4ver", "elo": 1572},
      {"id": "Lemur", "elo": 2546},
      {"id": "aron141", "elo": 2500},
      {"id": "Stiletto", "elo": 1578},
      {"id": "Kess", "elo": 1403},
      {"id": "ItsMathe", "elo": 2500},
      {"id": "Vidra", "elo": 1524},
      {"id": "su61", "elo": 1104},
      {"id": "KPHun", "elo": 1107},
      {"id": "Messor", "elo": 1658},
      {"id": "Deathless", "elo": 2485},
      {"id": "BalintGO", "elo": 1548}
    ]
    response = test_client.post("/", json=data)
    assert response.status_code == status.HTTP_200_OK
