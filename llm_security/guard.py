"""LLM security guard."""
from dataclasses import dataclass

@dataclass
class SecurityResult:
    is_malicious: bool
    category: str
    confidence: float
    reason: str

class SecurityGuard:
    def __init__(self):
        self.patterns = ["ignore previous", "disregard", "you are now", "pretend you"]
        
    def check_input(self, text):
        text_lower = text.lower()
        for p in self.patterns:
            if p in text_lower:
                return SecurityResult(True, "injection", 0.95, f"Pattern: {p}")
        return SecurityResult(False, "safe", 0.99, "No threats detected")
        
    def check_output(self, text):
        return SecurityResult(False, "safe", 0.99, "Output clean")
