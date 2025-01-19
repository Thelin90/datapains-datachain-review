from src.process import ProcessVideoMetadata
from datachain import func
import pandas as pd

if __name__ == '__main__':
    pvm = ProcessVideoMetadata()
    video_metadata = pvm.metadata
    video_metadata.print_schema()

    with pd.option_context("display.max_columns", None, "display.width", 1000):
        print(video_metadata.to_pandas())

    print(video_metadata.group_by(
        avg_video_fps=func.avg("video.fps")
    ).to_pandas())
