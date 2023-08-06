import json
import uuid
import sys

import dill
import requests
import pickle
import pandas

import sklearn
from .plot import Plot
from .request import Request
from .mlmodel import MLModel
from .script import Script
from .execution import Execution
from .dataframe_toolkit import DataFrameToolkit
from .dsapi_json_encoder import DSAPIEncoder
from .ds_dataframe import DSDataFrame
import msal
import os


class WizataDSAPIClient:

    def __init__(self,
                 client_id=None,
                 scope=None,
                 tenant_id=None,
                 username=None,
                 password=None,
                 domain="localhost",
                 protocol="https"):

        # properties
        self.domain = domain
        self.protocol = protocol

        # authentication
        self.__username = username
        self.__password = password

        self.__client_id = client_id
        self.__tenant_id = tenant_id
        if tenant_id is not None:
            self.__authority = "https://login.microsoftonline.com/" + tenant_id
        self.__scopes = [scope]

        self.__interactive_token = None

        self.__app = msal.PublicClientApplication(
            client_id=self.__client_id,
            authority=self.__authority
        )

    def authenticate(self):
        result = self.__app.acquire_token_interactive(
            scopes=self.__scopes,
            success_template="""<html><body>You are authenticated and your code is running, you can close this page.<script>setTimeout(function(){window.close()}, 3000);</script></body></html> """
        )
        self.__interactive_token = result["access_token"]

    def __url(self):
        return self.protocol + "://" + self.domain + "/dsapi/"

    def __token(self):
        # Interactive Authentication
        if self.__interactive_token is not None:
            return self.__interactive_token

        # Silent Authentication
        result = None
        accounts = self.__app.get_accounts(username=self.__username)
        if accounts:
            # If there is an account in the cache, try to get the token silently
            result = self.__app.acquire_token_silent(scopes=self.__scopes, account=accounts[0])

        if not result:
            # If there is no cached token, try to get a new token using the provided username and password
            result = self.__app.acquire_token_by_username_password(
                username=self.__username,
                password=self.__password,
                scopes=self.__scopes
            )

        return result["access_token"]

    def __header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.__token()}'
        }

    def __raise_error(self, response):
        json_content = response.json()
        if "errors" in json_content.keys():
            message = json_content["errors"][0]["message"]
            return RuntimeError(str(response.status_code) + " - " + message)
        else:
            return RuntimeError(str(response.status_code) + " - " + response.reason)

    def lists(self, str_type):
        """
        lists all elements of a specific entity.

        :param str_type: plural name of the entity (e.g. scripts, plots, mlmodels, dataframes...)
        :return: list of all elements with at least the id property.
        """
        if str_type == "scripts":
            response = requests.request("GET",
                                        self.__url() + "scripts/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                scripts = []
                for json_model in response.json():
                    scripts.append(Script(uuid.UUID(json_model["id"])))
                return scripts
            else:
                raise self.__raise_error(response)
        elif str_type == "plots":
            response = requests.request("GET",
                                        self.__url() + "plots/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                plots = []
                for plot in response.json():
                    plots.append(Plot(plot["id"]))
                return plots
            else:
                raise self.__raise_error(response)
        elif str_type == "mlmodels":
            response = requests.request("GET",
                                        self.__url() + "mlmodels/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                json_models = response.json()
                ml_models = []
                for json_model in json_models:
                    ml_models.append(MLModel(uuid.UUID(json_model["id"])))
                return ml_models
            else:
                raise self.__raise_error(response)
        elif str_type == "dataframes":
            response = requests.request("GET",
                                        self.__url() + "dataframes/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                json_dfs = response.json()
                dfs = []
                for json_model in json_dfs:
                    dfs.append(DSDataFrame(uuid.UUID(json_model["id"])))
                return dfs
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def get(self, obj):
        """
        get full content of an object identified with is id.

        :param obj: object of a supported entity with at list its id
        :return: object completed with all properties on server.
        """
        if isinstance(obj, MLModel):
            response = requests.request("GET",
                                        self.__url() + "mlmodels/" + str(obj.model_id) + "/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                mlmodel_bytes = response.content
                return pickle.loads(mlmodel_bytes)
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, Script):
            response = requests.request("GET",
                                        self.__url() + "scripts/" + str(obj.script_id) + "/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                script_bytes = response.content
                return dill.loads(script_bytes)
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, Plot):
            response = requests.request("GET",
                                        self.__url() + "plots/" + str(obj.plot_id) + "/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                obj.from_json(response.json())
                return obj
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, DSDataFrame):
            response = requests.request("GET",
                                        self.__url() + "dataframes/" + str(obj.df_id) + "/",
                                        headers=self.__header()
                                        )
            if response.status_code == 200:
                df_bytes = response.content
                return pickle.loads(df_bytes)
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def create(self, obj):
        """
        create and save an object on the server

        :param obj: object to save on the server (any id is ignored and replaced)
        :return: id of created object
        """
        if isinstance(obj, Script):
            response = requests.post(self.__url() + "scripts/",
                                     headers=self.__header(),
                                     data=dill.dumps(obj))
            if response.status_code == 200:
                obj.script_id = uuid.UUID(response.json()["id"])
                return obj.script_id
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def update(self, obj):
        """
        update and save an object on the server

        :param obj: object to update on the server
        :return: None
        """
        if isinstance(obj, Script):
            response = requests.put(self.__url() + "scripts/" + str(obj.script_id) + "/",
                                    headers=self.__header(),
                                    data=dill.dumps(obj))
            if response.status_code == 200:
                return
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def delete(self, obj):
        """
        delete an object on the server

        :param obj: object to delete including all content
        :return: None
        """
        if isinstance(obj, Script):
            response = requests.delete(self.__url() + "scripts" + "/" + str(obj.script_id) + "/",
                                       headers=self.__header())
            if response.status_code == 200:
                return
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, Plot):
            response = requests.delete(self.__url() + "plots" + "/" + str(obj.plot_id) + "/",
                                       headers=self.__header())
            if response.status_code == 200:
                return
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, MLModel):
            response = requests.delete(self.__url() + "mlmodels" + "/" + str(obj.model_id) + "/",
                                       headers=self.__header())
            if response.status_code == 200:
                return
            else:
                raise self.__raise_error(response)
        elif isinstance(obj, DSDataFrame):
            response = requests.delete(self.__url() + "dataframes" + "/" + str(obj.df_id) + "/",
                                       headers=self.__header())
            if response.status_code == 200:
                return
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def execute(self, execution: Execution = None) -> Execution:
        """
        execute an execution configuration on the server

        :param execution: Execution to execute on the server with configuration (Request, Script, ML Model, ...)
        :return: Execution updated with expected content (Data, Anomalies, Plots, ML Models, ...)
        """
        if execution is None:
            execution = Execution()
        if isinstance(execution, Execution):
            response = requests.post(self.__url() + "execute/",
                                     headers=self.__header(),
                                     data=json.dumps(execution.to_json(), cls=DSAPIEncoder))
            if response.status_code == 200:
                obj = response.json()
                if "plots" in obj.keys():
                    for plot in obj["plots"]:
                        execution.plots.append(self.get(Plot(plot_id=plot["id"])))
                if "models" in obj.keys():
                    for mlmodel in obj["models"]:
                        execution.models.append(self.get(MLModel(model_id=mlmodel["id"])))
                if "anomaliesList" in obj.keys():
                    execution.anomalies = obj["anomaliesList"]
                if "dataframe" in obj.keys():
                    execution.output_ds_dataframe = self.get(DSDataFrame(df_id=obj["dataframe"]["id"]))
                return execution
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("No execution have been loaded from parameters.")

    def validate(self, obj: Execution) -> Script:
        """
        run an execution to validate the script used.
        Do not store anything on the DS API nor return anything.
        In case of error, set the Script as invalid.

        :param obj: Execution to validate - must contains a dataframe or a query and a script
        :return: validated script properties (do not use update or it will invalidate the script)
        """
        if isinstance(obj, Execution):
            if obj.script is None:
                raise ValueError("Execution must contains at least a Script.")
            response = requests.post(self.__url() + "execute/validate",
                                     headers=self.__header(),
                                     data=json.dumps(obj.to_json(), cls=DSAPIEncoder))
            if response.status_code == 200:
                response_script = Script()
                response_script.from_json(response.json())
                return response_script
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def test(self, obj: Execution):
        """
        test an execution to validate the script used.
        Do not store anything on the DS API but return full content.

        :param obj: Execution to test - must contain a dataframe or a query and a script
        :return: results, including plots, data and models.
        """
        if isinstance(obj, Execution):
            if obj.script is None:
                raise ValueError("Execution must contains at least a Script.")
            response = requests.post(self.__url() + "execute/test",
                                     headers=self.__header(),
                                     data=json.dumps(obj.to_json(), cls=DSAPIEncoder))
            if response.status_code == 200:
                return pickle.loads(response.content)
            else:
                raise self.__raise_error(response)
        else:
            raise TypeError("Type not supported.")

    def query(self, query: Request) -> pandas.DataFrame:
        """
        execute a query to retrieve a panda dataframe

        :param query: Request object with at least datapoints, time frame and aggregation information
        :return: formatted panda dataframe
        """
        response = requests.request("POST", self.__url() + "execute/data",
                                    headers=self.__header(),
                                    data=json.dumps(query.prepare(), cls=DSAPIEncoder))
        if response.status_code == 200:
            return pickle.loads(response.content)
        else:
            raise self.__raise_error(response)
