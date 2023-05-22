from configparser import ConfigParser

config = ConfigParser()
config.read("application.conf")


class Service:
    port = config["SERVICE"]["port"]
    host = config["SERVICE"]["host"]
    uri = config["MONGO_DB"]["mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"]
    database_name = config["MONGO_DB"]["database_name"]
    collection_name = config["MONGO_DB"]["collection_name"]


service_object = Service()
