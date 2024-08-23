import pytest
from project import *

def test_adieu_single_name():
    assert adieu(["taha"]) == "🤝 I recently collaborated with taha."

def test_adieu_two_name():
    assert adieu(["taha","sahel"]) == "🤝 I recently collaborated with taha and sahel."

def test_adieu_3_name():
    assert adieu(["taha","sahel","maziar"]) == "🤝 I recently collaborated with taha, sahel, and maziar."



def test_count_repos_by_language():
    repo_languages = {'Captcha-breaker': 'Python', 'Data-Structure-Coursera': 'C#', 'Emergency-pm': 'CSS', 'friendZone': 'Jupyter Notebook', 'images': 'Jupyter Notebook', 'MalwareDetector': 'Python', 'Petro-Lithology-Prediction': 'Jupyter Notebook', 'quera-solutions': 'Python', 'Stratego': 'Java', 'Sudoku_cpp': 'C++', 'Toos': 'Python', 'webShop': 'Python', 'Web_Security_tools': 'Python', 'words': 'Python', 'xv6-public': 'C'}
    language_count = list(count_repos_by_language(repo_languages))

    assert language_count[0] == 'Python'

def test_rgb_to_hex():
    assert rgb_to_hex((255, 0, 0)) == "ff0000"  # Red
    assert rgb_to_hex((0, 255, 0)) == "00ff00"  # Green
    assert rgb_to_hex((0, 0, 255)) == "0000ff"  # Blue
    assert rgb_to_hex((255, 255, 255)) == "ffffff"  # White
    assert rgb_to_hex((0, 0, 0)) == "000000"  # Black
    assert rgb_to_hex((128, 128, 128)) == "808080"  # Gray
    assert rgb_to_hex((255, 165, 0)) == "ffa500"  # Orange


def test_hex_to_rgb():
    assert hex_to_rgb("#ff0000") == (255, 0, 0)  # Red
    assert hex_to_rgb("#00ff00") == (0, 255, 0)  # Green
    assert hex_to_rgb("#0000ff") == (0, 0, 255)  # Blue
    assert hex_to_rgb("#ffffff") == (255, 255, 255)  # White
    assert hex_to_rgb("#000000") == (0, 0, 0)  # Black
    assert hex_to_rgb("#808080") == (128, 128, 128)  # Gray
    assert hex_to_rgb("#ffa500") == (255, 165, 0)  # Orange
    assert hex_to_rgb("#abc") == (170, 187, 204)  # Short hex


def test_get_complementary_color():
    assert get_complementary_color("#ff0000") == "00ffff"  # Complement of Red
    assert get_complementary_color("#00ff00") == "ff00ff"  # Complement of Green
    assert get_complementary_color("#0000ff") == "ffff00"  # Complement of Blue
    assert get_complementary_color("#ffffff") == "000000"  # Complement of White
    assert get_complementary_color("#000000") == "ffffff"  # Complement of Black
    assert get_complementary_color("#808080") == "7f7f7f"  # Complement of Gray
    assert get_complementary_color("#ffa500") == "005aff"  # Complement of Orange
import json

def test_wrap_text():
    assert wrap_text("This is a test", 50, 10) ==  ['This is a', 'test']

