
from datachain import DataChain, C as _col
import io
import math
import imageio
from datachain import File

from src.models.video_model import Video


class ProcessVideoMetadata:
    def __init__(
        self,
        dataset_name: str = "videos",
        video_path: str = "src/data/",
    ) -> None:
        self.video_path = video_path
        self.dataset_name = dataset_name
        self.datachain = self._get_video_datachain()
        self.metadata = self._get_metadata()

    def _get_video_datachain(self) -> DataChain:
        return (
            DataChain.from_storage(self.video_path, anon=True)
            .settings(parallel=4, cache=True)
            .filter(_col("file.path").glob("*.mp4"))
            .save(self.dataset_name)
        )

    def _get_metadata(self):
        ds = DataChain.from_dataset(self.dataset_name)
        return ds.map(video=self.get_video_metadata).save()

    @staticmethod
    def get_video_metadata(file: File) -> Video:
        video_id = file.get_file_stem()
        file_ext = file.get_file_ext()
        file_read = file.read()

        reader = imageio.get_reader(io.BytesIO(file_read), format=file_ext, mode="?")
        meta = reader.get_meta_data()

        width, height = meta["size"]
        fps = meta["fps"]
        codec = meta["codec"]
        duration = meta["duration"]
        nframes = meta["nframes"]
        frame_count = int(duration * fps) if math.isinf(nframes) else int(nframes)

        return Video(
            video_id=video_id,
            duration=duration,
            width=width,
            height=height,
            fps=fps,
            frame_count=frame_count,
            codec=codec,
        )
