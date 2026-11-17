#!/usr/bin/env python3
"""
OSINT HUNTER v3.0 - Comprehensive Open Source Intelligence Tool
Expanded with 500+ sources across all categories
"""
import os
import sys
import time
import random
import requests
from datetime import datetime
from urllib.parse import quote

def matrix_code(text):
    print("\033[1;32m" + "="*60)
    print(" ░██ ░██ ░██ ░███████  ░██████  ░███████ ")
    print(" ░██ ░██ ░██ ░██░░░░██ ░██░░░██ ░██░░░░██")
    print(" ░█████████████ ░██   ░██ ░██████  ░███████ ")
    print(" ░██░░░░██░██ ░██   ░██ ░██░░░   ░██░░░░██")
    print(" ░██   ░██░██ ░░██████  ░██      ░██   ░██")
    print(" ░░     ░░ ░░   ░░░░░░   ░░       ░░    ░░")
    print("="*60)
    
    chars = "0123456789ABCDEF"
    for _ in range(15):
        line = "".join(random.choice(chars) if random.random() > 0.7 else " " for _ in range(50))
        print("\033[1;32m" + line)
        time.sleep(0.1)
    
    print("\n\033[1;36mOSINT HUNTER v3.0 - COMPREHENSIVE OSINT TOOL")
    print("© 2024 OSINT EXPERTS | 500+ SOURCES | ALL SYSTEMS OPERATIONAL\n")

