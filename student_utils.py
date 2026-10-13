def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不为 2")
    name, score_str = parts
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError("成绩无法转为整数: " + score_str)
    if not (0 <= score <= 100):
        raise ValueError("成绩超出 0~100 范围: " + str(score))
    return name, score
