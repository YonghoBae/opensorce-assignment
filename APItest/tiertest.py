import requests
import random

def fetch_random_problem(level=7, max_attempts=10):
    url = "https://solved.ac/api/v3/search/problem"
    headers = {
        "x-solvedac-language": "",
        "Accept": "application/json"
    }

    for attempt in range(max_attempts):
        random_page = random.randint(1, 350)
        querystring = {"query": "", "page": random_page, "direction": "desc", "sort": "solved"}

        # API 요청 보내기
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])

            # 모든 문제의 티어를 출력하여 확인
            print(f"Attempt {attempt + 1}: Found problems on page {random_page}:")
            for item in items:
                print(f"ID={item['problemId']}, Title={item.get('titleKo', 'No Title')}, Level={item['level']}")

            # 레벨이 해당 레벨인 모든 문제를 수집
            level_items = [item for item in items if item['level'] == level]

            if level_items:
                # 해당 레벨의 문제 중에서 랜덤으로 하나를 선택
                selected_item = random.choice(level_items)
                print(f"Selected Problem: ID={selected_item['problemId']}, Title={selected_item.get('titleKo', 'No Title')}, Level={selected_item['level']}")
                return
            else:
                print(f"No Tier {level} Problem found on page {random_page}. Trying again...")
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response content: {response.content}")

    print(f"Failed to find a Tier {level} Problem after {max_attempts} attempts.")

if __name__ == "__main__":
    # 특정 티어를 지정하여 테스트
    fetch_random_problem(level=7)
