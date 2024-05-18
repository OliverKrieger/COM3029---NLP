import traceback

from .request_test import make_requests, request_over_time
from entity_recogniser.recogniser import run_model

def test_input():
    try:
        input_str = "OBS is an abbreviation"
        response = run_model("spaCy", input_str)
        assert response == [('OBS', 'AC'), ('is', 'O'), ('an', 'O'), ('abbreviation', 'O')]
        print("TEST (test_input) - Success!")
    except AssertionError:
        raise Exception("ERROR (test_input) - assertation failed!")
    except Exception:
        print(traceback.format_exc())
        raise Exception("ERROR (test_input) - test failed for non assertation reasons!")

def test_long_input():
    try:
        input_str = "So far, reviews investigating insulin pump therapy showed mixed results regarding the health - related quality of life (HRQOL) in paediatric diabetes patients.[13, 16, 17] According to recent publications,[15, 18–20] there is still a lack of adequately powered studies to underpin the advantages of CSII regarding QoL improvement for children diagnosed with DM and to potentially balance the higher treatment cost attached to it.[8] Thus, insulin pumps are – forty years after they were first introduced to the market – still not part of first - line recommendations in most countries around the world."
        response = run_model("spaCy", input_str)
        assert response == [('So', 'O'), ('far', 'O'), (',', 'O'), ('reviews', 'O'), ('investigating', 'O'), ('insulin', 'O'), ('pump', 'O'), ('therapy', 'O'), ('showed', 'O'), ('mixed', 'O'), ('results', 'O'), ('regarding', 'O'), ('the', 'O'), ('health - related quality of life', 'LF'), ('(', 'O'), ('HRQOL', 'AC'), (')', 'AC'), ('in', 'O'), ('paediatric', 'O'), ('diabetes', 'O'), ('patients.[13', 'O'), (',', 'O'), ('16', 'O'), (',', 'O'), ('17', 'O'), (']', 'O'), ('According', 'O'), ('to', 'O'), ('recent', 'O'), ('publications,[15', 'O'), (',', 'O'), ('18–20', 'O'), (']', 'O'), ('there', 'O'), ('is', 'O'), ('still', 'O'), ('a', 'O'), ('lack', 'O'), ('of', 'O'), ('adequately', 'O'), ('powered', 'O'), ('studies', 'O'), ('to', 'O'), ('underpin', 'O'), ('the', 'O'), ('advantages', 'O'), ('of', 'O'), ('CSII', 'AC'), ('regarding', 'O'), ('QoL', 'AC'), ('improvement', 'O'), ('for', 'O'), ('children', 'O'), ('diagnosed', 'O'), ('with', 'O'), ('DM', 'AC'), ('and', 'O'), ('to', 'O'), ('potentially', 'O'), ('balance', 'O'), ('the', 'O'), ('higher', 'O'), ('treatment', 'O'), ('cost', 'O'), ('attached', 'O'), ('to', 'O'), ('it.[8', 'O'), (']', 'O'), ('Thus', 'O'), (',', 'O'), ('insulin', 'O'), ('pumps', 'O'), ('are', 'O'), ('–', 'O'), ('forty', 'O'), ('years', 'O'), ('after', 'O'), ('they', 'O'), ('were', 'O'), ('first', 'O'), ('introduced', 'O'), ('to', 'O'), ('the', 'O'), ('market', 'O'), ('–', 'O'), ('still', 'O'), ('not', 'O'), ('part', 'O'), ('of', 'O'), ('first', 'O'), ('-', 'O'), ('line', 'O'), ('recommendations', 'O'), ('in', 'O'), ('most', 'O'), ('countries', 'O'), ('around', 'O'), ('the', 'O'), ('world', 'O'), ('.', 'O')]
        print("TEST (test_long_input) - Success!")
    except AssertionError:
        raise Exception("ERROR (test_long_input) - assertation failed!")
    except Exception:
        print(traceback.format_exc())
        raise Exception("ERROR (test_long_input) - test failed for non assertation reasons!")

def test_no_input():
    try:
        response = run_model("spaCy", "")
        assert response == []
        response = run_model("DistilBERT", "")
        assert response == []
        print("TEST (test_no_input) - Success!")
    except AssertionError:
        raise Exception("ERROR (test_no_input) - assertation failed!")
    except Exception:
        print(traceback.format_exc())
        raise Exception("ERROR (test_no_input) - test failed for non assertation reasons!")

def test_run_request_one_second():
    try:
        make_requests(1, "spaCy", "OBS is an abbreviation", "make_requests_fig_1s_spacy")
        make_requests(1, "DistilBERT", "OBS is an abbreviation", "make_requests_fig_1s_DistilBERT")
    except Exception:
        print(traceback.format_exc())

def test_run_request_ten_second():
    try:
        make_requests(10, "spaCy", "OBS is an abbreviation", "make_requests_fig_10s_spacy")
        make_requests(10, "DistilBERT", "OBS is an abbreviation", "make_requests_fig_10s_DistilBERT")
    except Exception:
        print(traceback.format_exc())

def test_run_200_requests():
    try:
        request_over_time(200, "spaCy", "OBS is an abbreviation", "requests_over_time_200_spacy")
        request_over_time(200, "DistilBERT", "OBS is an abbreviation", "requests_over_time_200_DistilBERT")
    except Exception:
        print(traceback.format_exc())

def run_tests() -> bool:
    try:
        test_input()
        test_long_input()
        test_no_input()
        # test_run_request_one_second()
        # test_run_request_ten_second()
        # test_run_200_requests()

        print("SUCCESS - All tests passed successfully!")
        return True
    except Exception:
        print(traceback.format_exc())
        return False