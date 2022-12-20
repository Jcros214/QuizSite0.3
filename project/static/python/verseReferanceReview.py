import json
from typing import Dict, List
import random

with open("project/static/json/material.json", 'r') as jsonfile:
	material = json.load(jsonfile)

material: Dict[str, Dict[str, List]]

mychapters = [
	material['IICor']['5'],
	# material['IICor']['6'],	
]


nums = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

missed = []

chapter = mychapters[0]

random.shuffle(nums)

for verse in nums:
	if int(verse) < len(chapter):
		print(chapter[int(verse)-1])
		ans = int(input())

		if ans != int(verse):
			missed.append(verse)

		print(int(verse))

missed2 =  missed.copy()

for verse in missed2:
	if int(verse) < len(chapter):
		print(chapter[int(verse)-1])
		ans = int(input())

		if ans != int(verse):
			missed.append(verse)

		print(int(verse))
