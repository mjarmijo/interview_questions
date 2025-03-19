class LogAnalyzer:
    def __init__(self, logs: list[str]) -> None:
        self.logs = logs
        self._freq: dict[str, int] = {}
        self._addresses: list[str] = []

    @property
    def freq(self) -> dict[str, int]:
        return self._freq

    @property
    def addresses(self) -> list[str]:
        return list(self._addresses)

    def analyze(self) -> None:
        self._calculate_freq()  # This must be first
        self._get_top_addresses()

    def _calculate_freq(self) -> None:
        for log in self.logs:
            ip = log.split()[0]
            self._freq[ip] = self._freq.get(ip, 0) + 1
        self._freq = dict(
            sorted(self._freq.items(), key=lambda item: item[1], reverse=True)
        )

    def _get_top_addresses(self) -> list[str]:
        self._addresses = [
            ip
            for ip, count in self._freq.items()
            if count == list(self._freq.values())[0]
        ]
        self._addresses.sort()
