from fastapi.testclient import TestClient
from api import api

client = TestClient(api)

def test_create_experiment():
    response = client.post(
        "/experiments/",
        json={
            "model_name": "RandomForest",
            "dataset": "Iris",
            "accuracy": 0.95,
            "status": "completed"
        }
    )

    assert response.status_code == 200
    assert response.json()["model_name"] == "RandomForest"
    assert "id" in response.json()

def test_invalid_accuracy():
    response = client.post(
        "/experiments/",
        json={
            "model_name": "RandomForest",
            "dataset": "Iris",
            "accuracy": 1.5
        }
    )
    assert response.status_code == 422    

def test_get_experiment():
    response = client.post(
        "/experiments/",
        json={
            "model_name": "SVM",
            "dataset": "Iris"
        }
    )

    experiment_id = response.json()["id"]

    get_response = client.get(f"/experiments/{experiment_id}")

    assert get_response.status_code == 200
    assert get_response.json()["model_name"] == "SVM"


def test_update_experiment():
    response = client.post(
        "/experiments/",
        json={
            "model_name": "RandomForest",
            "dataset": "Iris",
            "accuracy": 0.85
        }
    )

    experiment_id = response.json()["id"]

    update_response = client.patch(
        f"/experiments/{experiment_id}",
        json={"accuracy": 0.95}
    )

    assert update_response.status_code == 200
    assert update_response.json()["accuracy"] == 0.95
    assert update_response.json()["model_name"] == "RandomForest"

def test_delete_experiment():
    response = client.post(
        "/experiments/",
        json={
            "model_name": "XGBoost",
            "dataset": "Iris"
        }
    )

    experiment_id = response.json()["id"]

    delete_response = client.delete(
        f"/experiments/{experiment_id}"
    )

    assert delete_response.status_code == 200

    get_response = client.get(
        f"/experiments/{experiment_id}"
    )

    assert get_response.status_code == 404