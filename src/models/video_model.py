from datachain import DataModel


class Video(DataModel):
    video_id: str
    duration: float
    width: int
    height: int
    fps: float
    frame_count: int
    codec: str
