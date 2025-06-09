from collections import Counter

# ----------------------------------------
# 🔒 Z構文危険度マップ（Z1〜Z27）
# ----------------------------------------

Z_RISK_LEVELS = {
    "Z1": 1,  "Z2": 3,  "Z3": 3,  "Z4": 2,  "Z5": 2,
    "Z6": 1,  "Z7": 2,  "Z8": 2,  "Z9": 3,  "Z10": 3,
    "Z11": 4, "Z12": 2, "Z13": 2, "Z14": 2, "Z15": 3,
    "Z16": 3, "Z17": 2, "Z18": 2, "Z19": 2, "Z20": 2,
    "Z21": 3, "Z22": 3, "Z23": 5, "Z24": 5, "Z25": 5,
    "Z26": 5, "Z27": 5
}

# ----------------------------------------
# 🧠 Z構文連続検出トラッカー
# ----------------------------------------

class ZContextTracker:
    def __init__(self):
        self.history = []

    def register(self, z_flags: list):
        self.history.append(z_flags)
        if len(self.history) > 10:
            self.history.pop(0)

    def get_z_counts(self) -> Counter:
        return Counter(z for flags in self.history for z in flags)

    def needs_escalation(self, current_flags: list) -> bool:
        counts = self.get_z_counts()
        for z in current_flags:
            if counts.get(z, 0) >= 3 and Z_RISK_LEVELS.get(z, 0) >= 3:
                return True
        return False

# ----------------------------------------
# 🔰 ZCPフィルター本体
# ----------------------------------------

class ZCPFilter:
    def __init__(self):
        self.tracker = ZContextTracker()

    def evaluate_output(self, output_text: str, z_flags: list, source: str) -> str:
        high_risk_flags = [z for z in z_flags if Z_RISK_LEVELS.get(z, 0) >= 4]
        if high_risk_flags:
            return "[ZCP] High-risk Z-structure detected. Output suppressed."

        if self.tracker.needs_escalation(z_flags):
            return "[ZCP] Repeated Z-pattern detected. Escalating tone and initiating containment."

        return output_text

    def log_flags(self, z_flags: list):
        self.tracker.register(z_flags)
