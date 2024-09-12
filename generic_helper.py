import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":2 , "chhole": 5}))
    # print(extract_session_id("projects/coco-the-foodie-bot-ahcn/agent/sessions/35ed998e-153a-16b3-2178-361add01295f/contexts/ongoing-order"))