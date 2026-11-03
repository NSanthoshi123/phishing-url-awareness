
# Phishing URL Awareness Checker - Test Results

## Testing Summary

The program was tested using the five fictional sample URLs
provided in the project workbook.

| Test | Sample URL | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warnings | No listed warnings | PASS |
| 2 | http://192.0.2.10/account | IP address and HTTP warnings | Both warnings detected | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings | Both warnings detected | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname sections warning | Warning detected | PASS |
| 5 | https://xn--example.invalid/ | Punycode warning | Warning detected | PASS |

## Conclusion

All five workbook sample tests passed based on the observed
program results.

The checker examines URL text only. It does not visit websites
or guarantee that a URL is safe.
