from ex48 import lexicon

def test_directions():
    assert lexicon.scan("north") == [('direction', 'north')]
    actual_result = lexicon.scan("north south east")
    expected_result = [
        ('direction', 'north'),
        ('direction', 'south'),
        ('direction', 'east')
    ]
    assert actual_result == expected_result

def test_verbs():
    actual_result = lexicon.scan("go")
    expected_result = [('verb', 'go')]
    assert actual_result == expected_result

    actual_result = lexicon.scan("go kill eat")
    expected_result = [
        ("verb", "go"),
        ("verb", "kill"),
        ("verb", "eat")
    ]
    assert actual_result == expected_result

def test_stops():
    actual_result = lexicon.scan("the")
    expected_result = [("stop", "the")]
    assert actual_result == expected_result

    actual_result = lexicon.scan("the in of")
    expected_result = [
        ("stop", "the"),
        ("stop", "in"),
        ("stop", "of")
    ]
    assert actual_result == expected_result

def test_nouns():
    actual_result = lexicon.scan("Bear")
    expected_result = [("noun","Bear")]
    assert actual_result == expected_result

    actual_result = lexicon.scan("bear princess")
    expected_result = [("noun", "bear"), ("noun", "princess")]
    assert actual_result == expected_result

def test_numbers():
    actual_result = lexicon.scan("1234")
    expected_result = [("number", 1234)]
    assert actual_result == expected_result

    actual_result = lexicon.scan("3 9124")
    expected_result = [("number", 3), ("number", 9124)]
    assert actual_result == expected_result

def test_error():
    actual_result = lexicon.scan("ASDFALJALSKDJF")
    expected_result = [("error", "ASDFALJALSKDJF")]
    assert actual_result == expected_result

    actual_result = lexicon.scan("bear IAS princess")
    expected_result = [
        ("noun", "bear"),
        ("error", "IAS"),
        ("noun", "princess")
    ]
    assert actual_result == expected_result