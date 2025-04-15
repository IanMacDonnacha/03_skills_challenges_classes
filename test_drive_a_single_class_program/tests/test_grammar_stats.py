from lib.grammar_stats import *

def test_for_capitalised_first_word_and_punctuation_period_at_end():
    check_func = GrammarStats()
    result = check_func.check("Test my grammar.")
    assert result == True

def test_for_capitalised_first_word_and_punctuation_exclamation_mark_at_end():
    check_func = GrammarStats()
    result = check_func.check("Test my grammar!")
    assert result == True

def test_for_capitalised_first_word_and_no_punctuation_period_at_end():
    check_func = GrammarStats()
    result = check_func.check("Test my grammar")
    assert result == False

def test_for_capitalised_first_word_and_no_punctuation_exclamation_mark_at_end():
    check_func = GrammarStats()
    result = check_func.check("Test my grammar")
    assert result == False

def test_for_noncapitalised_first_word_and_punctuation_exclamation_mark_at_end():
    check_func = GrammarStats()
    result = check_func.check("test my grammar!")
    assert result == False

def test_for_noncapitalised_first_word_and_punctuation_period_at_end():
    check_func = GrammarStats()
    result = check_func.check("test my grammar!")
    assert result == False

def test_grammar_stats_percentage_good_func_2_good_1_bad():
    check_func = GrammarStats()
    check_func.check("Test my grammar!")
    check_func.check("Test my grammar.")
    check_func.check("test my grammar!")
    result = check_func.percentage_good()
    assert result == 67

def test_grammar_stats_percentage_good_func_2_good_2_bad():
    check_func = GrammarStats()
    check_func.check("Test my grammar!")
    check_func.check("Test my grammar.")
    check_func.check("test my grammar!")
    check_func.check("test my grammar!")
    result = check_func.percentage_good()
    assert result == 50