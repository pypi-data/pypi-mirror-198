import json
import requests
import tempfile
import logging
import uuid
import operator
import pydub

import cloudlanguagetools.service
import cloudlanguagetools.constants
import cloudlanguagetools.languages
import cloudlanguagetools.ttsvoice
import cloudlanguagetools.translationlanguage
import cloudlanguagetools.transliterationlanguage
import cloudlanguagetools.errors

NAVER_VOICE_SPEED_DEFAULT = 0
NAVER_VOICE_PITCH_DEFAULT = 0

class NaverVoice(cloudlanguagetools.ttsvoice.TtsVoice):
    def __init__(self, audio_language, name, gender, description, voice_type):
        self.service = cloudlanguagetools.constants.Service.Naver
        self.service_fee = cloudlanguagetools.constants.ServiceFee.paid
        self.audio_language = audio_language
        self.name = name
        self.gender = gender
        self.description = description
        self.voice_type = voice_type

    def get_voice_key(self):
        return {
            'name': self.name
        }

    def get_voice_shortname(self):
        return f'{self.description} ({self.voice_type})'

    def get_options(self):
        return {
            'speed' : {
                'type': 'number_int',
                'min': -5,
                'max': 5,
                'default': NAVER_VOICE_SPEED_DEFAULT
            },
            'pitch': {
                'type': 'number_int',
                'min': -5,
                'max': 5,
                'default': NAVER_VOICE_PITCH_DEFAULT
            }
        }

class NaverTranslationLanguage(cloudlanguagetools.translationlanguage.TranslationLanguage):
    def __init__(self, language, language_id):
        self.service = cloudlanguagetools.constants.Service.Naver
        self.service_fee = cloudlanguagetools.constants.ServiceFee.paid
        self.language = language
        self.language_id = language_id

    def get_language_id(self):
        return self.language_id

