import threading
import zipfile
from io import BytesIO
from pathlib import Path
from time import sleep

import click
from flask import Flask, send_file

from tunnel import Tunnel


class TappServer:

    def __init__(self, project_data, port=8080):

        self.port = port
        self.project_data = project_data
        self.app = Flask(self.__class__.__name__)
        self.app.route('/<download_name>')(self.serve_tapp)
        self.thread = threading.Thread(target=self.start_app)
        self.start()

    def start(self):
        self.thread.start()

    def start_app(self):
        self.app.run(port=self.port)

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def wait(self):
        while self.thread.is_alive():
            sleep(1)

    def serve_tapp(self, download_name):

        name = Path(download_name).stem
        if name not in self.project_data:
            raise ValueError(f'Unknown project "{name}"')

        path = self.project_data[name]

        byte_buffer = BytesIO()
        with zipfile.ZipFile(byte_buffer, mode='w') as zip_file:

            for file_path in path.iterdir():
                if file_path.is_file():
                    zip_file.write(file_path, arcname=file_path.name)

        byte_buffer.seek(0)

        response = send_file(byte_buffer, as_attachment=True, download_name=download_name)
        return response


def start(project_data, port):
    with TappServer(project_data, port) as tapp_server:
        with Tunnel(port) as tunnel:
            for name in tapp_server.project_data:
                msg = f'Serving project "{name}": `tasmota.urlfetch("{tunnel.tunnel.public_url}/{name}.tapp")`'
                print(msg)
            tapp_server.wait()


@click.command()
@click.option('--project', '-p', multiple=True, metavar='PATH')
@click.option('--port', '-pt', default=8080, show_default=True)
def start_cli(project, port):
    projects = project
    project_data = {}
    for project in projects:
        if ':' in project:
            name, path = project.split(':')
        else:
            name, path = Path(project).stem, project
        project_data[name] = Path(path).absolute()

    start(project_data, port)


if __name__ == '__main__':
    start_cli()
