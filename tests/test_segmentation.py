from novelscope.segmentation import split_into_chapters


def test_fallback_single_chapter():
    text = "Once upon a time.\n\nThe end."
    chaps = split_into_chapters(text)
    assert len(chaps) >= 1
    assert chaps[0][0].startswith("Once upon")


def test_chapter_regex():
    text = "Chapter 1\nHello.\n\nChapter 2\nWorld."
    chaps = split_into_chapters(text)
    assert len(chaps) == 2
