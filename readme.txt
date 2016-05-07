##wrapper
	洗数据

##find journal.py 
	input: dblp.xml
	output: result4.txt
	查找in proceedings期刊 不知道有什么用

data_handle.py
	input: new_data.txt
	output: final_data.txt

  data_analysis.py
	input: final_data.txt
	output: author_number.csv //task2

  FPTree.py & test.py / close_pattern.py //task1
	input: final_data.txt
	output: frequent_pattern.txt
	挖掘频繁项

  partner.py
	input: final_data.txt
	output: relation.txt

average_active_year.py
	input: new_data.txt
	output: active_year.txt
	活跃年份 
	
    teacher.py //task3
	input: relation.txt active_year.txt
	output: teacher.txt
	师生关系

conf_data
	input: new_data.txt
	output: init 11个数据库.txt

  page_rank //task4
	input: 11个数据库.txt
	output: influence.txt result11个数据库.txt
	每本杂志里影响最大的人
