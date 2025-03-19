from log_analysis.log_analyzer import LogAnalyzer


class TestLogAnalyzer:
    def test_empty(self):
        log_analyzer = LogAnalyzer([])
        log_analyzer.analyze()
        assert log_analyzer.freq == {}
        assert len(log_analyzer.addresses) == 0

    def test_simple(self):
        logs = [
            "192.168.1.1 - GET 2022-01-01",
        ]

        log_analyzer = LogAnalyzer(logs)
        log_analyzer.analyze()
        assert len(log_analyzer.freq.keys()) == 1
        assert log_analyzer.freq["192.168.1.1"] == 1
        assert len(log_analyzer.addresses) == 1
        assert log_analyzer.addresses[0] == "192.168.1.1"

    def test_complex(self):
        logs = [
            "192.168.1.4 - GET 2022-01-01",
            "192.168.1.4 - GET 2022-01-01",
            "192.168.1.4 - GET 2022-01-01",
            "192.168.1.4 - GET 2022-01-01",
            "192.168.1.3 - GET 2022-01-01",
            "192.168.1.1 - GET 2022-01-01",
            "192.168.1.1 - GET 2022-01-01",
            "192.168.1.3 - GET 2022-01-01",
            "192.168.1.2 - GET 2022-01-01",
            "192.168.1.2 - GET 2022-01-01",
            "192.168.1.1 - GET 2022-01-01",
            "192.168.1.2 - GET 2022-01-01",
            "192.168.1.3 - GET 2022-01-01",
            "192.168.1.1 - GET 2022-01-01",
        ]

        log_analyzer = LogAnalyzer(logs)
        log_analyzer.analyze()
        assert len(log_analyzer.freq.keys()) == 4
        assert len(log_analyzer.addresses) == 2
        assert log_analyzer.addresses[0] == "192.168.1.1"
        assert log_analyzer.addresses[1] == "192.168.1.4"
