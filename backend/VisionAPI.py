import requests


class VisionAPI:
    def __init__(self):
        self.url = 'https://vision.googleapis.com/v1p1beta1/images:annotate'
        self.KEY = "AIzaSyB1i8WBPtqil7aNJO4X5EI4xAo-fTs-tmY"
        self.maxResults = 10

    def build_url(self):
        return self.url + "?key=" + self.KEY

    def build_image_json(self, image_url):
        ImageSource = "{\"imageUri\": \"" + image_url + " \"}"
        Image = "{\"source\":" + ImageSource + "}"
        Feature = "{\"type\": \"LABEL_DETECTION\", \"maxResults\": " + str(self.maxResults) + "}"
        image_json = "{\"image\":" + Image + ",\"features\": [" + Feature + "]}"
        return image_json

    def get_image_labels(self, image_urls):
        #image_urls = ["https://pbs.twimg.com/media/DVru7X_UQAUfVAr.jpg"]

        json = "{\"requests\": ["
        for image_url in image_urls:
            json += self.build_image_json(image_url) + ","
        json += "]}"

        print(json)

        r = requests.post(self.build_url(), data=json).json()

        total_labels = []
        for resp in r["responses"]:
            labels = []
            for label in resp["labelAnnotations"]:
                labels.append({"Label": label["description"], "Score": label["score"]})
            total_labels.append(labels)
        return total_labels
