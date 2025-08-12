import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []  

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    assert tasks, "Nenhuma tarefa criada"
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["id"] == task_id

def test_update_task():
    assert tasks, "Nenhuma tarefa criada"
    task_id = tasks[0]
    payload = {
        "completed": True,
        "description": "Nova Descrição",
        "title": "Título atualizado"
    }
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json