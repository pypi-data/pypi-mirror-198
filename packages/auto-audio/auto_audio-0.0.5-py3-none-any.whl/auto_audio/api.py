# -*- coding: utf-8 -*-
__author__ = "hanayong"

import os
import re
import glob
import shutil
from datetime import date, datetime
import logging
import soundfile as sf

logger = logging.getLogger(__name__)


class file_object(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'" + self.name + "'"


class auto_audio:

    def __init__(self):
        self.current_path = os.getcwd()
        self.desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")

    @staticmethod
    def new_dir() -> None:

        # dir_name = os.path.join(self.desktop_path, 'auto_audio')
        dir_name = "C:\\Users\STudio\Desktop\\auto_audio"
        try:
            if os.path.isdir(dir_name):
                return None
        except FileNotFoundError:
            print("It couldn't find the directory. Please check your path.")
            return None

    # Convert wav to mp3
    @staticmethod
    def converter() -> str:
        # convert wav to
        mp3_files = glob.glob("C:\\Users\STudio\Desktop\\auto_audio\*.mp3")

        for file in mp3_files:
            print(file, end='\n')

        for file in mp3_files:
            # convert df
            # os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 44100 {file[:-4]}.wav""")
            os.system(f"""ffmpeg -i {file} -acodec pcm_s16le -ar 44100 {file[:-4]}.wav""")
            # remove .mp3 files
            os.remove(file)

        return f"{len(mp3_files)} is converted as WAV file."

    # Upload to Air Force
    @staticmethod
    def upload() -> None:

        wav_files = glob.glob("C:\\Users\STudio\Desktop\\auto_audio\*.wav")
        data = []
        for idx, elem in enumerate(wav_files):
            data = sf.read(elem)
            sf.write(f"\\\\kfox-pilot\AudioD\\27000\\{os.path.basename(elem)[:-4]}.WAV", data[0], data[1])
            print(f"{os.path.basename(elem)[:-4]} is Completed!")

        return None

    @staticmethod
    def christianMoveFiles():

        today = date.today().strftime("%m/%d/%y").replace('/', '')
        path_before = [r"C:\\Users\STudio\Dropbox\크리스챤 비젼_라디오서울",
                       r"C:\\Users\STudio\Dropbox\미주 기독교방송",
                       r"C:\\Users\STudio\Dropbox\성화 장로 교회_라디오서울",
                       r"C:\\Users\STudio\Dropbox\Radio Seoul\편성국 주말 녹음방송\.토3. 11PM LA Lately",
                       r"C:\\Users\STudio\Dropbox\(2018년 3월~4월)주님의 영광교회GCJC"]

        path_after = [r"C:\test\cut\1.src\\", r"C:\test\cut\1.src\미주기독교"] + \
                     [os.path.join(r"C:\test\cut\1.src\weekend", i) for i in os.listdir(r"C:\test\cut\1.src\weekend")]

        # 크리스천 비전 파일 복사

        christian_file_list = [file for file in os.listdir(path_before[0]) if file.endswith(r'.mp3')]
        vision_element_dict = {}
        upload_file = []

        for file in christian_file_list:
            vision_element_dict[file_object(file[0:6])] = file

        # for key, value in vision_element_dict.items():
        #     if str(key)[4:] >= today[4:]:
        #         if str(key)[:-2] > today[:-2]:
        #             shutil.copy(os.path.join(path_before[0], value), os.path.join(path_after[0], '크리스챤비젼'))
        #             logger.info(f"Copied {value}")
        #             logger.debug(f"Copied {value}")

        # 미주기독교 파일 복사

        # for path, dirs, files in os.walk(r'C:\Users\STudio\Dropbox\미주 기독교방송'):
        #     print(path, dirs, files)

    @staticmethod
    def christianityMovesFiles():
        path_before = r"C:\\Users\STudio\Dropbox\미주 기독교방송"
        path_after = r"C:\test\cut\1.src\미주기독교"

        for path, dirs, files in os.walk(r'C:\Users\STudio\Dropbox\미주 기독교방송'):
            print(path, dirs, files)

        today = datetime.today()
        year_str = str(today.year)
        start_date_str = year_str + '0311'
        end_date_str = year_str + '0315'

        # 0311과 0315 날짜를 datetime 객체로 변환하기
        start_date = datetime.strptime(start_date_str, '%Y%m%d')
        end_date = datetime.strptime(end_date_str, '%Y%m%d')

        # 0311과 0315 날짜 사이의 날짜 리스트 생성하기
        dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

        # 토요일과 일요일이 있는지 확인하기
        for date in dates:
            if date.weekday() == 5 or date.weekday() == 6:
                print(f'{date.date()}에는 토요일 또는 일요일이 있습니다.')

        # dirname =
        # result_files = []
        # # dirname에 있는 파일/디렉터리들을 검색하면서
        # for (path, dir, files) in os.walk(dirname):
        #     # 파일 이름이 '복음의메아리'를 포함하고, 확장자가 '.mp3'인 파일을 result_files에 추가
        #     for filename in files:
        #         if '복음의메아리' in filename and filename.endswith('.mp3'):
        #             result_files.append(os.path.join(path, filename))
        # return result_files
