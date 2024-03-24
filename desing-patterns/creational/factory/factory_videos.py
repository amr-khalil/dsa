import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        pass
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass
    
    
class MP4Exporter(VideoExporter):
    def prepare_export(self, video_data):
        print(f'Preparing export of {video_data} to MP4')
        
    def do_export(self, folder: pathlib.Path):
        print(f'Exporting to MP4 in folder {folder}')


class AVIExporter:
    def prepare_export(self, video_data):
        print(f'Preparing export of {video_data} to AVI')
        
    def do_export(self, folder: pathlib.Path):
        print(f'Exporting to AVI in folder {folder}')
        

def get_exporter(exporter_type):
    factories = dict(mp4=MP4Exporter(), avi=AVIExporter())
    return factories[exporter_type]

if __name__ == '__main__':
    video_data = 'video_data'
    folder = pathlib.Path('myfolder')
    exporter = get_exporter('mp4')
    # print(exporter.prepare_export(video_data))
    exporter.do_export(folder)