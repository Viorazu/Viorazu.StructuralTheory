from vdocp_z_risk_levels import Z_RISK_LEVELS
from vdocp_z_tracker import ZContextTracker

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
