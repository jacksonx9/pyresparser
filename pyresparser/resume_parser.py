# Author: Omkar Pathak

import os
import io
import spacy
from . import utils


class ResumeParser(object):

    def __init__(self, text):
        nlp = spacy.load('en_core_web_sm')
        self.__details = {
            'skills': None,
        }

        self.__text = ' '.join(text.split())
        self.__nlp = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        skills = utils.extract_skills(
                    self.__nlp,
                    self.__noun_chunks,
                )

        # extract skills
        self.__details['skills'] = skills
