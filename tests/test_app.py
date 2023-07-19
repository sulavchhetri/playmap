"""
    This module is used to test the app module of flask
"""

import pytest
from fastapi.testclient import TestClient
from playwright.async_api import async_playwright
from src.app import (
    app,
    identify_google_map_url
)


@pytest.mark.asyncio
def test_process():
    """
        This function is used to test /process path
    """
    url = "https://www.google.com/maps/search/restaurants/@27.709096171536316,85.32725337665443,19z?hl=en"

    with TestClient(app) as client:
        response = client.get(f"/process?q={url}")

        assert response.status_code == 200

        data = response.json()
        assert 'url' in data['data']
        assert "https://www.google.com/search?tbm=map&authuser=0&hl=en&gl=" in data['data']['url']


def test_identify_google_map_url():
    """
        This function is used to test whether the url is the one that
        contains the correct response by verifying the url
    """
    bad_url = "https://www.google.com/locationhistory/preview/mas?authuser=0&hl=en"\
        "&gl=np&pb=!1s101186138336890680135!2m3!1sglN8ZLC_AeeL4-EP__K8uA0!7e81"\
        "!15i20392!9m0!10m1!3b1!12m1!1i50"
    result = identify_google_map_url(bad_url)
    assert result is None

    good_url = "https://www.google.com/search?tbm=map&authuser=0&hl=en&gl=np&pb=!4m8!1m3!1d1715.3148399251074!2d-98.0545904!3d30.7006938!3m2!1i1024!2i768!4f13.1!7i20!8i40!10b1!12m30!1m1!18b1!2m3!5m1!6e2!20e3!6m12!4b1!49b1!63m0!73m0!74i150000!75b1!85b1!89b1!91b1!110m0!114b1!149b1!10b1!12b1!13b1!14b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m2!1sSNd6ZIrjKNLC4-EPl4OW4Ak!7e81!24m79!1m26!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m15!3b1!4b1!5b1!6b1!13b1!14b1!15b1!17b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m6!2b1!3b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i530!2i768!1m6!1m2!1i974!2i0!2m2!1i1024!2i768!1m6!1m2!1i0!2i0!2m2!1i1024!2i20!1m6!1m2!1i0!2i748!2m2!1i1024!2i768!34m19!2b1!3b1!4b1!6b1!7b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!46m1!1e9!47m0!49m6!3b1!6m2!1b1!2b1!7m1!1e3!50m43!1m39!2m7!1u3!4sOpen+now!5e1!9s0ahUKEwjirfORt6b_AhWH6jgGHRSdBTEQ_KkBCNwHKBY!10m2!3m1!1e1!2m7!1u2!4sTop+rated!5e1!9s0ahUKEwjirfORt6b_AhWH6jgGHRSdBTEQ_KkBCN0HKBc!10m2!2m1!1e1!2m7!1u1!4sCheap!5e1!9s0ahUKEwjirfORt6b_AhWH6jgGHRSdBTEQ_KkBCN4HKBg!10m2!1m1!1e1!2m7!1u1!4sUpscale!5e1!9s0ahUKEwjirfORt6b_AhWH6jgGHRSdBTEQ_KkBCN8HKBk!10m2!1m1!1e2!3m1!1u3!3m1!1u2!3m1!1u1!4BIAE!2e2!3m1!3b1!59BQ2dBd0Fn!67m3!7b1!10b1!14b0!69i648&q=cafes%20in%20Austin%2C%20TX%2078717&tch=1&ech=2&psi=SNd6ZIrjKNLC4-EPl4OW4Ak.1685772275832.1"

    result = identify_google_map_url(good_url)
    assert result



if __name__ == "__main__":
    pytest.main()