class NaverService(cloudlanguagetools.service.Service):
    def __init__(self):
        pass

    def configure(self, config):
        self.client_id = config['client_id']
        self.client_secret = config['client_secret']

    def get_translation(self, text, from_language_key, to_language_key):
        url = 'https://naveropenapi.apigw.ntruss.com/nmt/v1/translation'
        headers = {
            'X-NCP-APIGW-API-KEY-ID': self.client_id,
            'X-NCP-APIGW-API-KEY': self.client_secret
        }

        data = {
            'text': text,
            'source': from_language_key,
            'target': to_language_key
        }

        # alternate_data = 'speaker=clara&text=vehicle&volume=0&speed=0&pitch=0&format=mp3'
        response = requests.post(url, json=data, headers=headers, timeout=cloudlanguagetools.constants.RequestTimeout)
        if response.status_code == 200:
            response_data = response.json()
            return response_data['message']['result']['translatedText']

        error_message = f'Status code: {response.status_code}: {response.content}'
        raise cloudlanguagetools.errors.RequestError(error_message)


    def get_tts_audio(self, text, voice_key, options):
        output_temp_file = tempfile.NamedTemporaryFile()
        output_temp_filename = output_temp_file.name

        url = 'https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-NCP-APIGW-API-KEY-ID': self.client_id,
            'X-NCP-APIGW-API-KEY': self.client_secret
        }

        data = {
            'text': text,
            'speaker': voice_key['name'],
            'speed': options.get('speed', NAVER_VOICE_SPEED_DEFAULT),
            'pitch': options.get('pitch', NAVER_VOICE_PITCH_DEFAULT)
        }

        # alternate_data = 'speaker=clara&text=vehicle&volume=0&speed=0&pitch=0&format=mp3'
        response = requests.post(url, data=data, headers=headers, timeout=cloudlanguagetools.constants.RequestTimeout)
        if response.status_code == 200:
            with open(output_temp_filename, 'wb') as audio:
                audio.write(response.content)
            return output_temp_file

        response_data = response.json()
        error_message = f'Status code: {response.status_code}: {response_data}'
        raise cloudlanguagetools.errors.RequestError(error_message)

    def get_tts_voice_list(self):
        # returns list of TtSVoice
        return [
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.en_US, 'clara', cloudlanguagetools.constants.Gender.Female, 'Clara', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.en_US, 'danna', cloudlanguagetools.constants.Gender.Female, 'Anna', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.en_US, 'djoey', cloudlanguagetools.constants.Gender.Female, 'Joy', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.en_US, 'matt', cloudlanguagetools.constants.Gender.Male, 'Matt', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.es_ES, 'carmen', cloudlanguagetools.constants.Gender.Female, 'Carmen', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.es_ES, 'jose', cloudlanguagetools.constants.Gender.Male, 'Jose', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'dayumu', cloudlanguagetools.constants.Gender.Male, 'Ayumu', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'ddaiki', cloudlanguagetools.constants.Gender.Male, 'Daiki', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'deriko', cloudlanguagetools.constants.Gender.Female, 'Eriko', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'dhajime', cloudlanguagetools.constants.Gender.Male, 'Hajime', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'dmio', cloudlanguagetools.constants.Gender.Female, 'Mio', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'dnaomi_formal', cloudlanguagetools.constants.Gender.Female, 'Naomi (news)', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'dnaomi_joyful', cloudlanguagetools.constants.Gender.Female, 'Naomi (joy)', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'driko', cloudlanguagetools.constants.Gender.Female, 'Riko', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'nnaomi', cloudlanguagetools.constants.Gender.Female, 'Naomi', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'nsayuri', cloudlanguagetools.constants.Gender.Female, 'Sayuri', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'ntomoko', cloudlanguagetools.constants.Gender.Female, 'Tomoko', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ja_JP, 'shinji', cloudlanguagetools.constants.Gender.Male, 'Shinji', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'dara_ang', cloudlanguagetools.constants.Gender.Female, 'Ara (angry)', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'dara-danna', cloudlanguagetools.constants.Gender.Female, 'Ara&Anna', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'dsinu-matt', cloudlanguagetools.constants.Gender.Male, 'Shinwoo & Matt', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'jinho', cloudlanguagetools.constants.Gender.Male, 'Jinho', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'mijin', cloudlanguagetools.constants.Gender.Female, 'Mijin', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'napple', cloudlanguagetools.constants.Gender.Female, 'Neulbom', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nara_call', cloudlanguagetools.constants.Gender.Female, 'Ara (agent)', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nara', cloudlanguagetools.constants.Gender.Female, 'Ara', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nbora', cloudlanguagetools.constants.Gender.Female, 'Bora', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'ndain', cloudlanguagetools.constants.Gender.Female, 'Dain', 'Premium (Child)'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nes_c_hyeri', cloudlanguagetools.constants.Gender.Female, 'Hyeri', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nes_c_kihyo', cloudlanguagetools.constants.Gender.Male, 'Kihyo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nes_c_mikyung', cloudlanguagetools.constants.Gender.Female, 'Mikyung', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nes_c_sohyun', cloudlanguagetools.constants.Gender.Female, 'Sohyeon', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'neunseo', cloudlanguagetools.constants.Gender.Female, 'Eunseo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'neunwoo', cloudlanguagetools.constants.Gender.Male, 'Eunwoo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'neunyoung', cloudlanguagetools.constants.Gender.Female, 'Eunyoung ', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'ngaram', cloudlanguagetools.constants.Gender.Female, 'Garam', 'Premium (Child)'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'ngoeun', cloudlanguagetools.constants.Gender.Female, 'Goeun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nhajun', cloudlanguagetools.constants.Gender.Male, 'Hajun', 'Premium (Child)'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nheera', cloudlanguagetools.constants.Gender.Female, 'Heera', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nihyun', cloudlanguagetools.constants.Gender.Female, 'Lee Hyun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njaewook', cloudlanguagetools.constants.Gender.Male, 'Jaewook', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njangj', cloudlanguagetools.constants.Gender.Female, 'Dream', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njihun', cloudlanguagetools.constants.Gender.Male, 'Jihun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njihwan', cloudlanguagetools.constants.Gender.Male, 'Jihwan', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njinho', cloudlanguagetools.constants.Gender.Male, 'Jinho', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njiwon', cloudlanguagetools.constants.Gender.Female, 'Jiwon', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njiyun', cloudlanguagetools.constants.Gender.Female, 'Jiyun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njonghyun', cloudlanguagetools.constants.Gender.Male, 'Jonghyun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njooahn', cloudlanguagetools.constants.Gender.Male, 'Jooan', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'njoonyoung', cloudlanguagetools.constants.Gender.Male, 'Junyoung', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nkitae', cloudlanguagetools.constants.Gender.Male, 'Kitae', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nkyunglee', cloudlanguagetools.constants.Gender.Female, 'Kyungri', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nkyungtae', cloudlanguagetools.constants.Gender.Male, 'Gyeongtae', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nkyuwon', cloudlanguagetools.constants.Gender.Male, 'Gyuwon', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nminjeong', cloudlanguagetools.constants.Gender.Female, 'Minjeong', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nminsang', cloudlanguagetools.constants.Gender.Male, 'Minsang', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nminseo', cloudlanguagetools.constants.Gender.Female, 'Minseo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nminyoung', cloudlanguagetools.constants.Gender.Female, 'Minyoung', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nnarae', cloudlanguagetools.constants.Gender.Female, 'Narae', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'noyj', cloudlanguagetools.constants.Gender.Female, 'Bomdal', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nraewon', cloudlanguagetools.constants.Gender.Male, 'Raewon', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nseonghoon', cloudlanguagetools.constants.Gender.Male, 'Seonghun', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nseungpyo', cloudlanguagetools.constants.Gender.Male, 'Seungpyo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nsinu', cloudlanguagetools.constants.Gender.Male, 'Shinwoo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nsiyoon', cloudlanguagetools.constants.Gender.Male, 'Siyoon', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nsujin', cloudlanguagetools.constants.Gender.Female, 'Sujin', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nsunhee', cloudlanguagetools.constants.Gender.Female, 'Seonhee', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nsunkyung', cloudlanguagetools.constants.Gender.Female, 'Seonkyung', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'ntaejin', cloudlanguagetools.constants.Gender.Male, 'Taejin', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'ntiffany', cloudlanguagetools.constants.Gender.Female, 'Giseo', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nwontak', cloudlanguagetools.constants.Gender.Male, 'Wontak', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nwoosik', cloudlanguagetools.constants.Gender.Male, 'Woosik', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyeji', cloudlanguagetools.constants.Gender.Female, 'Yeji', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyejin', cloudlanguagetools.constants.Gender.Female, 'Yejin', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyoungil', cloudlanguagetools.constants.Gender.Male, 'Youngil', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyoungmi', cloudlanguagetools.constants.Gender.Female, 'Youngmi', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyujin', cloudlanguagetools.constants.Gender.Female, 'Yujin', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'nyuna', cloudlanguagetools.constants.Gender.Female, 'Yuna', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'vara', cloudlanguagetools.constants.Gender.Female, 'Ara', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'vdain', cloudlanguagetools.constants.Gender.Female, 'Dain', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'vhyeri', cloudlanguagetools.constants.Gender.Female, 'Hyeri', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'vmikyung', cloudlanguagetools.constants.Gender.Female, 'Mikyung', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.ko_KR, 'vyuna', cloudlanguagetools.constants.Gender.Female, 'Yuna', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.zh_CN, 'liangliang', cloudlanguagetools.constants.Gender.Male, 'Liangliang', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.zh_CN, 'meimei', cloudlanguagetools.constants.Gender.Female, 'Meimei', 'General'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.zh_TW, 'chiahua', cloudlanguagetools.constants.Gender.Female, 'Chahwa', 'Premium'),
            NaverVoice(cloudlanguagetools.languages.AudioLanguage.zh_TW, 'kuanlin', cloudlanguagetools.constants.Gender.Male, 'Guanlin', 'Premium'),



        ]

    def get_translation_language_list(self):
        result = [
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.ko, 'ko'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.en, 'en'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.ja, 'ja'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.zh_cn, 'zh-CN'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.zh_tw, 'zh-TW'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.vi, 'vi'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.id_, 'id'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.th, 'th'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.de, 'de'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.ru, 'ru'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.it, 'it'),
            NaverTranslationLanguage(cloudlanguagetools.languages.Language.fr, 'fr'),
        ]
        return result

    def get_transliteration_language_list(self):
        result = []
        return result
   