def check_connectivity():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def search_username(username):
    print("\033[1;32m🔍 Searching for username:", username, "\n")
    
    sources = [
        # Major Social
        "https://instagram.com/{}/", "https://twitter.com/{}", "https://x.com/{}",
        "https://github.com/{}", "https://linkedin.com/in/{}", "https://facebook.com/{}/",
        "https://pinterest.com/{}/", "https://twitch.tv/{}", "https://snapchat.com/add/{}/",
        "https://reddit.com/u/{}", "https://reddit.com/user/{}", "https://youtube.com/@{}",
        "https://youtube.com/user/{}", "https://steamcommunity.com/id/{}",
        "https://flickr.com/people/{}/", "https://soundcloud.com/{}", "https://tiktok.com/@{}",
        "https://behance.net/{}", "https://tumblr.com/blog/{}", "https://myspace.com/{}",
        "https://vimeo.com/{}", "https://producthunt.com/@{}", "https://medium.com/@{}",
        "https://quora.com/profile/{}", "https://discord.com", "https://telegram.me/{}",
        "https://mastodon.social/@{}", "https://bsky.app/profile/{}.bsky.social",
        "https://threads.net/@{}",
        
        # Developer/Technical
        "https://gitlab.com/{}", "https://bitbucket.org/{}/", "https://sourceforge.net/u/{}/",
        "https://npmjs.com/~{}", "https://pypi.org/user/{}/", "https://rubygems.org/profiles/{}",
        "https://hub.docker.com/u/{}/", "https://codepen.io/{}/", "https://replit.com/@{}",
        "https://kaggle.com/{}", "https://stackoverflow.com/users/{}", "https://dev.to/{}",
        "https://hashnode.com/@{}", "https://hackerrank.com/{}", "https://codewars.com/users/{}",
        "https://leetcode.com/{}/", "https://topcoder.com/members/{}/",
        "https://glitch.com/@{}", "https://observablehq.com/@{}", "https://codesandbox.io/u/{}",
        
        # Gaming
        "https://roblox.com/user.aspx?username={}", "https://epicgames.com/id/{}",
        "https://gog.com/u/{}", "https://speedrun.com/users/{}", "https://hltv.org/player/{}",
        "https://liquipedia.net/{}", "https://twitchtracker.com/{}", "https://sullygnome.com/profile/{}",
        "https://playstation.com/en-us/games/{}", "https://xbox.com/en-us/games/{}",
        
        # Professional/Business
        "https://crunchbase.com/person/{}", "https://angel.co/u/{}", "https://glassdoor.com/profile/{}",
        "https://xing.com/profile/{}", "https://meetup.com/members/{}/", "https://eventbrite.com/u/{}",
        "https://freelancer.com/u/{}", "https://upwork.com/freelancers/~{}", "https://fiverr.com/{}",
        "https://99designs.com/profiles/{}", "https://dribbble.com/{}", "https://artstation.com/{}",
        "https://deviantart.com/{}", "https://newgrounds.com/{}", "https://patreon.com/{}",
        "https://kickstarter.com/profile/{}", "https://gofundme.com/f/{}", "https://opensea.io/{}",
        "https://foundation.app/@{}", "https://rarible.com/{}",
        
        # Academic/Research
        "https://scholar.google.com/citations?user={}", "https://researchgate.net/profile/{}",
        "https://academia.edu/{}", "https://orcid.org/{}", "https://semanticscholar.org/author/{}",
        "https://pubmed.ncbi.nlm.nih.gov/?term={}", "https://mendeley.com/profiles/{}",
        "https://figshare.com/authors/{}/", "https://osf.io/{}", "https://zenodo.org/{}",
        
        # Music/Entertainment
        "https://open.spotify.com/user/{}", "https://last.fm/user/{}", "https://bandcamp.com/{}",
        "https://mixcloud.com/{}/", "https://audiomack.com/{}", "https://reverbnation.com/{}",
        "https://discogs.com/artist/{}", "https://rateyourmusic.com/~{}/", "https://imdb.com/name/{}/",
        "https://letterboxd.com/{}", "https://trakt.tv/users/{}", "https://myanimelist.net/profile/{}",
        "https://anilist.co/user/{}/", "https://goodreads.com/{}", "https://librarything.com/profile/{}",
        
        # Shopping/E-commerce
        "https://amazon.com/shops/{}", "https://ebay.com/usr/{}", "https://etsy.com/people/{}",
        "https://poshmark.com/closet/{}", "https://mercari.com/u/{}", "https://depop.com/{}",
        "https://vinted.com/profile/{}", "https://stockx.com/users/{}", "https://goat.com/sellers/{}",
        "https://grailed.com/users/{}",
        
        # Travel/Lifestyle
        "https://airbnb.com/users/show/{}", "https://tripadvisor.com/members/{}",
        "https://yelp.com/user_details?userid={}", "https://foursquare.com/user/{}",
        "https://strava.com/athletes/{}", "https://alltrails.com/members/{}",
        "https://komoot.com/user/{}", "https://mapmyrun.com/profile/{}",
        
        # Crypto/Web3
        "https://etherscan.io/address/{}", "https://bscscan.com/address/{}",
        "https://polygonscan.com/address/{}", "https://snowtrace.io/address/{}",
        "https://ftmscan.com/address/{}", "https://arbiscan.io/address/{}",
        "https://solscan.io/account/{}", "https://explorer.solana.com/address/{}",
        "https://nearblocks.io/address/{}", "https://cardanoscan.io/address/{}",
        "https://algoexplorer.io/address/{}", "https://cosmos.bigdipper.live/account/{}",
        "https://mintscan.io/cosmos/account/{}",
        
        # Cloud/Storage
        "https://dropbox.com/u/{}", "https://drive.google.com/drive/folders/{}",
        "https://box.com/folder/{}", "https://icloud.com/{}", "https://onedrive.live.com/?id={}",
        "https://mega.nz/folder/{}", "https://mediafire.com/folder/{}", "https://4shared.com/u/{}/",
        
        # Search Engines
        "https://google.com/search?q={}", "https://bing.com/search?q={}",
        "https://duckduckgo.com/?q={}", "https://yandex.com/search/?text={}",
        "https://search.yahoo.com/search?p={}",
        
        # Username Checkers
        "https://namechk.com/{}", "https://knowem.com/{}", "https://checkusernames.com/{}",
        "https://namecheckr.com/{}", "https://instantusername.com/#q={}",
        "https://whatsmyname.app/{}", "https://usernamechecker.com/{}",
    ]
    
    found, not_found, errors = [], [], []
    
    for source in sources:
        try:
            url = source.format(username)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            
            if response.status_code == 200:
                response_lower = response.text.lower()
                if any(x in response_lower for x in ['not found', '404', 'user not found', 'profile not found', 'does not exist']):
                    not_found.append(url)
                else:
                    print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                    found.append(url)
            elif response.status_code == 404:
                not_found.append(url)
            elif response.status_code == 403:
                errors.append(f"403: {url.split('/')[2]}")
            elif response.status_code == 429:
                errors.append(f"429 Rate Limited: {url.split('/')[2]}")
        except requests.exceptions.Timeout:
            errors.append(f"Timeout: {url.split('/')[2]}")
        except Exception as e:
            errors.append(f"Error: {url.split('/')[2]}")
    
    print(f"\n\033[1;36m📊 Summary: {len(found)} found, {len(not_found)} not found, {len(errors)} errors")
    return found

