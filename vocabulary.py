# import pandas as pd

# df = pd.read_excel('vocabulary.xlsx')  # file Excel
# records = df.to_dict(orient='records')

# import json
# with open('vocabulary.json', 'w', encoding='utf-8') as f:
#     json.dump(records, f, ensure_ascii=False, indent=2)


import json

# Tên file JSON
users_file = 'users.json'
topic_file = 'topic.json'
vocab_file = 'vocabulary.json'
quiz_file = 'quiz.json'
quiz_questions_file = 'quiz_questions.json'



output_file = 'all.json'

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Đọc dữ liệu từng file
users_data = read_json(users_file)
topic_data = read_json(topic_file)
vocab_data = read_json(vocab_file)
quiz_data = read_json(quiz_file)
quiz_questions_data = read_json(quiz_questions_file)
# Tạo dict gộp
merged_data = {
    "users": users_data,
    "topic": topic_data,
    "vocabulary": vocab_data,
    "quiz": quiz_data,
    "quiz_questions": quiz_questions_data
}

# Ghi ra file mới
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print(f"Đã gộp 5 file JSON thành công vào {output_file}")
