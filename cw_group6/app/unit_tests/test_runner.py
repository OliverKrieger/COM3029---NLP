import traceback

from entity_recogniser.recogniser import run_model

def test_input():
    try:
        input_str = "OBS is an abbreviation"
        response = run_model("spaCy", input_str)
        assert response == [('OBS', 'AC'), ('is', 'O'), ('an', 'O'), ('abbreviation', 'O')]
    except Exception:
        print("ERROR (test_input) - assertation failed!")
        print(traceback.format_exc())

def test_long_input():
    try:
        input_str = "So far, reviews investigating insulin pump therapy showed mixed results regarding the health - related quality of life (HRQOL) in paediatric diabetes patients.[13, 16, 17] According to recent publications,[15, 18–20] there is still a lack of adequately powered studies to underpin the advantages of CSII regarding QoL improvement for children diagnosed with DM and to potentially balance the higher treatment cost attached to it.[8] Thus, insulin pumps are – forty years after they were first introduced to the market – still not part of first - line recommendations in most countries around the world."
        response = run_model("spaCy", input_str)
        assert response == [('So', 'O'), ('far', 'O'), (',', 'O'), ('reviews', 'O'), ('investigating', 'O'), ('insulin', 'O'), ('pump', 'O'), ('therapy', 'O'), ('showed', 'O'), ('mixed', 'O'), ('results', 'O'), ('regarding', 'O'), ('the', 'O'), ('health - related quality of life', 'LF'), ('(', 'O'), ('HRQOL', 'AC'), (')', 'AC'), ('in', 'O'), ('paediatric', 'O'), ('diabetes', 'O'), ('patients.[13', 'O'), (',', 'O'), ('16', 'O'), (',', 'O'), ('17', 'O'), (']', 'O'), ('According', 'O'), ('to', 'O'), ('recent', 'O'), ('publications,[15', 'O'), (',', 'O'), ('18–20', 'O'), (']', 'O'), ('there', 'O'), ('is', 'O'), ('still', 'O'), ('a', 'O'), ('lack', 'O'), ('of', 'O'), ('adequately', 'O'), ('powered', 'O'), ('studies', 'O'), ('to', 'O'), ('underpin', 'O'), ('the', 'O'), ('advantages', 'O'), ('of', 'O'), ('CSII', 'AC'), ('regarding', 'O'), ('QoL', 'AC'), ('improvement', 'O'), ('for', 'O'), ('children', 'O'), ('diagnosed', 'O'), ('with', 'O'), ('DM', 'AC'), ('and', 'O'), ('to', 'O'), ('potentially', 'O'), ('balance', 'O'), ('the', 'O'), ('higher', 'O'), ('treatment', 'O'), ('cost', 'O'), ('attached', 'O'), ('to', 'O'), ('it.[8', 'O'), (']', 'O'), ('Thus', 'O'), (',', 'O'), ('insulin', 'O'), ('pumps', 'O'), ('are', 'O'), ('–', 'O'), ('forty', 'O'), ('years', 'O'), ('after', 'O'), ('they', 'O'), ('were', 'O'), ('first', 'O'), ('introduced', 'O'), ('to', 'O'), ('the', 'O'), ('market', 'O'), ('–', 'O'), ('still', 'O'), ('not', 'O'), ('part', 'O'), ('of', 'O'), ('first', 'O'), ('-', 'O'), ('line', 'O'), ('recommendations', 'O'), ('in', 'O'), ('most', 'O'), ('countries', 'O'), ('around', 'O'), ('the', 'O'), ('world', 'O'), ('.', 'O')]
    except Exception:
        print("ERROR (test_long_input) - assertation failed!")
        print(traceback.format_exc())

def test_no_input():
    try:
        response = run_model("spaCy", "")
        assert response == []
        response = run_model("DistilBERT", "")
        assert response == []
    except Exception:
        print("ERROR (test_no_input) - assertation failed!")
        print(traceback.format_exc())

def test_array_input():
    print()

def test_JSON_input():
    # has to have tokens fields
    # ner tags fields
    print()

def test_invalid_array_input():
    print()

def test_invalid_JSON_input():
    print()