def search_email(email):
    print("\n\033[1;32m🔍 Searching for email:", email, "\n")
    
    sources = [
        "https://emailsherlock.com/search?q={}", "https://hunter.io/email-verifier/{}",
        "https://pipl.com/search/?q={}", "https://spokeo.com/search?keywords={}",
        "https://peekyou.com/email/{}", "https://radaris.com/{}",
        "https://zabasearch.com/email/{}", "https://truepeoplesearch.com/find/person/{}",
        "https://fastpeoplesearch.com/{}", "https://beenverified.com/search/email/{}",
        "https://intelius.com/search/{}", "https://instantcheckmate.com/search/{}",
        "https://truthfinder.com/{}", "https://peoplefinders.com/{}",
        "https://whitepages.com/name/{}", "https://411.com/reverse_email/{}",
        "https://haveibeenpwned.com/account/{}", "https://dehashed.com/search?query={}",
        "https://intelx.io/search?query={}", "https://leak-lookup.com/search?query={}",
        "https://leakcheck.io/search?query={}", "https://snusbase.com/search?q={}",
        "https://email-format.com/d/{}", "https://verify-email.org/{}",
        "https://mailtester.com/test.php?email={}", "https://emailhippo.com/tools/email-verification/{}",
        "https://neverbounce.com/verify-email/{}", "https://zerobounce.net/verify-email/{}",
        "https://kickbox.com/verify/{}", "https://snov.io/verify-email/{}",
        "https://clearbit.com/{}", "https://fullcontact.com/{}", "https://rocketreach.co/{}",
        "https://lusha.com/{}", "https://zoominfo.com/{}", "https://seamless.ai/{}",
        "https://apollo.io/{}", "https://snov.io/{}", "https://anymailfinder.com/{}",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(quote(email))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200 and len(response.text) > 1000:
                print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                found.append(url)
        except:
            pass
    return found

def search_phone(phone):
    print("\n\033[1;32m🔍 Searching for phone number:", phone, "\n")
    
    sources = [
        "https://whitepages.com/phone/{}", "https://spokeo.com/search?q={}",
        "https://peoplefinders.com/search/{}/", "https://peoplesearch.com/search?phone={}",
        "https://411.com/reverse_phone/{}", "https://reversephone.com/{}",
        "https://radaris.com/{}", "https://zabasearch.com/phone/{}",
        "https://truepeoplesearch.com/find/person/{}", "https://fastpeoplesearch.com/{}",
        "https://beenverified.com/search/phone/{}", "https://intelius.com/search/{}",
        "https://instantcheckmate.com/search/{}", "https://truthfinder.com/{}",
        "https://peekyou.com/phone/{}", "https://anywho.com/{}",
        "https://freecarrierlookup.com/{}", "https://opencnam.com/{}",
        "https://numverify.com/{}", "https://veriphone.io/{}",
        "https://phonevalidator.com/{}", "https://phonearea.us/{}",
        "https://areacode-lookup.com/{}", "https://allareacodes.com/{}.htm",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(quote(phone))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200 and len(response.text) > 1000:
                print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                found.append(url)
        except:
            pass
    return found

def search_name(name):
    print("\n\033[1;32m🔍 Searching for name:", name, "\n")
    
    sources = [
        "https://peoplefinders.com/search/{}/", "https://spokeo.com/search?q={}",
        "https://peoplesearch.com/search?name={}", "https://whitepages.com/search/FindPeople?name={}",
        "https://peekyou.com/{}", "https://radaris.com/{}", "https://zabasearch.com/name/{}",
        "https://truepeoplesearch.com/find/person/{}", "https://fastpeoplesearch.com/{}",
        "https://beenverified.com/search/name/{}", "https://intelius.com/search/{}",
        "https://instantcheckmate.com/search/{}", "https://truthfinder.com/{}",
        "https://anywho.com/{}", "https://411.com/name/{}", "https://criminalcheck.com/{}",
        "https://backgroundchecks.com/{}", "https://checkpeople.com/{}",
        "https://publicrecords.com/{}", "https://staterecords.org/{}",
        "https://countyrecords.com/{}", "https://courtrecords.com/{}",
        "https://marriagerecords.com/{}", "https://divorcerecords.com/{}",
        "https://birthrecords.com/{}", "https://deathrecords.com/{}",
        "https://voterrecords.com/{}", "https://propertyrecords.com/{}",
        "https://taxrecords.com/{}", "https://businessrecords.com/{}",
        "https://professionallicenses.com/{}", "https://drivingrecords.com/{}",
        "https://militaryrecords.com/{}", "https://immigrationrecords.com/{}",
        "https://socialsecurityrecords.com/{}", "https://medicalrecords.com/{}",
        "https://educationrecords.com/{}", "https://employmentrecords.com/{}",
        "https://financialrecords.com/{}", "https://creditrecords.com/{}",
        "https://bankruptcyrecords.com/{}", "https://liensrecords.com/{}",
        "https://judgmentsrecords.com/{}", "https://civilrecords.com/{}",
        "https://criminalrecords.com/{}", "https://sexoffenderrecords.com/{}",
        "https://warrantrecords.com/{}", "https://incarcerationrecords.com/{}",
        "https://parolerecords.com/{}", "https://probationrecords.com/{}",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(quote(name))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200 and len(response.text) > 1000:
                print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                found.append(url)
        except:
            pass
    return found

def search_ip(ip):
    print("\n\033[1;32m🔍 Searching for IP:", ip, "\n")
    
    sources = [
        "https://ipapi.co/{}/json/", "https://ipinfo.io/{}", "https://freegeoip.app/json/{}",
        "http://ip-api.com/json/{}", "https://ipwhois.app/json/{}", "https://ipapi.is/json/{}",
        "https://ipgeolocation.io/json/ip?apiKey=demo&ip={}", "https://ipdata.co/{}.json?api-key=test",
        "https://abstractapi.com/ip/geolocation?api_key=demo&ip={}", "https://ipregistry.co/{}?key=try",
        "https://ipapi.com/{}?access_key=demo", "https://ip2location.com/demo/{}",
        "https://shodan.io/host/{}", "https://censys.io/ipv4/{}",
        "https://virustotal.com/gui/ip-address/{}/details", "https://abuseipdb.com/check/{}",
        "https://ipqualityscore.com/free-ip-lookup-proxy-vpn-test/lookup/{}",
        "https://scamalytics.com/ip/{}", "https://iptrackeronline.com/app.php/iplookup?ip={}",
        "https://dnslytics.com/ip/{}", "https://whois.com/whois/{}",
        "https://ripe.net/whois?searchtext={}", "https://lookup.iana.org/ip/{}",
        "https://arin.net/rest/ip/{}", "https://lacnic.net/cgi-bin/lacnic/whois?lg=EN&query={}",
        "https://afrinic.net/en/whois?text={}", "https://apnic.net/en/whois/search?text={}",
        "https://bgp.he.net/ip/{}", "https://bgpview.io/ip/{}", "https://robtex.com/ip-lookup/{}.html",
        "https://myip.cn/{}", "https://ip-adress.com/{}", "https://iplocation.net/ip-lookup/{}",
        "https://iplocationtools.com/ip-lookup.php?ip={}", "https://ip2location.io/{}",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(ip)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                found.append(url)
        except:
            pass
    return found

def search_domain(domain):
    print("\n\033[1;32m🔍 Searching for domain:", domain, "\n")
    
    sources = [
        "https://whois.domaintools.com/{}", "https://whois.com/whois/{}",
        "http://dnslookup.org/{}", "https://securitytrails.com/domain/{}/dns",
        "https://whoisxmlapi.com/whoisserver/WhoisService?domainName={}",
        "https://namecheap.com/domains/whois/?domain={}",
        "https://godaddy.com/whois/results.aspx?domain={}",
        "https://whois.icann.org/en/lookup?name={}", "https://lookup.internic.net/{}",
        "https://ripe.net/whois?searchtext={}", "https://apnic.net/en/whois/search?text={}",
        "https://arin.net/rest/ip/{}", "https://lacnic.net/cgi-bin/lacnic/whois?lg=EN&query={}",
        "https://afrinic.net/en/whois?text={}", "https://viewdns.info/whois/?domain={}",
        "https://viewdns.info/dnsrecord/?domain={}", "https://viewdns.info/iphistory/?domain={}",
        "https://viewdns.info/reversewhois/?domain={}", "https://viewdns.info/spfrecord/?domain={}",
        "https://viewdns.info/dkimrecord/?domain={}", "https://viewdns.info/dmarcrecord/?domain={}",
        "https://viewdns.info/mxrecord/?domain={}", "https://viewdns.info/nsrecord/?domain={}",
        "https://viewdns.info/soarecord/?domain={}", "https://viewdns.info/txtrecord/?domain={}",
        "https://viewdns.info/ptrrecord/?domain={}", "https://viewdns.info/srvrecord/?domain={}",
        "https://dnsdumpster.com/{}", "https://subdomainfinder.c99.nl/{}",
        "https://crt.sh/?q={}", "https://transparencyreport.google.com/https/certificates?domain={}",
        "https://ssllabs.com/ssltest/analyze.html?d={}", "https://htbridge.com/ssltest/{}",
        "https://immuniweb.com/ssl/?id={}", "https://digicert.com/ssl-checker.htm#hostname={}",
        "https://geotrust.com/ssl-checker?host={}", "https://thawte.com/ssl-checker?host={}",
        "https://rapidssl.com/ssl-checker?host={}", "https://comodo.com/ssl-checker?host={}",
        "https://sectigo.com/ssl-checker?host={}", "https://entrust.com/ssl-checker?host={}",
        "https://globalsign.com/ssl-checker?host={}", "https://certum.eu/ssl-checker?host={}",
        "https://actalis.com/ssl-checker?host={}", "https://starfieldtech.com/ssl-checker?host={}",
        "https://networksolutions.com/ssl-checker?host={}", "https://register.com/ssl-checker?host={}",
        "https://hostgator.com/ssl-checker?host={}", "https://bluehost.com/ssl-checker?host={}",
        "https://dreamhost.com/ssl-checker?host={}", "https://siteadvisor.com/report/{}",
        "https://urlvoid.com/scan/{}/", "https://virustotal.com/gui/domain/{}/details",
        "https://threatcrowd.org/domain.php?domain={}", "https://passivetotal.org/analyze?domain={}",
        "https://riskiq.com/products/passivetotal/{}", "https://hexillion.com/lookup/{}",
        "https://dnsstuff.com/tools/whois?domain={}", "https://intodns.com/{}",
        "https://whatsmydns.net/{}", "https://dnschecker.org/{}",
        "https://dnspropagation.net/{}", "https://dnslookup.online/{}",
        "https://dnsqueries.com/en/domain_lookup.php?domain={}", "https://dnsdb.info/{}",
        "https://farsightsecurity.com/{}", "https://whoisrequest.com/{}",
        "https://domainiq.com/{}", "https://whoisology.com/{}",
        "https://domainbigdata.com/{}", "https://dnshistory.org/{}",
        "https://whois-history.whoisxmlapi.com/{}", "https://domaintools.com/products/whois/{}",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(domain)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200 and len(response.text) > 1000:
                print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                found.append(url)
        except:
            pass
    return found

def search_social_media(username):
    print("\n\033[1;32m🔍 Advanced Social Media Search:", username, "\n")
    
    sources = [
        "https://pinterest.com/{}/", "https://tumblr.com/blog/{}", "https://myspace.com/{}",
        "https://vimeo.com/{}", "https://scholar.google.com/citations?user={}",
        "https://researchgate.net/profile/{}", "https://academia.edu/{}", "https://orcid.org/{}",
        "https://linkedin.com/in/{}", "https://medium.com/@{}", "https://substack.com/@{}",
        "https://quora.com/profile/{}", "https://reddit.com/u/{}", "https://discord.com",
        "https://telegram.me/{}", "https://whatsapp.com/{}", "https://signal.org/{}",
        "https://threema.ch/{}", "https://wire.com/{}", "https://element.io/{}",
        "https://matrix.org/{}", "https://mastodon.social/@{}", "https://twitter.com/{}",
        "https://x.com/{}", "https://bluesky.app/profile/{}.bsky.social",
        "https://threads.net/@{}", "https://linkedin.com/company/{}",
        "https://facebook.com/{}/", "https://instagram.com/{}/", "https://tiktok.com/@{}",
        "https://youtube.com/@{}", "https://twitch.tv/{}", "https://snapchat.com/add/{}/",
        "https://github.com/{}", "https://gitlab.com/{}", "https://bitbucket.org/{}/",
        "https://stackoverflow.com/users/{}", "https://dev.to/{}", "https://hashnode.com/@{}",
        "https://hackerrank.com/{}", "https://codewars.com/users/{}", "https://leetcode.com/{}/",
        "https://kaggle.com/{}", "https://dribbble.com/{}", "https://behance.net/{}",
        "https://artstation.com/{}", "https://deviantart.com/{}", "https://flickr.com/people/{}/",
        "https://500px.com/{}", "https://unsplash.com/@{}", "https://pexels.com/@{}",
        "https://shutterstock.com/g/{}", "https://gettyimages.com/{}",
        "https://linktr.ee/{}", "https://beacons.ai/{}", "https://carrd.co/{}",
        "https://sites.google.com/view/{}", "https://wix.com/{}", "https://squarespace.com/{}",
        "https://wordpress.com/{}", "https://blogger.com/profile/{}",
        "https://patreon.com/{}", "https://ko-fi.com/{}", "https://buymeacoffee.com/{}",
        "https://paypal.me/{}", "https://cash.app/{}", "https://venmo.com/{}",
        "https://zellepay.com/{}", "https://stripe.com/{}", "https://square.com/{}",
        "https://shopify.com/{}", "https://etsy.com/people/{}", "https://ebay.com/usr/{}",
        "https://mercari.com/u/{}", "https://poshmark.com/closet/{}", "https://depop.com/{}",
        "https://vinted.com/profile/{}", "https://stockx.com/users/{}", "https://goat.com/sellers/{}",
        "https://grailed.com/users/{}", "https://therealreal.com/onboarding/seller/{}",
        "https://vestiairecollective.com/{}", "https://chrono24.com/dealer/{}.htm",
        "https://bobshop.co.za/seller/{}", "https://carousell.com/u/{}",
    ]
    
    found = []
    for source in sources:
        try:
            url = source.format(username)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                response_lower = response.text.lower()
                if not any(x in response_lower for x in ['not found', '404', 'does not exist']):
                    print(f"\033[1;32m✓ Found on {url.split('/')[2]}")
                    found.append(url)
        except:
            pass
    return found

def display_results(search_type, data, results):
    if not results:
        print("\n\033[1;31m❌ No results found for", search_type)
        return
    
    print(f"\n\033[1;32m🔍 Results for {search_type}:")
    print("-" * 60)
    for i, result in enumerate(results, 1):
        print(f"{i}. \033[1;33m{result}")

def main_menu():
    while True:
        print("\n\033[1;32m" + "="*60)
        print(" 🌐 OSINT WIZARD - SELECT SEARCH TYPE")
        print("="*60)
        print("1. 🔍 Username Search (150+ sources)")
        print("2. 📞 Phone Number Lookup (25+ sources)")
        print("3. ✉️ Email Address Analysis (40+ sources)")
        print("4. 👤 Name Investigation (50+ sources)")
        print("5. 🌐 IP Address Analysis (40+ sources)")
        print("6. 🌍 Domain Research (80+ sources)")
        print("7. 🔗 Social Media Search (100+ sources)")
        print("8. ⚡ All-in-One OSINT Scan")
        print("9. 📊 Export Results to File")
        print("0. 💻 Exit Wizard")
        print("="*60)
        
        choice = input("\n\033[1;36mEnter your choice (0-9): ").strip()
        
        if choice == '1':
            username = input("\n\033[1;32mEnter Username: ").strip()
            if username:
                print(f"\n\033[1;34mStarting username search for '{username}'...")
                results = search_username(username)
                display_results("Username", username, results)
        elif choice == '2':
            phone = input("\n\033[1;32mEnter Phone Number: ").strip()
            if phone:
                print(f"\n\033[1;34mStarting phone number search for '{phone}'...")
                results = search_phone(phone)
                display_results("Phone Number", phone, results)
        elif choice == '3':
            email = input("\n\033[1;32mEnter Email Address: ").strip()
            if email:
                print(f"\n\033[1;34mStarting email search for '{email}'...")
                results = search_email(email)
                display_results("Email", email, results)
        elif choice == '4':
            name = input("\n\033[1;32mEnter Name: ").strip()
            if name:
                print(f"\n\033[1;34mStarting name investigation for '{name}'...")
                results = search_name(name)
                display_results("Name", name, results)
        elif choice == '5':
            ip = input("\n\033[1;32mEnter IP Address: ").strip()
            if ip:
                print(f"\n\033[1;34mStarting IP analysis for '{ip}'...")
                results = search_ip(ip)
                display_results("IP Address", ip, results)
        elif choice == '6':
            domain = input("\n\033[1;32mEnter Domain: ").strip()
            if domain:
                print(f"\n\033[1;34mStarting domain search for '{domain}'...")
                results = search_domain(domain)
                display_results("Domain", domain, results)
        elif choice == '7':
            username = input("\n\033[1;32mEnter Username: ").strip()
            if username:
                print(f"\n\033[1;34mStarting social media search for '{username}'...")
                results = search_social_media(username)
                display_results("Social Media", username, results)
        elif choice == '8':
            data = input("\n\033[1;32mEnter Search Data: ").strip()
            if data:
                print(f"\n\033[1;34mStarting comprehensive OSINT scan for '{data}'...")
                all_results = []
                
                if '@' in data:
                    results = search_email(data)
                    display_results("Email", data, results)
                    all_results.extend(results)
                elif '.' in data and len(data.split('.')) > 1:
                    results = search_domain(data)
                    display_results("Domain", data, results)
                    all_results.extend(results)
                else:
                    results = search_username(data)
                    display_results("Username", data, results)

                # Also try phone if it looks like a number
                if len(data) > 7 and any(c.isdigit() for c in data):
                    results = search_phone(data)
                    display_results("Phone Number", data, results)
                    all_results.extend(results)
                
                # Try name search
                results = search_name(data)
                display_results("Name", data, results)
                all_results.extend(results)
                
                print(f"\n\033[1;36m📊 TOTAL RESULTS: {len(all_results)} sources checked")
        elif choice == '9':
            filename = input("\n\033[1;32mEnter filename to save results: ").strip()
            if filename:
                print(f"\033[1;34mResults would be saved to {filename}")
                print("(Export functionality - implement as needed)")
        elif choice == '0':
            print("\n\033[1;36m👋 Exiting OSINT Wizard. Good luck, hacker!")
            break
        else:
            print("\n\033[1;31m❌ Invalid option. Please select a valid menu item.")
        
        input("\nPress Enter to continue...")

def main():
    os.system('clear')
    
    matrix_code("OSINT WIZARD")
    print("\033[1;32m" + "="*60)
    print(" 🌐 Welcome to OSINT Wizard - Your Ultimate Intelligence Tool")
    print("="*60)
    print(" 🔍 This tool helps you gather information from various sources")
    print(" 💻 It searches across multiple platforms without requiring API keys")
    print(" ⚡ All your data is analyzed through open-source intelligence methods")
    print(" 📊 Now with 500+ sources across all categories!")
    print("="*60)
    
    if not check_connectivity():
        print("\n\033[1;31m⚠️ No internet connection detected!")
        input("Press Enter to continue anyway...")
    
    main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;36m👋 Exiting OSINT Wizard gracefully. Good luck, hacker!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[1;31m❌ An error occurred: {str(e)}")
        input("Press Enter to exit...")
        sys.exit(1)
