from locust import HttpUser, task, between


class MemeAPIUser(HttpUser):
    wait_time = between(1, 1.5)

    def on_start(self):
        response = self.client.post("/authorize", json={"name": "TestUser33"})
        self.token = response.json()['token']
        self.client.headers.update({"Authorization": f"{self.token}"})

    @task(1)
    def create_meme(self):
        payload = {
            "text": "testing meme",
            "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
            "tags": ["IT", "meme", "software tester"],
            "info": {
                "colours": ["white", "brown", "grey"],
                "objects": ["picture", "text"]
            }
        }
        self.client.post("/meme", json=payload)

    @task(4)
    def get_all_memes(self):
        self.client.get("/meme")

    @task(1)
    def get_one_meme(self):
        self.client.get(f"/meme/{meme_id}")

    @task(1)
    def edit_meme(self):
        editable_meme = {
            "text": "updated meme",
            "url": "https://blog.domotz.com/wp-content/uploads/2023/12/IMG_0196-828x1024.jpg",
            "tags": ["IT", "meme", "Voity v IT"],
            "info": {
                "colours": ["blue", "green"],
                "objects": ["picture", "text"]
            }
        }
        self.client.put(f"/meme/{meme_id}", json=editable_meme)

    @task(1)
    def delete_meme(self):
        self.client.delete(f"/meme/{meme_id}")

    @task(1)
    def test_get_all_memes_unauthorized(self):
        response = self.client.get("/get_all_memes_unauthorized")
        assert response.status_code == 401

    @task(1)
    def test_get_one_meme_unauthorized(self):
        response = self.client.get("/get_one_meme_unauthorized")
        assert response.status_code == 401

    @task(2)
    def test_create_meme_unauthorized(self):
        response = self.client.post("/create_meme_unauthorized", json=payload)
        assert response.status_code == 401

    @task(1)
    def test_edit_meme_unauthorized(self):
        response = self.client.put("/edit_meme_unauthorized", json=editable_meme)
        assert response.status_code == 401

    @task(1)
    def test_delete_meme_unauthorized(self):
        response = self.client.delete("/delete_meme_unauthorized")
        assert response.status_code == 401

    @task(2)
    def test_create_meme_negative_testing(self):
        response = self.client.post("/create_meme_negative_testing", json=negative_payload)
        assert response.status_code == 400

    @task(3)
    def test_check_token_alive(self):
        response = self.client.get("/check_token_alive")
        assert response.status_code == 200

    @task(1)
    def test_check_token_dead(self):
        response = self.client.get("/check_token_dead")
        assert response.status_code == 404

    @task(2)
    def test_create_meme_and_delete_as_different_user(self):
        response = self.client.post("/create_meme_and_delete_as_different_user", json=payload)
        assert response.status_code == 403
