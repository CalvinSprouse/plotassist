# plotlabelmanager.py

# Classes to help with labeling Matplotlib plots.

class PlotLabel:

    def __init__(self, key: object, text: str, plt_args: dict):
        # ensure that plt_args is at least an empty dict
        if plt_args is None:
            raise ValueError("plt_args cannot be None")
        if not isinstance(plt_args, dict):
            raise ValueError("plt_args must be a dict")

        # ensure text is a string
        if not isinstance(text, str):
            raise ValueError("text must be a string")

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

    def get_first_access(self) -> bool:
        return self.first_access

    def set_first_access(self, value: bool) -> None:
        self.first_access = value


class PlotLabelManager:

    def __init__(self):
        # define a dict to hold PlotLabel objects
        self.labels = {}

    def key_exists(self, key: object) -> bool:
        return key in self.labels

    def get_key_index(self, key: object) -> int:
        # check that key is in labels
        if not self.key_exists(key):
            raise ValueError(f"Key '{key}' not found")

        return list(self.labels.keys()).index(key)

    def get_key_count(self) -> int:
        return len(self.labels)

    def add(self, key: object, text: str, plt_args: dict) -> None:
        # check if key is already in list
        if self.key_exists(key):
            raise ValueError(f"Key '{key}' already exists")

        # create a new PlotLabel object and append
        plot_label = PlotLabel(key, text, plt_args)
        self.labels[plot_label.get_key()] = plot_label

    def get_args(self, key: object, include_text: bool = False) -> dict:
        # prepare the return dict
        return_dict = self.get_plot_label(key).get_plt_args()

        # check for label return
        if include_text:
            return_dict['label'] = self.get_text(key)

        return return_dict

    def get_text(self, key: object) -> str | None:
        # return de-duplicated label text
        plot_label = self.get_plot_label(key)
        if plot_label.get_first_access():
            plot_label.set_first_access(False)
            return plot_label.get_text()

        return None

    def get_all_labels(self) -> list[PlotLabel]:
        return self.labels.values()

    def get_plot_label(self, key: object) -> PlotLabel:
        # check if key exists
        if not self.key_exists(key):
            raise ValueError(f"Key '{key}' not found")

        return self.labels[key]