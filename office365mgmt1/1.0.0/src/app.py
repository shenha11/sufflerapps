from walkoff_app_sdk.app_base import AppBase

class PythonPlayground(AppBase):
    __version__ = "1.0.0"
    app_name = "Office365_Mgt_API"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        add this row to check
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def run_me_1(self, planType,tenantID,clientID,clientSecret):
        #Poll last 10 min Office365
        #Parse json_data with key value data
        #planType = json_data['planType']
        #tenantID = json_data['tenantID']
        #clientID = json_data['clientID']
        #clientSecret = json_data['clientSecret']
        pollInterval = 10 #Assume minutes
        return office365poller.pollOffice(planType,tenantID,clientID,clientSecret,pollInterval)

    def run_me_2(self,planType,tenantID,clientID,clientSecret):
        #Poll last 23 horus or 1380 min Office365
        #Parse json_data with key value data
        #planType = json_data['planType']
        #tenantID = json_data['tenantID']
        #clientID = json_data['clientID']
        #clientSecret = json_data['clientSecret']
        pollInterval = 1380 #Assume minutes
        return office365poller.pollOffice(planType,tenantID,clientID,clientSecret,pollInterval)


    def run_me_3(self, json_data):
        return "Ran function 3"

    def hello_world(self):
        """
        Returns Hello World from the hostname the action is run on
        :return: Hello World from your hostname
        """
        message = f"Hello World from in workflow !"

        # This logs to the docker logs
        self.logger.info(message)

        return message

    # Write your data inside this function
    def run_o365poller(self, planType,tenantID,clientID,clientSecret, PollInterval,json_data):
        # It comes in as a string, so needs to be set to JSON
        try:
            #json_data = json.loads(json_data)
            #We are not using json_data structure at this time, getting creds directly
            pass
        except json.decoder.JSONDecodeError as e:
            return "Couldn't decode json: %s" % e

        # These are functions
        switcher = {
            "option1_to_run": self.run_me_1,
            "option2_to_run": self.run_me_2,
            "option3_hello_world": self.hello_world,
        }

        func = switcher.get(PollInterval, lambda: "Invalid function")
        return func(planType,tenantID,clientID,clientSecret)

if __name__ == "__main__":
    PythonPlayground.run()