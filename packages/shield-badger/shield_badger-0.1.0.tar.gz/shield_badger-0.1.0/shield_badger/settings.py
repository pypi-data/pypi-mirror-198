# -*- coding: utf-8 -*-
"""Global settings for the application"""
import os

CWD = os.getcwd()

LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARNING")

START_BADGE_HOOK = "<!-- START BADGE HOOK -->"
END_BADGE_HOOK = "<!-- END BADGE HOOK -->"
