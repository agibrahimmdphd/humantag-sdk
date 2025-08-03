import json
import time

class WatermarkEmbedder:
    def __init__(self, device_id="HUMANTAG123"):
        self.device_id = device_id

    def generate_payload(self, entropy_score, signature):
        payload = {
            "timestamp": int(time.time()),
            "entropy_score": entropy_score,
            "device_id": self.device_id,
            "signature": signature
        }
        return json.dumps(payload, indent=2)

    def embed_to_media(self, media_file="sample_video.mp4", payload=None):
        print(f"Simulated embedding payload into: {media_file}")
        return {
            "media_file": media_file,
            "embedded_payload": payload,
            "status": "success"
        }