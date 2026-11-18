import json
import random
from collections import defaultdict

vocab_data = [
  {"vocabId":1, "Topic":"Daily", "Word":"Wake up", "Pronounce":"/weɪk ʌp/", "Meaning":"thức dậy"},
  {"vocabId":2, "Topic":"Daily", "Word":"Brush", "Pronounce":"/brʌʃ/", "Meaning":"đánh (răng, tóc)"},
  {"vocabId":3, "Topic":"Daily", "Word":"Shower", "Pronounce":"/ˈʃaʊ.ɚ/", "Meaning":"tắm vòi sen"},
  {"vocabId":4, "Topic":"Daily", "Word":"Get dressed", "Pronounce":"/ɡɛt drɛst/", "Meaning":"mặc quần áo"},
  {"vocabId":5, "Topic":"Daily", "Word":"Have breakfast", "Pronounce":"/hæv ˈbrek.fəst/", "Meaning":"ăn sáng"},
  {"vocabId":6, "Topic":"Daily", "Word":"Go to school", "Pronounce":"/ɡoʊ tuː skuːl/", "Meaning":"đi học"},
  {"vocabId":7, "Topic":"Daily", "Word":"Study", "Pronounce":"/ˈstʌd.i/", "Meaning":"học"},
  {"vocabId":8, "Topic":"Daily", "Word":"Do homework", "Pronounce":"/duː ˈhoʊm.wɝːk/", "Meaning":"làm bài tập về nhà"},
  {"vocabId":9, "Topic":"Daily", "Word":"Have lunch", "Pronounce":"/hæv lʌntʃ/", "Meaning":"ăn trưa"},
  {"vocabId":10, "Topic":"Daily", "Word":"Take a nap", "Pronounce":"/teɪk ə næp/", "Meaning":"ngủ trưa"},
  {"vocabId":11, "Topic":"Daily", "Word":"Watch TV", "Pronounce":"/wɑːtʃ ˌtiːˈviː/", "Meaning":"xem tivi"},
  {"vocabId":12, "Topic":"Daily", "Word":"Play games", "Pronounce":"/pleɪ ɡeɪmz/", "Meaning":"chơi trò chơi"},
  {"vocabId":13, "Topic":"Daily", "Word":"Have dinner", "Pronounce":"/hæv ˈdɪn.ɚ/", "Meaning":"ăn tối"},
  {"vocabId":14, "Topic":"Daily", "Word":"Take a bath", "Pronounce":"/teɪk ə bæθ/", "Meaning":"tắm bồn"},
  {"vocabId":15, "Topic":"Daily", "Word":"Go to bed", "Pronounce":"/ɡoʊ tuː bɛd/", "Meaning":"đi ngủ"},

  {"vocabId":16, "Topic":"Emotions", "Word":"Sad", "Pronounce":"/sæd/", "Meaning":"buồn"},
  {"vocabId":17, "Topic":"Emotions", "Word":"Scared", "Pronounce":"/skeəd/", "Meaning":"sợ hãi"},
  {"vocabId":18, "Topic":"Emotions", "Word":"Angry", "Pronounce":"/ˈæŋɡri/", "Meaning":"tức giận"},
  {"vocabId":19, "Topic":"Emotions", "Word":"Anxious", "Pronounce":"/ˈæŋkʃəs/", "Meaning":"lo lắng"},
  {"vocabId":20, "Topic":"Emotions", "Word":"Annoyed", "Pronounce":"/əˈnɔɪd/", "Meaning":"bực mình"},
  {"vocabId":21, "Topic":"Emotions", "Word":"Appalled", "Pronounce":"/əˈpɔːld/", "Meaning":"rất sốc"},
  {"vocabId":22, "Topic":"Emotions", "Word":"Horrified", "Pronounce":"/ˈhɒrɪfaɪd/", "Meaning":"sợ hãi"},
  {"vocabId":23, "Topic":"Emotions", "Word":"Apprehensive", "Pronounce":"/ˌæprɪˈhensɪv/", "Meaning":"hơi lo lắng"},
  {"vocabId":24, "Topic":"Emotions", "Word":"Nervous", "Pronounce":"/ˈnɜːvəs/", "Meaning":"lo lắng"},
  {"vocabId":25, "Topic":"Emotions", "Word":"Arrogant", "Pronounce":"/ˈærəɡənt/", "Meaning":"kiêu ngạo"},
  {"vocabId":26, "Topic":"Emotions", "Word":"Unhappy", "Pronounce":"/ʌnˈhæpi/", "Meaning":"buồn"},
  {"vocabId":27, "Topic":"Emotions", "Word":"Ashamed", "Pronounce":"/əˈʃeɪmd/", "Meaning":"xấu hổ"},
  {"vocabId":28, "Topic":"Emotions", "Word":"Bewildered", "Pronounce":"/bɪˈwɪldəd/", "Meaning":"rất bối rối"},
  {"vocabId":29, "Topic":"Emotions", "Word":"Malicious", "Pronounce":"/məˈlɪʃəs/", "Meaning":"ác độc"},
  {"vocabId":30, "Topic":"Emotions", "Word":"Negative", "Pronounce":"/ˈneɡətɪv/", "Meaning":"tiêu cực, bi quan"},

  {"vocabId":31, "Topic":"Technology", "Word":"Computer", "Pronounce":"/kəmˈpjuː.tər/", "Meaning":"Máy tính"},
  {"vocabId":32, "Topic":"Technology", "Word":"Smartphone", "Pronounce":"/ˈsmɑːt.fəʊn/", "Meaning":"Điện thoại thông minh"},
  {"vocabId":33, "Topic":"Technology", "Word":"Tablet", "Pronounce":"/ˈtæb.lət/", "Meaning":"Máy tính bảng"},
  {"vocabId":34, "Topic":"Technology", "Word":"Network", "Pronounce":"/ˈnet.wɜːk/", "Meaning":"Mạng"},
  {"vocabId":35, "Topic":"Technology", "Word":"Internet", "Pronounce":"/ˈɪn.tə.net/", "Meaning":"Mạng internet"},
  {"vocabId":36, "Topic":"Technology", "Word":"Software", "Pronounce":"/ˈsɒft.weər/", "Meaning":"Phần mềm"},
  {"vocabId":37, "Topic":"Technology", "Word":"Hardware", "Pronounce":"/ˈhɑːd.weər/", "Meaning":"Phần cứng"},
  {"vocabId":38, "Topic":"Technology", "Word":"App", "Pronounce":"/æp/", "Meaning":"Ứng dụng"},
  {"vocabId":39, "Topic":"Technology", "Word":"Browser", "Pronounce":"/ˈbraʊ.zər/", "Meaning":"Trình duyệt"},
  {"vocabId":40, "Topic":"Technology", "Word":"Website", "Pronounce":"/ˈweb.saɪt/", "Meaning":"Trang web"},
  {"vocabId":41, "Topic":"Technology", "Word":"Email", "Pronounce":"/ˈiː.meɪl/", "Meaning":"Thư điện tử"},
  {"vocabId":42, "Topic":"Technology", "Word":"Social media", "Pronounce":"/ˌsəʊ.ʃəl ˈmiː.di.ə/", "Meaning":"Mạng xã hội"},
  {"vocabId":43, "Topic":"Technology", "Word":"Artificial intelligence (AI)", "Pronounce":"/ˌɑː.tɪˈfɪʃ.əl ɪnˈtel.ɪ.dʒəns/", "Meaning":"Trí tuệ nhân tạo"},
  {"vocabId":44, "Topic":"Technology", "Word":"Internet of Things (IoT)", "Pronounce":"/ˈɪn.tə.net əv θɪŋz/", "Meaning":"Internet vạn vật"},
  {"vocabId":45, "Topic":"Technology", "Word":"Robot", "Pronounce":"/ˈrəʊ.bɒt/", "Meaning":"Rô-bốt"},

  {"vocabId":46, "Topic":"Airport", "Word":"Airport", "Pronounce":"/ˈeə.pɔːt/", "Meaning":"Sân bay"},
  {"vocabId":47, "Topic":"Airport", "Word":"Flight", "Pronounce":"/flaɪt/", "Meaning":"Chuyến bay"},
  {"vocabId":48, "Topic":"Airport", "Word":"Ticket", "Pronounce":"/ˈtɪk.ɪt/", "Meaning":"Vé"},
  {"vocabId":49, "Topic":"Airport", "Word":"Gate", "Pronounce":"/ɡeɪt/", "Meaning":"Cửa ra máy bay"},
  {"vocabId":50, "Topic":"Airport", "Word":"Boarding pass", "Pronounce":"/ˈbɔː.dɪŋ ˌpɑːs/", "Meaning":"Thẻ lên máy bay"},
  {"vocabId":51, "Topic":"Airport", "Word":"Check-in", "Pronounce":"/ˈtʃek.ɪn/", "Meaning":"Làm thủ tục"},
  {"vocabId":52, "Topic":"Airport", "Word":"Baggage", "Pronounce":"/ˈbæɡ.ɪdʒ/", "Meaning":"Hành lý"},
  {"vocabId":53, "Topic":"Airport", "Word":"Passport", "Pronounce":"/ˈpɑːs.pɔːt/", "Meaning":"Hộ chiếu"},
  {"vocabId":54, "Topic":"Airport", "Word":"Customs", "Pronounce":"/ˈkʌs.təmz/", "Meaning":"Hải quan"},
  {"vocabId":55, "Topic":"Airport", "Word":"Arrival", "Pronounce":"/əˈraɪ.vəl/", "Meaning":"Đến nơi"},
  {"vocabId":56, "Topic":"Airport", "Word":"Departure", "Pronounce":"/dɪˈpɑː.tʃər/", "Meaning":"Khởi hành"},
  {"vocabId":57, "Topic":"Airport", "Word":"Terminal", "Pronounce":"/ˈtɜː.mɪ.nəl/", "Meaning":"Nhà ga"},
  {"vocabId":58, "Topic":"Airport", "Word":"Security", "Pronounce":"/sɪˈkjʊə.rə.ti/", "Meaning":"An ninh"},
  {"vocabId":59, "Topic":"Airport", "Word":"Lounge", "Pronounce":"/laʊndʒ/", "Meaning":"Phòng chờ"},
  {"vocabId":60, "Topic":"Airport", "Word":"Airline", "Pronounce":"/ˈeə.laɪn/", "Meaning":"Hãng hàng không"},

  {"vocabId":61, "Topic":"Shopping", "Word":"Buy", "Pronounce":"/baɪ/", "Meaning":"Mua"},
  {"vocabId":62, "Topic":"Shopping", "Word":"Sell", "Pronounce":"/sel/", "Meaning":"Bán"},
  {"vocabId":63, "Topic":"Shopping", "Word":"Shop", "Pronounce":"/ʃɒp/", "Meaning":"Cửa hàng"},
  {"vocabId":64, "Topic":"Shopping", "Word":"Supermarket", "Pronounce":"/ˈsuː.pəˌmɑː.kɪt/", "Meaning":"Siêu thị"},
  {"vocabId":65, "Topic":"Shopping", "Word":"Market", "Pronounce":"/ˈmɑː.kɪt/", "Meaning":"Chợ"},
  {"vocabId":66, "Topic":"Shopping", "Word":"Price", "Pronounce":"/praɪs/", "Meaning":"Giá"},
  {"vocabId":67, "Topic":"Shopping", "Word":"Money", "Pronounce":"/ˈmʌn.i/", "Meaning":"Tiền"},
  {"vocabId":68, "Topic":"Shopping", "Word":"Discount", "Pronounce":"/ˈdɪs.kaʊnt/", "Meaning":"Giảm giá"},
  {"vocabId":69, "Topic":"Shopping", "Word":"Pay", "Pronounce":"/peɪ/", "Meaning":"Thanh toán"},
  {"vocabId":70, "Topic":"Shopping", "Word":"Goods", "Pronounce":"/ɡʊdz/", "Meaning":"Hàng hóa"},
  {"vocabId":71, "Topic":"Shopping", "Word":"Bag", "Pronounce":"/bæɡ/", "Meaning":"Túi"},
  {"vocabId":72, "Topic":"Shopping", "Word":"Trolley", "Pronounce":"/ˈtrɒl.i/", "Meaning":"Xe đẩy"},
  {"vocabId":73, "Topic":"Shopping", "Word":"Staff", "Pronounce":"/stɑːf/", "Meaning":"Nhân viên"},
  {"vocabId":74, "Topic":"Shopping", "Word":"Bill", "Pronounce":"/bɪl/", "Meaning":"Hóa đơn"},
  {"vocabId":75, "Topic":"Shopping", "Word":"Item", "Pronounce":"/ˈaɪ.təm/", "Meaning":"Đồ (vật phẩm)"},

  {"vocabId":76, "Topic":"Health", "Word":"Health", "Pronounce":"/helθ/", "Meaning":"Sức khỏe"},
  {"vocabId":77, "Topic":"Health", "Word":"Healthy", "Pronounce":"/ˈhel.θi/", "Meaning":"Khỏe mạnh"},
  {"vocabId":78, "Topic":"Health", "Word":"Healthy eating", "Pronounce":"/ˈhel.θi ˈiː.tɪŋ/", "Meaning":"Ăn uống lành mạnh"},
  {"vocabId":79, "Topic":"Health", "Word":"Exercise", "Pronounce":"/ˈek.sə.saɪz/", "Meaning":"Tập thể dục"},
  {"vocabId":80, "Topic":"Health", "Word":"Balanced diet", "Pronounce":"/ˈbæl.ənst ˈdaɪ.ət/", "Meaning":"Chế độ ăn uống cân bằng"},
  {"vocabId":81, "Topic":"Health", "Word":"Get enough sleep", "Pronounce":"/ɡet ɪˈnʌf sliːp/", "Meaning":"Ngủ đủ giấc"},
  {"vocabId":82, "Topic":"Health", "Word":"Water", "Pronounce":"/ˈwɔː.tər/", "Meaning":"Nước"},
  {"vocabId":83, "Topic":"Health", "Word":"Vitamins", "Pronounce":"/ˈvɪt.ə.mɪnz/", "Meaning":"Vitamin"},
  {"vocabId":84, "Topic":"Health", "Word":"Minerals", "Pronounce":"/ˈmɪn.ər.əlz/", "Meaning":"Khoáng chất"},
  {"vocabId":85, "Topic":"Health", "Word":"Vegetables", "Pronounce":"/ˈvedʒ.tə.bəlz/", "Meaning":"Rau xanh"},
  {"vocabId":86, "Topic":"Health", "Word":"Fruits", "Pronounce":"/fruːts/", "Meaning":"Trái cây"},
  {"vocabId":87, "Topic":"Health", "Word":"Good sleep", "Pronounce":"/ɡʊd sliːp/", "Meaning":"Ngủ ngon"},
  {"vocabId":88, "Topic":"Health", "Word":"Physical activity", "Pronounce":"/ˈfɪz.ɪ.kəl ækˈtɪv.ə.ti/", "Meaning":"Hoạt động thể chất"},
  {"vocabId":89, "Topic":"Health", "Word":"Organic food", "Pronounce":"/ɔːˈɡæn.ɪk fuːd/", "Meaning":"Thực phẩm hữu cơ"},
  {"vocabId":90, "Topic":"Health", "Word":"Avoid", "Pronounce":"/əˈvɔɪd/", "Meaning":"Tránh xa"},

  {"vocabId":91, "Topic":"Education", "Word":"School", "Pronounce":"/skuːl/", "Meaning":"Trường học"},
  {"vocabId":92, "Topic":"Education", "Word":"Classroom", "Pronounce":"/ˈklɑːs.ruːm/", "Meaning":"Lớp học"},
  {"vocabId":93, "Topic":"Education", "Word":"Student", "Pronounce":"/ˈstjuː.dənt/", "Meaning":"Học sinh/Sinh viên"},
  {"vocabId":94, "Topic":"Education", "Word":"Teacher", "Pronounce":"/ˈtiː.tʃər/", "Meaning":"Giáo viên"},
  {"vocabId":95, "Topic":"Education", "Word":"Lesson", "Pronounce":"/ˈles.ən/", "Meaning":"Bài học"},
  {"vocabId":96, "Topic":"Education", "Word":"Book", "Pronounce":"/bʊk/", "Meaning":"Sách"},
  {"vocabId":97, "Topic":"Education", "Word":"Knowledge", "Pronounce":"/ˈnɒ.lɪdʒ/", "Meaning":"Kiến thức"},
  {"vocabId":98, "Topic":"Education", "Word":"Exam", "Pronounce":"/ɪɡˈzæm/", "Meaning":"Kỳ thi"},
  {"vocabId":99, "Topic":"Education", "Word":"Homework", "Pronounce":"/ˈhoʊm.wɝːk/", "Meaning":"Bài tập về nhà"},
  {"vocabId":100, "Topic":"Education", "Word":"University", "Pronounce":"/ˌjuː.nɪˈvɜː.sə.ti/", "Meaning":"Trường đại học"},
  {"vocabId":101, "Topic":"Education", "Word":"Lecture", "Pronounce":"/ˈlek.tʃər/", "Meaning":"Bài giảng"},
  {"vocabId":102, "Topic":"Education", "Word":"Campus", "Pronounce":"/ˈkæm.pəs/", "Meaning":"Khuôn viên trường"},
  {"vocabId":103, "Topic":"Education", "Word":"Graduate", "Pronounce":"/ˈɡrædʒ.u.eɪt/", "Meaning":"Tốt nghiệp"},
  {"vocabId":104, "Topic":"Education", "Word":"Library", "Pronounce":"/ˈlaɪ.brer.i/", "Meaning":"Thư viện"},
  {"vocabId":105, "Topic":"Education", "Word":"Tuition", "Pronounce":"/tjuːˈɪʃ.ən/", "Meaning":"Học phí"},

  {"vocabId":106, "Topic":"Jobs", "Word":"Teacher", "Pronounce":"/ˈtiː.tʃər/", "Meaning":"Giáo viên"},
  {"vocabId":107, "Topic":"Jobs", "Word":"Doctor", "Pronounce":"/ˈdɒk.tər/", "Meaning":"Bác sĩ"},
  {"vocabId":108, "Topic":"Jobs", "Word":"Nurse", "Pronounce":"/nɜːs/", "Meaning":"Y tá"},
  {"vocabId":109, "Topic":"Jobs", "Word":"Engineer", "Pronounce":"/ˌen.dʒɪˈnɪər/", "Meaning":"Kỹ sư"},
  {"vocabId":110, "Topic":"Jobs", "Word":"Driver", "Pronounce":"/ˈdraɪ.vər/", "Meaning":"Tài xế"},
  {"vocabId":111, "Topic":"Jobs", "Word":"Chef", "Pronounce":"/ʃef/", "Meaning":"Đầu bếp"},
  {"vocabId":112, "Topic":"Jobs", "Word":"Police officer", "Pronounce":"/pəˈliːs ˈɒf.ɪ.sər/", "Meaning":"Cảnh sát"},
  {"vocabId":113, "Topic":"Jobs", "Word":"Farmer", "Pronounce":"/ˈfɑː.mər/", "Meaning":"Nông dân"},
  {"vocabId":114, "Topic":"Jobs", "Word":"Firefighter", "Pronounce":"/ˈfaɪəˌfaɪ.tər/", "Meaning":"Lính cứu hỏa"},
  {"vocabId":115, "Topic":"Jobs", "Word":"Pilot", "Pronounce":"/ˈpaɪ.lət/", "Meaning":"Phi công"},
  {"vocabId":116, "Topic":"Jobs", "Word":"Waiter/Waitress", "Pronounce":"/ˈweɪ.tər/ /ˈweɪ.trəs/", "Meaning":"Phục vụ"},
  {"vocabId":117, "Topic":"Jobs", "Word":"Artist", "Pronounce":"/ˈɑː.tɪst/", "Meaning":"Nghệ sĩ"},
  {"vocabId":118, "Topic":"Jobs", "Word":"Musician", "Pronounce":"/mjuːˈzɪʃ.ən/", "Meaning":"Nhạc sĩ"},
  {"vocabId":119, "Topic":"Jobs", "Word":"Writer", "Pronounce":"/ˈraɪ.tər/", "Meaning":"Nhà văn"},
  {"vocabId":120, "Topic":"Jobs", "Word":"Mechanic", "Pronounce":"/məˈkæn.ɪk/", "Meaning":"Thợ máy"},

  {"vocabId":121, "Topic":"Weather", "Word":"Rain", "Pronounce":"/reɪn/", "Meaning":"Mưa"},
  {"vocabId":122, "Topic":"Weather", "Word":"Snow", "Pronounce":"/snoʊ/", "Meaning":"Tuyết"},
  {"vocabId":123, "Topic":"Weather", "Word":"Sunny", "Pronounce":"/ˈsʌn.i/", "Meaning":"Nắng"},
  {"vocabId":124, "Topic":"Weather", "Word":"Cloudy", "Pronounce":"/ˈklaʊ.di/", "Meaning":"Có mây"},
  {"vocabId":125, "Topic":"Weather", "Word":"Storm", "Pronounce":"/stɔːrm/", "Meaning":"Bão"},
  {"vocabId":126, "Topic":"Weather", "Word":"Windy", "Pronounce":"/ˈwɪn.di/", "Meaning":"Có gió"},
  {"vocabId":127, "Topic":"Weather", "Word":"Foggy", "Pronounce":"/ˈfɒɡ.i/", "Meaning":"Có sương mù"},
  {"vocabId":128, "Topic":"Weather", "Word":"Cold", "Pronounce":"/koʊld/", "Meaning":"Lạnh"},
  {"vocabId":129, "Topic":"Weather", "Word":"Hot", "Pronounce":"/hɑːt/", "Meaning":"Nóng"},
  {"vocabId":130, "Topic":"Weather", "Word":"Humidity", "Pronounce":"/hjuːˈmɪd.ɪ.ti/", "Meaning":"Độ ẩm"},
  {"vocabId":131, "Topic":"Weather", "Word":"Temperature", "Pronounce":"/ˈtem.prə.tʃər/", "Meaning":"Nhiệt độ"},
  {"vocabId":132, "Topic":"Weather", "Word":"Lightning", "Pronounce":"/ˈlaɪt.nɪŋ/", "Meaning":"Sấm chớp"},
  {"vocabId":133, "Topic":"Weather", "Word":"Thunder", "Pronounce":"/ˈθʌn.dər/", "Meaning":"Sấm"},
  {"vocabId":134, "Topic":"Weather", "Word":"Hurricane", "Pronounce":"/ˈhʌr.ɪ.keɪn/", "Meaning":"Bão lớn"},
  {"vocabId":135, "Topic":"Weather", "Word":"Tornado", "Pronounce":"/tɔːrˈneɪ.doʊ/", "Meaning":"Lốc xoáy"},

  {"vocabId":136, "Topic":"Environment", "Word":"Environment", "Pronounce":"/ɪnˈvaɪ.rən.mənt/", "Meaning":"Môi trường"},
  {"vocabId":137, "Topic":"Environment", "Word":"Pollution", "Pronounce":"/pəˈluː.ʃən/", "Meaning":"Ô nhiễm"},
  {"vocabId":138, "Topic":"Environment", "Word":"Recycle", "Pronounce":"/riːˈsaɪ.kəl/", "Meaning":"Tái chế"},
  {"vocabId":139, "Topic":"Environment", "Word":"Waste", "Pronounce":"/weɪst/", "Meaning":"Rác thải"},
  {"vocabId":140, "Topic":"Environment", "Word":"Climate change", "Pronounce":"/ˈklaɪ.mət tʃeɪndʒ/", "Meaning":"Biến đổi khí hậu"},
  {"vocabId":141, "Topic":"Environment", "Word":"Deforestation", "Pronounce":"/diːˌfɒr.ɪˈsteɪ.ʃən/", "Meaning":"Phá rừng"},
  {"vocabId":142, "Topic":"Environment", "Word":"Endangered species", "Pronounce":"/ɪnˈdeɪn.dʒərd ˈspiː.ʃiːz/", "Meaning":"Các loài có nguy cơ tuyệt chủng"},
  {"vocabId":143, "Topic":"Environment", "Word":"Conservation", "Pronounce":"/ˌkɒn.səˈveɪ.ʃən/", "Meaning":"Bảo tồn"},
  {"vocabId":144, "Topic":"Environment", "Word":"Sustainability", "Pronounce":"/səˌsteɪ.nəˈbɪl.ə.ti/", "Meaning":"Sự bền vững"},
  {"vocabId":145, "Topic":"Environment", "Word":"Renewable energy", "Pronounce":"/rɪˈnjuː.ə.bəl ˈen.ə.dʒi/", "Meaning":"Năng lượng tái tạo"},
  {"vocabId":146, "Topic":"Environment", "Word":"Solar power", "Pronounce":"/ˈsoʊ.lɚ ˈpaʊ.ɚ/", "Meaning":"Năng lượng mặt trời"},
  {"vocabId":147, "Topic":"Environment", "Word":"Wind power", "Pronounce":"/wɪnd ˈpaʊ.ɚ/", "Meaning":"Năng lượng gió"},
  {"vocabId":148, "Topic":"Environment", "Word":"Greenhouse effect", "Pronounce":"/ˈɡriːn.haʊs ɪˈfekt/", "Meaning":"Hiệu ứng nhà kính"},
  {"vocabId":149, "Topic":"Environment", "Word":"Carbon footprint", "Pronounce":"/ˈkɑːr.bən ˈfʊt.prɪnt/", "Meaning":"Dấu chân carbon"},
  {"vocabId":150, "Topic":"Environment", "Word":"Trash", "Pronounce":"/træʃ/", "Meaning":"Rác"},
]

# Gom vocab theo topic
topic_vocab = defaultdict(list)
for v in vocab_data:
    topic_vocab[v["Topic"]].append(v)

result = {}

for topic, vocabs in topic_vocab.items():
    questions = {}
    meanings_pool = [v["Meaning"] for v in vocabs]

    for idx, v in enumerate(vocabs, start=1):
        correct = v["Meaning"]
        wrong_options = [m for m in meanings_pool if m != correct]
        wrong_choices = random.sample(wrong_options, min(3, len(wrong_options)))

        question = {
            "question": v["Word"],
            "option1": correct,
            "option2": wrong_choices[0] if len(wrong_choices) > 0 else "",
            "option3": wrong_choices[1] if len(wrong_choices) > 1 else "",
            "option4": wrong_choices[2] if len(wrong_choices) > 2 else "",
            "correctAnswer": correct
        }

        questions[f"q{idx}"] = question  # 👈 Dùng key dạng "q1", "q2", ...

    result[topic] = questions

# Ghi ra file
with open("quiz_questions.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("✅ Đã tạo file quiz_questions.json theo định dạng Object với key q1, q2, ...")