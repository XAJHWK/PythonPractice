'''
改革开放近 40 年，中国取得了世界瞩目的发展成就，人民生活水
平显著提高，越来越多人开始关注“身体质量”，其中，肥胖程度最受 关注。
身体质量指数(BMI，Body Mass Index)是国际上常用的衡量 人体肥胖程度和是否健康的重要标准，
主要用于统计分析。肥胖程度 的判断不能采用体重的绝对值，它天然与身高有关。
因此，BMI 通过 人体体重和身高两个数值获得相对客观的参数，并用这个参数所处范 围衡量身体质量。
BMI 的定义如下: BMI = 体重(kg) 身高 2(m2)
国内外有两种不同的标准，请输出两种不同的标准
'''
while True:
    kg =  float(input("请输入体重 单位kg ："))
    m = float(input("请输入身高，单位m ："))
    bim = kg/(m*m)
    if bim <18.5:
        print(bim,'国内：偏瘦 国际：偏瘦')
    elif 18.5<bim<24:
        print(bim,'国内：正常 国际：正常')
    elif 24<=bim<=25:
        print(bim,'国内：偏胖 国际：正常')
    elif 25<bim<=28:
        print(bim,'国内：偏胖 国际：偏胖')
    elif 28<bim<=30:
        print(bim,'国内：肥胖 国际：偏胖')
    else:
        print(bim + "偏胖") 
    