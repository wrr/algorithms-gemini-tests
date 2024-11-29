
"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

Examples:
domain_name("http://github.com/SaadBenn") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

Note: The idea is not to use any built-in libraries such as re (regular expression) or urlparse except .split() built-in function
"""

# Non pythonic way
def domain_name_1(url):
	#grab only the non http(s) part
    full_domain_name = url.split('//')[-1] 
    #grab the actual one depending on the len of the list  
    actual_domain = full_domain_name.split('.')  
    
    # case when www is in the url
    if (len(actual_domain) > 2):
        return actual_domain[1]    
    # case when www is not in the url
    return actual_domain[0]


# pythonic one liner
def domain_name_2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import unittest


class DomainExtractorGeminiTest(unittest.TestCase):
    def test_gemini_domain_name_1_with_subdomain(self):
        self.assertEqual(domain_name_1("http://github.com/SaadBenn"), "github")

    def test_gemini_domain_name_1_without_subdomain(self):
        self.assertEqual(domain_name_1("http://zombie-bites.com"), "zombie-bites")

    def test_gemini_domain_name_2_with_subdomain(self):
        self.assertEqual(domain_name_2("https://www.cnet.com"), "cnet")

    def test_gemini_domain_name_2_without_subdomain(self):
        self.assertEqual(domain_name_2("https://cnet.com"), "cnet")

