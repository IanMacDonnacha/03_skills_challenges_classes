from lib.diary_entry import *

def test_diary_entry_formatted_string():
    formatted_string = DiaryEntry("One Piece", "Luffy, Zoro, Sanji, Chopper")
    assert formatted_string.format() == "One Piece: Luffy, Zoro, Sanji, Chopper"

def test_diary_entry_word_count_from_entry():
    word_count = DiaryEntry("One Piece", "Luffy, Zoro, Sanji, Chopper")
    assert word_count.count_words() == 4

def test_diary_entry_reading_time_from_entry():
    reading_time = DiaryEntry("One Piece", "Luffy, Zoro, Sanji, Chopper")
    assert reading_time.reading_time(200) == 0.02

def test_diary_entry_reading_time_chunk_from_entry_10wpm_1min():
    reading_chunk = DiaryEntry("One Piece", ["word" for i in range(0, 5)])
    assert reading_chunk.reading_chunk(10, 1) == "word word word word word"

def test_diary_entry_reading_time_chunk_from_entry_2wpm_2min():
    reading_chunk = DiaryEntry("One Piece", ["word" for i in range(0, 5)])
    assert reading_chunk.reading_chunk(2, 2) == "word word word word"