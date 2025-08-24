import uuid

class Util:
    @staticmethod
    def generate_uuid() -> str:
        return str(uuid.uuid4())