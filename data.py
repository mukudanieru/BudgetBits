import json


class InformationManager:
    def __init__(self, file_name) -> None:
        """
        InformationManager: a class that can a program to handle
        loading and saving data (with a dictionary) using json.

        Args:
            file_name (str): for the name of the file
        """
        self.file_name = file_name

    def retrieve(self) -> dict:
        """
        This method simply retrieve the data from the file
        and return back that data.
        """
        with open(self.file_name, 'a+') as file:
            file.seek(0)
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return {}
            else:
                return data

    def save(self, data) -> None:
        """
        This method simply write and update data in the saving file.

        Args:
            data (any python data structure): any data types such as
            list, dictionary, etc.
        """
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
