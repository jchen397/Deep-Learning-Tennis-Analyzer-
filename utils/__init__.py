# To decide what functions can be exposed outside of the utils folder
# have utils/__init__.py file with the following content:
# from utils folder import function

from .video_utils import read_video, save_video