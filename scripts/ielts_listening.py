with open(
    "ielts_listening.txt",
    "r",
    encoding="utf-8",
) as f:
    lines = f.readlines()

category_translation_pairs = {}
current_category = None
current_sub_category = None
current_sub_category_dict = None

for line in lines:
    # 去除行尾的换行符
    line = line.strip()
    # 检查行是否表示一个类别
    if "：" in line:
        # 获取类别名称
        current_category = line.split("：")[-1]
        # 初始化当前类别的字典
        category_translation_pairs[current_category] = {}
    else:
        # 分割行
        parts = line.split(" ")
        if len(parts) == 1 and parts[0]:
            # 获取子类别名称
            current_sub_category = parts[0]
            # 初始化当前子类别的字典
            current_sub_category_dict = {}
            category_translation_pairs[current_category][
                current_sub_category
            ] = current_sub_category_dict
        else:
            # 获取单词或短语和译文
            word_or_phrase = " ".join(parts[1:-1])
            translation = parts[-1]
            if word_or_phrase and translation and current_sub_category_dict is not None:
                current_sub_category_dict[word_or_phrase.lower()] = translation.lower()

print(category_translation_pairs)