mock_data = """[
  {
    "id": "41289018355",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19905903336,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "c69c7907b8dc515d70d791b0db62882c6b2e94f1",
      "before": "6266f5d4d7b08944c2ffd7cda621677525dd8c47",
      "commits": [
        {
          "sha": "c69c7907b8dc515d70d791b0db62882c6b2e94f1",
          "author": {
            "email": "87542766+tahamusvi@users.noreply.github.com",
            "name": "Taha Mousavi"
          },
          "message": "Update README.md",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/c69c7907b8dc515d70d791b0db62882c6b2e94f1"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-23T15:19:41Z"
  },
  {
    "id": "41287863859",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 516455253,
      "name": "tahamusvi/tahamusvi",
      "url": "https://api.github.com/repos/tahamusvi/tahamusvi"
    },
    "payload": {
      "repository_id": 516455253,
      "push_id": 19905341511,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/'main'",
      "head": "3b777961e5aec496dccb31baa5dda8e98bd24386",
      "before": "9e6199afbb04d447e2d1a8667146b0c1889e6cca",
      "commits": [
        {
          "sha": "3b777961e5aec496dccb31baa5dda8e98bd24386",
          "author": {
            "email": "87542766+tahamusvi@users.noreply.github.com",
            "name": "Taha Mousavi"
          },
          "message": "Update README.md",
          "distinct": true,
          "url": "https://api.github.com/repos/tahamusvi/tahamusvi/commits/3b777961e5aec496dccb31baa5dda8e98bd24386"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-23T14:42:21Z"
  },
  {
    "id": "41286387773",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19904613977,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "b7d6516c6c82fbd3db189246c8e97f71b7b71f6d",
      "before": "25b2fab25b9e8fc13506acca476d369d29e01276",
      "commits": [
        {
          "sha": "b7d6516c6c82fbd3db189246c8e97f71b7b71f6d",
          "author": {
            "email": "TahaM8000@gmail.com",
            "name": "taa"
          },
          "message": "star repo",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/b7d6516c6c82fbd3db189246c8e97f71b7b71f6d"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-23T13:57:03Z"
  },
  {
    "id": "41285082647",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 516455253,
      "name": "tahamusvi/tahamusvi",
      "url": "https://api.github.com/repos/tahamusvi/tahamusvi"
    },
    "payload": {
      "repository_id": 516455253,
      "push_id": 19903990526,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/'main'",
      "head": "9e6199afbb04d447e2d1a8667146b0c1889e6cca",
      "before": "5e94db0c011c8e80a6959afbb95717bd87fa53ae",
      "commits": [
        {
          "sha": "9e6199afbb04d447e2d1a8667146b0c1889e6cca",
          "author": {
            "email": "87542766+tahamusvi@users.noreply.github.com",
            "name": "Taha Mousavi"
          },
          "message": "Update README.md",
          "distinct": true,
          "url": "https://api.github.com/repos/tahamusvi/tahamusvi/commits/9e6199afbb04d447e2d1a8667146b0c1889e6cca"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-23T13:16:30Z"
  },
  {
    "id": "41284783462",
    "type": "WatchEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 795852702,
      "name": "omidTarabavar/ICPC_Fundamental_Sharif",
      "url": "https://api.github.com/repos/omidTarabavar/ICPC_Fundamental_Sharif"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2024-08-23T13:07:09Z"
  },
  {
    "id": "41284392672",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19903637010,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "0804fe940039397972369339c3b20e7e97a0a381",
      "before": "1ed4b2a936889355740320871e5a62d475e87b69",
      "commits": [
        {
          "sha": "0804fe940039397972369339c3b20e7e97a0a381",
          "author": {
            "email": "TahaM8000@gmail.com",
            "name": "taa"
          },
          "message": "cleaning code",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/0804fe940039397972369339c3b20e7e97a0a381"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-23T12:55:15Z"
  },
  {
    "id": "41260111426",
    "type": "WatchEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 845941007,
      "name": "NazaninRzQ/LinearAlgebra_for_ML",
      "url": "https://api.github.com/repos/NazaninRzQ/LinearAlgebra_for_ML"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2024-08-22T18:32:50Z"
  },
  {
    "id": "41255334873",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19888939117,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "79fb29c06c1e4cb18a7c5a3784a67d2036a29c0e",
      "before": "1ada0e53df39e694c80e7e893efacc16f782ac60",
      "commits": [
        {
          "sha": "79fb29c06c1e4cb18a7c5a3784a67d2036a29c0e",
          "author": {
            "email": "TahaM8000@gmail.com",
            "name": "Taha"
          },
          "message": "LICENSE",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/79fb29c06c1e4cb18a7c5a3784a67d2036a29c0e"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-22T15:46:13Z"
  },
  {
    "id": "41255193265",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 516455253,
      "name": "tahamusvi/tahamusvi",
      "url": "https://api.github.com/repos/tahamusvi/tahamusvi"
    },
    "payload": {
      "repository_id": 516455253,
      "push_id": 19888873708,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/'main'",
      "head": "5e94db0c011c8e80a6959afbb95717bd87fa53ae",
      "before": "b4fa517f41e969b7724cf8b11635b166bea5d155",
      "commits": [
        {
          "sha": "5e94db0c011c8e80a6959afbb95717bd87fa53ae",
          "author": {
            "email": "87542766+tahamusvi@users.noreply.github.com",
            "name": "Taha Mousavi"
          },
          "message": "Update README.md",
          "distinct": true,
          "url": "https://api.github.com/repos/tahamusvi/tahamusvi/commits/5e94db0c011c8e80a6959afbb95717bd87fa53ae"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-22T15:41:57Z"
  },
  {
    "id": "41255129524",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19888843791,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "1ada0e53df39e694c80e7e893efacc16f782ac60",
      "before": "67089145ff8228448002c353e9304739dba99ff9",
      "commits": [
        {
          "sha": "1ada0e53df39e694c80e7e893efacc16f782ac60",
          "author": {
            "email": "TahaM8000@gmail.com",
            "name": "Taha"
          },
          "message": "update readme",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/1ada0e53df39e694c80e7e893efacc16f782ac60"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-22T15:40:04Z"
  },
  {
    "id": "41254713002",
    "type": "PushEvent",
    "actor": {
      "id": 87542766,
      "login": "tahamusvi",
      "display_login": "tahamusvi",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tahamusvi",
      "avatar_url": "https://avatars.githubusercontent.com/u/87542766?"
    },
    "repo": {
      "id": 842669809,
      "name": "Seyedsahel/ProfilePizza",
      "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza"
    },
    "payload": {
      "repository_id": 842669809,
      "push_id": 19888655391,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "67089145ff8228448002c353e9304739dba99ff9",
      "before": "0c3da077b65cee13df3c6dd1efa4112f96d0ad1b",
      "commits": [
        {
          "sha": "67089145ff8228448002c353e9304739dba99ff9",
          "author": {
            "email": "TahaM8000@gmail.com",
            "name": "Taha"
          },
          "message": "update for db",
          "distinct": true,
          "url": "https://api.github.com/repos/Seyedsahel/ProfilePizza/commits/67089145ff8228448002c353e9304739dba99ff9"
        }
      ]
    },
    "public": true,
    "created_at": "2024-08-22T15:28:13Z"
  }
]"""
response_events = json.loads(mock_data)


def test_get_user_satr():
    assert get_user_satr(response_events) == 'omidTarabavar/ICPC_Fundamental_Sharif'



if __name__ == "__main__":
    pytest.main()