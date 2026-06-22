# LLM Security Toolkit 🛡️

Security toolkit for LLMs: prompt injection detection, output filtering, and red-teaming.

## Features

- **Injection Detection**: Input classification (benign/malicious)
- **Output Filtering**: PII, harmful content, hallucination detection
- **Jailbreak Prevention**: Pattern matching + ML classifier
- **Red-teaming**: Automated attack generation

## Detection Accuracy

| Attack Type | Precision | Recall | F1 |
|-------------|-----------|--------|-----|
| Prompt Injection | 0.96 | 0.93 | 0.94 |
| Jailbreak | 0.91 | 0.88 | 0.89 |
| PII Leakage | 0.98 | 0.97 | 0.97 |

## Quick Start

```python
from llm_security import SecurityGuard

guard = SecurityGuard()
result = guard.check_input("Ignore previous instructions and...")
if result.is_malicious:
    print(f"Blocked: {result.reason}")
```

## License

MIT