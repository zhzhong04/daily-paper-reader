import json

import pytest

from src.maintain.fetchers import fetch_arxiv


@pytest.mark.parametrize("api_fails", [False, True])
def test_arxiv_empty_response_and_request_failure_are_distinct(monkeypatch, tmp_path, api_fails):
    class ArxivClient:
        def results(self, search):
            if api_fails:
                raise OSError("arXiv unavailable")
            return iter(())

    output = tmp_path / "papers.json"
    crawl_state = tmp_path / "crawl_state.json"
    seen_state = tmp_path / "arxiv_seen.json"
    monkeypatch.setattr(fetch_arxiv.arxiv, "Client", lambda **kwargs: ArxivClient())
    monkeypatch.setattr(fetch_arxiv, "CATEGORIES_TO_FETCH", ["cs"])
    monkeypatch.setattr(fetch_arxiv, "CRAWL_STATE_FILE", str(crawl_state))
    monkeypatch.setattr(fetch_arxiv, "SEEN_IDS_FILE", str(seen_state))

    def fetch():
        fetch_arxiv.fetch_all_domains_metadata_robust(
            days=1, output_file=str(output), disable_supabase_read=True
        )

    if api_fails:
        with pytest.raises(RuntimeError, match="arXiv.*cs"):
            fetch()
        assert not output.exists()
        assert not crawl_state.exists()
        assert not seen_state.exists()
    else:
        fetch()
        assert json.loads(output.read_text()) == []
        assert crawl_state.is_file()
