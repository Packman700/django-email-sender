class RecaptchaLogicSession:
    def __init__(self, request):
        self.request = request

    @property
    def invalid_submits_counter(self):
        return self.request.session.get("InvalidSubmitsCounter", 0)

    @invalid_submits_counter.setter
    def invalid_submits_counter(self, value):
        self.request.session["InvalidSubmitsCounter"] = value

    @invalid_submits_counter.deleter
    def invalid_submits_counter(self):
        del self.request.session["InvalidSubmitsCounter"]

    @property
    def valid_submits_counter(self):
        return self.request.session.get("ValidSubmitsCounter", 0)

    @valid_submits_counter.setter
    def valid_submits_counter(self, value):
        self.request.session["ValidSubmitsCounter"] = value

    @valid_submits_counter.deleter
    def valid_submits_counter(self):
        del self.request.session["ValidSubmitsCounter"]

    @property
    def use_recaptcha(self):
        invalid_submits_counter = self.invalid_submits_counter
        valid_submits_counter = self.valid_submits_counter
        if invalid_submits_counter > 4 or valid_submits_counter > 0:
            return True
        else:
            return False
