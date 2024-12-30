from youtube_transcript_api import YouTubeTranscriptApi
import os
from summarise import *
from get_video_id import *
from follow_up_question import *
from print_url import *

# Add and configure your gemini API key here
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def main(url):
    global video_id 
    video_id = get_yt_vid_url(url)
    global transcript 
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return summarise(transcript)

def question(question):
# Allows the user to ask a follop-up question
    global video_id
    global transcript
    follow_up_summary = follow_up(transcript, question)
    link = print_url(follow_up_summary, video_id)
    return (follow_up_summary, link)
