import uuid

from flask import jsonify


class MLModel:

    def __init__(self, model_id=None):

        # Model ID (GUID used to store the entity on backend and the wizatads on the blob storage
        if model_id is None:
            model_id = uuid.uuid4()
        self.model_id = model_id

        # Used to link the wizatads to the experiment who generate it
        self.experiment_id = None

        # The wizatads itself that is stored storage
        self.trained_model = None
        self.scaler = None

        # List of time-series column used as input for the wizatads (index is the timestamp)
        self.input_columns = None

        # Additional columns is generated by the wizatads (None if no additional columns is generated)
        self.output_columns = None

        # Set if the wizatads generate anomalies or not
        self.has_anomalies = False

        # Set the number of labels
        self.label_counts = 0

        # Set if wizatads has target_feat
        self.has_target_feat = False

    def jsonify(self):
        outputs = self.output_columns
        if outputs is None:
            outputs = []

        return jsonify({
            "model_id": str(self.model_id),
            "experiment_id": str(self.experiment_id),
            "input_columns": list(self.input_columns),
            "output_columns": list(outputs),
            "has_anomalies": str(self.has_anomalies),
            "labels_count": str(self.label_counts),
            "has_target_feat": str(self.has_target_feat)
        })

    def load_json(self, json):
        self.label_counts = int(json["labels_count"])
        self.input_columns = json["input_columns"]
        self.output_columns = json["output_columns"]
        self.has_anomalies = json["has_anomalies"]
        if ("has_target_feat" in json.keys()) and (json["has_target_feat"] == 'True'):
            self.has_target_feat = True

    def get_sample_payload(self):
        pl_columns = {"timestamp": "[timestamp]"}
        for hardwareId in self.input_columns:
            pl_columns[hardwareId] = "[" + hardwareId + "]"
        pl_json = {
            "model_id": str(self.model_id),
            "dataset": pl_columns
        }
        return pl_json

