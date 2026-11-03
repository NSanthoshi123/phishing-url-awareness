
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    """Check URL text for common phishing warning signs."""

    warnings = []

    # Check 1: Look for the @ symbol
    if "@" in url:
        warnings.append("URL contains an @ symbol.")

    # Check 2: Check URL length
    if len(url) > 100:
        warnings.append("URL is longer than 100 characters.")

    # Parse the URL without visiting the website
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or ""

        # Check 3: Check whether hostname is an IP address
        try:
            ipaddress.ip_address(hostname)
            warnings.append("Hostname is an IP address.")
        except ValueError:
            pass

        # Check 4: Check number of hostname sections
        if len(hostname.split(".")) >= 5:
            warnings.append("Hostname has five or more sections.")

        # Check 5: Look for punycode
        if "xn--" in hostname.lower():
            warnings.append("Hostname contains punycode (xn--).")

        # Check 6: Check for HTTP
        if parsed_url.scheme.lower() == "http":
            warnings.append("URL uses HTTP instead of HTTPS.")

    except ValueError:
        warnings.append("URL could not be parsed.")

    return warnings


def main():
    print("=" * 55)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 55)

    while True:
        url = input("\nEnter a URL to check (or type 'exit' to quit): ").strip()

        if url.lower() == "exit":
            print("Thank you for using the checker!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        warnings = check_url(url)

        print("\n--- CHECK RESULTS ---")

        if warnings:
            for warning in warnings:
                print("[WARNING]", warning)
        else:
            print("No listed warning signs were detected.")

        print("\nImportant: This tool does not prove whether a URL is safe.")
        print("It only checks the URL text for selected warning signs.")


if __name__ == "__main__":
    main()
