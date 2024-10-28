# plotlabelmanager.py

# Classes to help with labeling Matplotlib plots.

class PlotLabel:

    def __init__(self, key: object, text: str, plt_args: dict):
        # save data
        self.key = key
        self.text = text
        self.plt_args = plt_args

        # save a boolean to record first access
        self.first_access = True

    def get_key(self) -> object:
        return self.key

    def get_text(self) -> str:
        return self.text

    def get_plt_args(self) -> dict:
        return self.plt_args

    def access_label(self) -> str | None:
        # check for first access
        if not self.first_access:
            # return nothing to prevent duplicate entries
            return None

        # return the label text and record first access complete
        self.first_access = False
        return self.text


class PlotLabelManager:

    def __init__(self):
        # define a dict to hold PlotLabel objects
        self.labels = {}

    def _append(self, plot_label: PlotLabel) -> None:
        self.labels[plot_label.get_key()] = plot_label

    def key_exists(self, key: object) -> bool:
        return key in self.labels

    def add(self, key: object, text: str, plt_args: dict) -> None:
        # check if key is already in list
        if self.key_exists(key):
            raise ValueError(f"Key '{key}' already exists")

        # create a new PlotLabel object and append
        label = PlotLabel(key, text, plt_args)
        self._append(label)

    def get_plt_args(self, key: object, include_label: bool = False) -> dict:
        # check if key exists
        if not self.key_exists(key):
            raise ValueError(f"Key '{key}' not found")

        # prepare the return dict
        return_dict = self.labels[key].get_plt_args()

        # check for label return
        if include_label:
            return_dict["label"] = self.get_label(key)

        return return_dict

    def get_label(self, key: object) -> str | None:
        # check if key exists
        if not self.key_exists(key):
            raise ValueError(f"Key '{key}' not found")

        return self.labels[key].access_label()

    def get_all_labels(self) -> list[PlotLabel]:
        return self.labels.values()
