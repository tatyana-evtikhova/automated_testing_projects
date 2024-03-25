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
