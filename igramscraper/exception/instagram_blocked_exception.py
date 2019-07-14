class InstagramBlockedException(Exception):
    def __init__(self, message = "", code = 401):
        super().__init__(f'{message}, Code:{code}')