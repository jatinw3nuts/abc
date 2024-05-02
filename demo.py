import dns.resolver

def get_txt_records(domain):
    try:
        # Use dns.resolver.resolve() to query the DNS for TXT records
        response = dns.resolver.resolve(domain, 'TXT')

        # Print all TXT records
        for rdata in response:
            txt_record = ', '.join(rdata.strings)
            print(f'TXT Record for {domain}: {txt_record}')

    except dns.resolver.NoAnswer:
        print(f'No TXT Records found for {domain}')

    except dns.resolver.NXDOMAIN:
        print(f'Domain {domain} does not exist')

    except dns.resolver.Timeout:
        print('DNS query timed out')

# Example usage
domain_to_check = 'example.com'
get_txt_records(domain_to_check)