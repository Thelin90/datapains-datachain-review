from datachain import DataChain
import polars as pl


class ProcessVideoMetadata:
    def __init__(
        self,
        dataset_name: str = "videos",
        video_path: str = "src/data/",
    ) -> None:
        self.datachain = DataChain.from_storage(video_path).save("videos")
        self.dataset_name = dataset_name

    def _save_datachain(self) -> None:
        self.datachain.save(self.dataset_name)

    def get_df(self) -> pl.DataFrame:
        return pl.from_pandas(self.datachain.to_pandas())
