from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        try:
            toml_data = toml.loads(content)

            project_info = toml_data.get("project", {})
            name = toml_data["tool"]["poetry"].get("name", "Default Name")
            description = toml_data["tool"]["poetry"].get("description", "Default Description")
            license = toml_data["tool"]["poetry"].get("license", "Default License")
            authors = toml_data["tool"]["poetry"].get("authors", [])
            dependencies = [dep for dep in toml_data["tool"]["poetry"]["dependencies"].keys()]
            dev_dependencies = [dep for dep in toml_data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()]

        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
            return Project(name, description, license, authors, dependencies, dev_dependencies)

        except toml.TomlDecodeError as e:
            print("error")
            return None
