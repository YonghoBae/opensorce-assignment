#백준 문제 크롤링
import requests
from bs4 import BeautifulSoup

num = '15652'
base = 'https://www.acmicpc.net/problem/'
url = base + num

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    problem_description = soup.select('#problem_description > p')
    problem_ul = soup.select('#problem_description > ul')
    input_description = soup.select('#problem_input > p')
    output_description = soup.select('#problem_output > p')
    sample_input = soup.select_one('#sampleinput1').text.strip()
    sample_output = soup.select_one('#sampleoutput1').text.strip()
    sample_i = soup.select("pre[id^=sample-input]")
    sample_o = soup.select("pre[id^=sample-output]")

    print("#####   Problem", num, "  ######")
    for i in problem_description:
        print(i.text.strip(), end = '\n\n')
    for i in problem_ul:
        print(i.text.strip(), end = '\n\n')
    print("IN")
    for i in input_description:
        print(i.text.strip(), end = '\n\n')
    print("OUT")
    for i in output_description:
        print(i.text.strip(), end = '\n\n')
    print("EXAMPLE")
    for i in range(len(sample_i)):
        print("### IN", i+1, '###')
        print(sample_i[i].text.strip(), end='\n\n')
        print("### OUT", i+1, '###')
        print(sample_o[i].text.strip(), end='\n\n')
else:
    print(response.status_code)
