# Copyright 2022-2023 The Wordcab Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wordcab API Config variables."""

from pathlib import Path


AVAILABLE_AUDIO_FORMATS = [".flac", ".m4a", ".mp3", ".mpga", ".ogg", ".wav"]
AVAILABLE_GENERIC_FORMATS = [".json", ".txt"]
AVAILABLE_PLAN = ["free", "metered", "paid"]
CONTEXT_ELEMENTS = ["discussion_points", "issue", "keywords", "next_steps", "purpose"]
EXTRACT_AVAILABLE_STATUS = [
    "Deleted",
    "Error",
    "Extracting",
    "ExtractionComplete",
    "ItemQueued",
    "Pending",
    "PreparingExtraction",
]
EXTRACT_PIPELINES = [
    "questions_answers",
    "topic_segments",
    "emotions",
    "speaker_talk_ratios",
]
LIST_JOBS_ORDER_BY = [
    "time_started",
    "time_completed",
    "-time_started",
    "-time_completed",
]
REQUEST_TIMEOUT = 30
SOURCE_LANG = ["de", "en", "es", "fr", "it", "nl", "pt", "sv"]
SOURCE_OBJECT_MAPPING = {
    "generic": "GenericSource",
    "audio": "AudioSource",
    "wordcab_transcript": "WordcabTranscriptSource",
    "signed_url": "SignedUrlSource",
    "assembly_ai": "AssemblyAISource",
    "deepgram": "DeepgramSource",
    "rev_ai": "RevSource",
    "vtt": "VTTSource",
}
SUMMARIZE_AVAILABLE_STATUS = [
    "Deleted",
    "Error",
    "ItemQueued",
    "Pending",
    "PreparingSummary",
    "PreparingTranscript",
    "Summarizing",
    "SummaryComplete",
    "Transcribing",
    "TranscriptComplete",
]
SUMMARY_LENGTHS_RANGE = [1, 5]
SUMMARY_PIPELINES = ["transcribe", "summarize"]
SUMMARY_TYPES = ["brief", "conversational", "narrative", "no_speaker"]
TARGET_LANG = ["de", "en", "es", "fr", "it", "pt", "sv"]
WORDCAB_TOKEN_FOLDER = Path.home() / ".wordcab" / "token"  # noqa: S105
